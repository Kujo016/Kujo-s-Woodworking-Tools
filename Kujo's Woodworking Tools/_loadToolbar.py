# loadToolbar.py
# Organizes tools into logical toolbars for KujoWorkbench.
import _loadTools

def getItems(iType):
    parts = []
    if iType == "KujoWorkbench - Layout and Visualization":
        parts = ["board_layout_macro"]
    
    if iType == "KujoWorkbench - Spreadsheet Tools":
        parts = ["populate_spreadsheet", "board_foot_calculator", "export_csv"]

    return parts

