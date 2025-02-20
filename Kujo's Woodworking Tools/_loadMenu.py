import FreeCAD
import FreeCADGui
import os
import __Init__

translate = FreeCAD.Qt.translate

def QT_TRANSLATE_NOOP(context, text):
    return text
path = os.path.dirname(__Init__.__file__)
iconPath = os.path.join(path, "Icons")

# ######################################################################################################################
class BoardFootCalculator():

    def GetResources(self):
        return {"Pixmap": os.path.join(iconPath, "board_foot_calculator.png"),
                "MenuText": QT_TRANSLATE_NOOP('BoardFootCalculator', 'Board Foot Calculator'),
                "ToolTip": QT_TRANSLATE_NOOP('BoardFootCalculator', 'Calculate board feet and update the spreadsheet.'),
                "Accel": ""}

    def Activated(self):
        import os, sys, __Init__
        module = "board_foot_calculator"
        path = os.path.dirname(__Init__.__file__)
        tools_path = os.path.join(path, "Tools")

        if tools_path not in sys.path:
            sys.path.append(tools_path)

        if module in sys.modules:
            del sys.modules[module]

        board_foot_calculator = __import__(module, globals(), locals(), [], 0)
        board_foot_calculator.calculate_board_feet()  # Correct function call.

        sys.path.remove(tools_path)
        return

    def IsActive(self):
        return True

FreeCADGui.addCommand("board_foot_calculator", BoardFootCalculator())
print("Registered board_foot_calculator")
# ######################################################################################################################
class BoardLayoutMacro():

    def GetResources(self):
        return {"Pixmap": os.path.join(iconPath, "board_layout_macro.png"),
                "MenuText": QT_TRANSLATE_NOOP('BoardLayoutMacro', 'Board Layout Visualizer'),
                "ToolTip": QT_TRANSLATE_NOOP('BoardLayoutMacro', 'Visualize and optimize board layout.'),
                "Accel": ""}

    def Activated(self):
        import os, sys, __Init__
        module = "board_layout_macro"
        path = os.path.dirname(__Init__.__file__)
        tools_path = os.path.join(path, "Tools")

        if tools_path not in sys.path:
            sys.path.append(tools_path)

        if module in sys.modules:
            del sys.modules[module]

        board_layout_macro = __import__(module, globals(), locals(), [], 0)
        board_layout_macro.MainLauncher().exec_()  # Launch the main GUI.

        sys.path.remove(tools_path)
        return


    def IsActive(self):
        return True

FreeCADGui.addCommand("board_layout_macro", BoardLayoutMacro())

# ######################################################################################################################
class PopulateSpreadsheet():

    def GetResources(self):
        return {"Pixmap": os.path.join(iconPath, "populate_spreadsheet.png"),
                "MenuText": QT_TRANSLATE_NOOP('PopulateSpreadsheet', 'Populate Spreadsheet'),
                "ToolTip": QT_TRANSLATE_NOOP('PopulateSpreadsheet', 'Populate the spreadsheet with predefined headers.'),
                "Accel": ""}

    def Activated(self):
        import os, sys, __Init__
        module = "populate_spreadsheet"
        path = os.path.dirname(__Init__.__file__)
        tools_path = os.path.join(path, "Tools")

        if tools_path not in sys.path:
            sys.path.append(tools_path)

        if module in sys.modules:
            del sys.modules[module]

        populate_spreadsheet = __import__(module, globals(), locals(), [], 0)
        populate_spreadsheet.run()  # Correct function call.

        sys.path.remove(tools_path)
        return

    def IsActive(self):
        return True

FreeCADGui.addCommand("populate_spreadsheet", PopulateSpreadsheet())

# ######################################################################################################################
class ExportCSV():

    def GetResources(self):
        return {"Pixmap": os.path.join(iconPath, "export_csv.png"),
                "MenuText": QT_TRANSLATE_NOOP('ExportCSV', 'Export CSV'),
                "ToolTip": QT_TRANSLATE_NOOP('ExportCSV', 'Export data to CSV format.'),
                "Accel": ""}

    def Activated(self):
        import os, sys, __Init__
        module = "export_csv"
        path = os.path.dirname(__Init__.__file__)
        tools_path = os.path.join(path, "Tools")

        if tools_path not in sys.path:
            sys.path.append(tools_path)

        if module in sys.modules:
            del sys.modules[module]

        export_csv = __import__(module, globals(), locals(), [], 0)
        export_csv.exportCSV()  # Correct function call.

        sys.path.remove(tools_path)
        return

    def IsActive(self):
        return True

FreeCADGui.addCommand("export_csv", ExportCSV())

# ######################################################################################################################

def getItems():

	parts = []

	parts = [ 
		"board_foot_calculator",
        "board_layout_macro",
        "populate_spreadsheet",
        "export_csv"
	]

	return parts
