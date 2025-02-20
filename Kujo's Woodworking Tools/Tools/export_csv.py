import FreeCAD as App
import csv
from PySide import QtGui
def exportCSV():
    """Export spreadsheet data to a CSV file."""
    doc = App.ActiveDocument
    spreadsheet = doc.getObject("Spreadsheet") 
    if not spreadsheet:
        App.Console.PrintError("No spreadsheet found!\n")
        return
    
     
    file_path, _ = QtGui.QFileDialog.getSaveFileName(None, "Save CSV", "", "CSV Files (*.csv)")

    if file_path:
        if not file_path.endswith(".csv"):
            file_path += ".csv"
        
        with open(file_path, "w", newline='') as csvfile:
            writer = csv.writer(csvfile)
            for row in range(1, 100):  # Example: Export first 100 rows
                row_data = []
                for col in range(1, 10):  # Example: First 10 columns
                    cell = f"{chr(64 + col)}{row}"  # Convert column number to letter (A, B, C...)
                    value = spreadsheet.get(cell)
                    row_data.append(value if value is not None else "")
                writer.writerow(row_data)
        
        App.Console.PrintMessage(f"CSV exported to {file_path}\n")
