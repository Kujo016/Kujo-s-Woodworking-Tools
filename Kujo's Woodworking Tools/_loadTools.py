# This file has been automatically generated for KujoWorkbench tools.
print("loadTools.py is running")

import FreeCAD, FreeCADGui
import os, sys
import __Init__  

translate = FreeCAD.Qt.translate

def QT_TRANSLATE_NOOP(context, text):
    return text

path = os.path.dirname(__Init__.__file__)
iconPath = os.path.join(path, "Icons")

# ######################################################################################################################
# Create tool classes
# ######################################################################################################################

class board_foot_calculator:

    def GetResources(self):
        return {
            "Pixmap": os.path.join(iconPath, "board_foot_calculator.png"),
            "MenuText": QT_TRANSLATE_NOOP("board_foot_calculator", "Board Foot Calculator"),
            "ToolTip": QT_TRANSLATE_NOOP("board_foot_calculator", "Calculate board feet for a given set of dimensions."),
            "Accel": ""
        }

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

FreeCADGui.addCommand("board_foot_calculator", board_foot_calculator())
print("Registered board_foot_calculator")

# ######################################################################################################################

class board_layout_macro:

    def GetResources(self):
        return {
            "Pixmap": os.path.join(iconPath, "board_layout_macro.png"),
            "MenuText": QT_TRANSLATE_NOOP("board_layout_macro", "Board Layout Macro"),
            "ToolTip": QT_TRANSLATE_NOOP("board_layout_macro", "Visualize and optimize board layouts."),
            "Accel": ""
        }

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

FreeCADGui.addCommand("board_layout_macro", board_layout_macro())
print("Registered board_layout_macro")
# ######################################################################################################################

class populate_spreadsheet:

    def GetResources(self):
        return {
            "Pixmap": os.path.join(iconPath, "populate_spreadsheet.png"),
            "MenuText": QT_TRANSLATE_NOOP("populate_spreadsheet", "Populate Spreadsheet"),
            "ToolTip": QT_TRANSLATE_NOOP("populate_spreadsheet", "Populate a spreadsheet with predefined headers."),
            "Accel": ""
        }

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

FreeCADGui.addCommand("populate_spreadsheet", populate_spreadsheet())
print("Registered populate_spreadsheet")
# ######################################################################################################################

class export_csv:

    def GetResources(self):
        return {
            "Pixmap": os.path.join(iconPath, "export_csv.png"),
            "MenuText": QT_TRANSLATE_NOOP("export_csv", "Export to CSV"),
            "ToolTip": QT_TRANSLATE_NOOP("export_csv", "Export data to CSV format."),
            "Accel": ""
        }

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

FreeCADGui.addCommand("export_csv", export_csv())
print("Registered export_csv")
# ######################################################################################################################
# End of file
