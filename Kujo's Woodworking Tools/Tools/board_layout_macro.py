import FreeCAD, FreeCADGui
from PySide import QtGui, QtCore

# Kerf value in inches
KERF = 0.125

# Function to extract numeric values from spreadsheet cells
def extract_numeric(value):
    value = value.strip()
    if value.startswith('='):
        value = value[1:]  # Remove '='
    value = value.replace('in', '').strip()  # Remove 'in'
    try:
        return float(eval(value))  # Evaluate simple expressions
    except:
        return float(value) if value else 0

# Function to load parts data from FreeCAD spreadsheet
# List of valid categories

# Function to load parts data from FreeCAD spreadsheet with category filtering
def load_parts_from_spreadsheet(category_filter=None):
    doc = FreeCAD.ActiveDocument
    spreadsheet = doc.getObject("Spreadsheet")
    if spreadsheet is None:
        for obj in doc.Objects:
            if obj.TypeId == 'Spreadsheet::Sheet':
                spreadsheet = obj
                break
    if spreadsheet is None:
        QtGui.QMessageBox.critical(None, "Error", "No spreadsheet found in the active document.")
        return []

    parts = []
    row = 2
    while True:
        length_cell = spreadsheet.getContents(f"E{row}")
        if not length_cell.strip():
            break  # Stop reading at an empty row

        try:
            # Read the row values
            category = spreadsheet.getContents(f"A{row}").strip().strip("'\"")
            quantity = extract_numeric(spreadsheet.getContents(f"B{row}"))
            name = spreadsheet.getContents(f"C{row}")
            body = spreadsheet.getContents(f"D{row}")
            length = extract_numeric(spreadsheet.getContents(f"E{row}"))
            width = extract_numeric(spreadsheet.getContents(f"F{row}"))
            height = extract_numeric(spreadsheet.getContents(f"G{row}"))
            board_foot = extract_numeric(spreadsheet.getContents(f"H{row}"))

            # If a filter is specified, skip parts that don't match (case-insensitive)
            if category_filter and category.lower() != category_filter.lower():
                row += 1
                continue

            # Only add parts with valid (positive) values
            if quantity > 0 and length > 0 and width > 0:
                parts.append((category, quantity, name, body, length, width, height, board_foot))
                print(f"Part added: {name}, {length} x {width}, Category: {category}")

        except Exception as e:
            print(f"Error at row {row}: {e}")
        
        row += 1

    print(f"Total valid parts found: {len(parts)}")
    return parts




# -------------------------------
# Dialogs for board and category selection
# -------------------------------
class BoardSelectionDialog(QtGui.QDialog):
    def __init__(self, parent=None):
        super(BoardSelectionDialog, self).__init__(parent)
        self.setWindowTitle("Select Standard Solid Wood Boards")
        self.setGeometry(150, 150, 300, 300)
        layout = QtGui.QVBoxLayout()
        self.boardSizes = {
            "1x2 (0.75\" x 1.5\") Nominal, 96\" Length": (0.75, 1.5, 96),
            "1x4 (0.75\" x 3.5\") Nominal, 96\" Length": (0.75, 3.5, 96),
            "2x4 (1.5\" x 3.5\") Nominal, 96\" Length": (1.5, 3.5, 96),
            "4x4 (3.5\" x 3.5\") Nominal, 96\" Length": (3.5, 3.5, 96),
            "1x2 (1\" x 2\") Actual, 96\" Length": (1.0, 2.0, 96),
            "1x4 (1\" x 4\") Actual, 96\" Length": (1.0, 4.0, 96),
            "2x4 (2\" x 4\") Actual, 96\" Length": (2.0, 4.0, 96),
            "4x4 (4\" x 4\") Actual, 96\" Length": (4.0, 4.0, 96),
            "4x8 (4\' x 8\') Plywood, Size": (0.5625, 48.0, 96.0)
        }
        self.boardComboBox = QtGui.QComboBox()
        self.boardComboBox.addItems(self.boardSizes.keys())
        layout.addWidget(self.boardComboBox)
        selectButton = QtGui.QPushButton("Select")
        selectButton.clicked.connect(self.selectBoard)
        layout.addWidget(selectButton)
        self.setLayout(layout)
    
    def selectBoard(self):
        selected_board = self.boardComboBox.currentText()
        dimensions = self.boardSizes[selected_board]
        # Set the selected board dimensions in the parent and redraw layout
        self.parent().selected_board_dimensions = dimensions
        self.parent().drawLayout()
        self.accept()

