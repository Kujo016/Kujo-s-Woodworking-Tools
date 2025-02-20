import FreeCAD
import Spreadsheet

def get_column_letter(n):
    """Converts a zero-based index to Excel-style column letters (A, B, ..., Z, AA, AB, etc.)."""
    result = ''
    while n >= 0:
        result = chr(65 + (n % 26)) + result
        n = n // 26 - 1
    return result

def run():
    if FreeCAD.activeDocument() is None:
        FreeCAD.newDocument()

    # Check if spreadsheet exists, else create a new one
    doc = FreeCAD.ActiveDocument
    spreadsheet = doc.getObject("Spreadsheet")
    if not spreadsheet:
        spreadsheet = doc.addObject('Spreadsheet::Sheet', 'Spreadsheet')

    headers = [
        "Category", "Quantity","Part_Name", "Body_Name", "Length", "Width", "Height", "Board_Foot", "Diameter",
        "Alt_Length", "Alt_Width", "Alt_Height", "Arc_Radius", "Quantity", "Board_Foot", "Cubic_Inches",
        "Cubic_Feet", "Wood_Type", "Grain_Direction", "Kerf_Loss", "Saw_Blade_Thickness", "Edge_Radius",
        "Chamfer", "Fillet_Radius", "Offset_X", "Offset_Y", "Offset_Z", "Rotation_Angle", "Coincidence_Index",
        "Glue_Joint_Type", "Dado_Depth", "Rabbet_Depth", "Mortise_Depth", "Tenon_Length", "Spline_Thickness",
        "Dowel_Diameter", "Dowel_Spacing", "Plywood_Veneer_Thickness", "Finish_Coats"
    ]

    # Populate headers in the first row
    for col, header in enumerate(headers):
        cell = f"{get_column_letter(col)}1"
        spreadsheet.set(cell, header)
        print(f"Set {cell} to {header}")  # Debug output

    FreeCAD.ActiveDocument.recompute()
    print("Spreadsheet populated with headers successfully.")