class CategorySelectionDialog(QtGui.QDialog):
    def __init__(self, parent=None):
        super(CategorySelectionDialog, self).__init__(parent)
        self.setWindowTitle("Select Category")
        self.setGeometry(150, 150, 300, 200)
        layout = QtGui.QVBoxLayout()
        
        # List of allowed categories
        self.categories = ["Solid Wood", "Sheet Wood"]
        
        self.categoryComboBox = QtGui.QComboBox()
        self.categoryComboBox.addItems(self.categories)
        layout.addWidget(self.categoryComboBox)
        
        selectButton = QtGui.QPushButton("Select")
        selectButton.clicked.connect(self.selectCategory)
        layout.addWidget(selectButton)
        
        self.setLayout(layout)
    
    def selectCategory(self):
        self.parent().selected_category = self.categoryComboBox.currentText()
        self.accept()


# -------------------------------
# Main Board Layout Visualizer GUI
# -------------------------------
class BoardLayout(QtGui.QDialog):
    def __init__(self):
        super(BoardLayout, self).__init__()
        self.zoom_factor = 1.0
        self.selected_board_dimensions = (0, 0, 0)
        self.board_count = 0
        self.pan_x = 0
        self.pan_y = 0
        self.selected_category = None
        self.parts = []
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle("Board Layout Visualizer")
        self.setGeometry(100, 100, 800, 600)
        mainLayout = QtGui.QVBoxLayout()
        
        # Canvas for drawing layout
        self.canvas = QtGui.QLabel()
        self.canvas.setFixedSize(780, 500)
        self.canvas.setStyleSheet("background-color: white; border: 1px solid black;")
        mainLayout.addWidget(self.canvas)
        
        # Control panel with buttons
        controlPanel = QtGui.QHBoxLayout()
        
        loadButton = QtGui.QPushButton("Load Parts")
        loadButton.clicked.connect(self.loadParts)
        controlPanel.addWidget(loadButton)
        
        optimizeButton = QtGui.QPushButton("Optimize Layout")
        optimizeButton.clicked.connect(self.optimizeLayout)
        controlPanel.addWidget(optimizeButton)
        
        boardSelectionButton = QtGui.QPushButton("Select Board")
        boardSelectionButton.clicked.connect(self.openBoardSelection)
        controlPanel.addWidget(boardSelectionButton)
        
        # New button to select the category (instead of opening it automatically)
        selectCategoryButton = QtGui.QPushButton("Select Category")
        selectCategoryButton.clicked.connect(self.selectCategory)
        controlPanel.addWidget(selectCategoryButton)
        
        zoomInButton = QtGui.QPushButton("Zoom In")
        zoomInButton.clicked.connect(self.zoomIn)
        controlPanel.addWidget(zoomInButton)
        
        zoomOutButton = QtGui.QPushButton("Zoom Out")
        zoomOutButton.clicked.connect(self.zoomOut)
        controlPanel.addWidget(zoomOutButton)
        
        panLeftButton = QtGui.QPushButton("Pan Left")
        panLeftButton.clicked.connect(self.panLeft)
        controlPanel.addWidget(panLeftButton)
        
        panRightButton = QtGui.QPushButton("Pan Right")
        panRightButton.clicked.connect(self.panRight)
        controlPanel.addWidget(panRightButton)
        
        panUpButton = QtGui.QPushButton("Pan Up")
        panUpButton.clicked.connect(self.panUp)
        controlPanel.addWidget(panUpButton)
        
        panDownButton = QtGui.QPushButton("Pan Down")
        panDownButton.clicked.connect(self.panDown)
        controlPanel.addWidget(panDownButton)
        
        exportButton = QtGui.QPushButton("Export Layout")
        exportButton.clicked.connect(self.exportLayout)
        controlPanel.addWidget(exportButton)
        
        self.totalBoardFeetLabel = QtGui.QLabel("Total Board Feet: 0")
        controlPanel.addWidget(self.totalBoardFeetLabel)
        
        self.boardCountLabel = QtGui.QLabel("Board Count: 0")
        controlPanel.addWidget(self.boardCountLabel)
        
        mainLayout.addLayout(controlPanel)
        self.setLayout(mainLayout)
    
    def selectCategory(self):
        dialog = CategorySelectionDialog(self)
        dialog.exec_()
        if self.selected_category:
            print(f"Selected Category: {self.selected_category}")
            self.parts = load_parts_from_spreadsheet(category_filter=self.selected_category)
            if not self.parts:
                QtGui.QMessageBox.warning(self, "No Parts Found", f"No parts found for category '{self.selected_category}'.")
            self.displayTotalBoardFeet()
            self.drawLayout()

    
    def panLeft(self):
        self.pan_x -= 20
        self.drawLayout()
    
    def panRight(self):
        self.pan_x += 20
        self.drawLayout()
    
    def panUp(self):
        self.pan_y -= 20
        self.drawLayout()
    
    def panDown(self):
        self.pan_y += 20
        self.drawLayout()
    
    def openBoardSelection(self):
        dialog = BoardSelectionDialog(self)
        dialog.exec_()
    
    def loadParts(self):
        # Use the selected_category if one is chosen; otherwise load all parts.
        if self.selected_category:
            self.parts = load_parts_from_spreadsheet(category_filter=self.selected_category)
                    
        if not self.parts:
            QtGui.QMessageBox.warning(self, "No Valid Parts", "No parts found with valid categories ('Solid Wood', 'Sheet Wood').")
            return
        self.displayTotalBoardFeet()
        self.drawLayout()

    
    def optimizeLayout(self):
        if not self.parts:
            QtGui.QMessageBox.warning(None, "No Parts", "No parts found for the selected category.")
            return
        print(f"Optimizing layout for category: {self.selected_category}")
        for part in self.parts:
            print(part)
    
    def zoomIn(self):
        self.zoom_factor *= 1.2
        self.drawLayout()
    
    def zoomOut(self):
        self.zoom_factor /= 1.2
        self.drawLayout()
    
    def drawLayout(self):
        if not self.parts:
            QtGui.QMessageBox.warning(self, "Warning", "No parts available to draw.")
            return

        # Use self.parts directly since they are already filtered.
        parts_to_draw = self.parts

        pixmap = QtGui.QPixmap(self.canvas.size())
        pixmap.fill(QtCore.Qt.white)
        painter = QtGui.QPainter(pixmap)
        pen = QtGui.QPen(QtCore.Qt.black)
        pen.setWidth(2)
        painter.setPen(pen)
        
        x_offset, y_offset = 10 + self.pan_x, 10 + self.pan_y
        board_thickness, board_width, board_length = self.selected_board_dimensions
        self.board_count = 0
        current_board_length = 0

        for part in parts_to_draw:
            category, quantity, name, body, length, width, height, board_foot = part
            
            scaled_length = int(length * self.zoom_factor)
            scaled_width = int(width * self.zoom_factor)

            for _ in range(int(quantity)):
                if current_board_length <= 0 or (current_board_length - length - KERF) < 0:
                    current_board_length = board_length
                    self.board_count += 1
                    x_offset = 10 + self.pan_x
                    y_offset += int(board_width * self.zoom_factor) + 20
                    painter.drawRect(x_offset, y_offset, int(board_length * self.zoom_factor), 
                                    int(board_width * self.zoom_factor))
                
                if current_board_length >= (length + KERF):
                    painter.drawRect(x_offset, y_offset, scaled_length, scaled_width)
                    text_rect = QtCore.QRectF(x_offset, y_offset, scaled_length, scaled_width)
                    painter.drawText(text_rect, QtCore.Qt.AlignCenter, body)
                    x_offset += scaled_length + int(KERF * self.zoom_factor)
                    current_board_length -= (length + KERF)
                else:
                    current_board_length = 0  

        painter.end()
        self.canvas.setPixmap(pixmap)
        self.boardCountLabel.setText(f"Board Count: {self.board_count}")


        
    def displayTotalBoardFeet(self):
        total_board_feet = sum(part[7] for part in self.parts)
        self.totalBoardFeetLabel.setText(f"Total Board Feet: {round(total_board_feet, 2)}")
    
    def exportLayout(self):
        filePath, _ = QtGui.QFileDialog.getSaveFileName(self, "Save Layout", "", "PNG Files (*.png)")
        if filePath:
            self.canvas.pixmap().save(filePath, "PNG")

# -------------------------------
# Main Launcher Window
# -------------------------------
class MainLauncher(QtGui.QDialog):
    def __init__(self, parent=None):
        super(MainLauncher, self).__init__(parent)
        self.setWindowTitle("Main Launcher")
        self.setGeometry(200, 200, 300, 150)
        layout = QtGui.QVBoxLayout(self)
        self.openButton = QtGui.QPushButton("Open Board Layout Visualizer")
        layout.addWidget(self.openButton)
        self.openButton.clicked.connect(self.openBoardLayout)
    
    def openBoardLayout(self):
        self.boardLayout = BoardLayout()
        self.boardLayout.exec_()


# -------------------------------
# Application Entry Point
# -------------------------------
if __name__ == "__main__":
    app = QtGui.QApplication([])
    launcher = MainLauncher()
    launcher.show()
    app.exec_()
