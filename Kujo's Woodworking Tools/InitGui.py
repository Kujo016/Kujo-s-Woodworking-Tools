# InitGui.py
# Initializes KujoWorkbench in FreeCAD.
import FreeCAD, FreeCADGui
import sys, os

class KujoWorkbench(FreeCADGui.Workbench):
    
    translate = FreeCAD.Qt.translate
    def QT_TRANSLATE_NOOP(context, text):
        return text
    import __Init__
    path = os.path.dirname(__Init__.__file__)
    iconPath = os.path.join(path,"Icons")
    translationsPath = os.path.join(path, "translations")

    MenuText = QT_TRANSLATE_NOOP("KujoWorkbench", "Kujo's Tools")
    ToolTip = QT_TRANSLATE_NOOP("KujoWorkbench", "Workbench for woodworking design.")
    Icon = os.path.join(iconPath, "k_workbench_icon.png")
    def Initialize(self):
        import _loadToolbar
        import _loadMenu
        def QT_TRANSLATE_NOOP(context, text):
            return text
        FreeCADGui.addLanguagePath(self.translationsPath)
        
        #Toolbar
        print("Toolbar Layout and Visualization items:", _loadToolbar.getItems("KujoWorkbench - Layout and Visualization"))
        self.appendToolbar(QT_TRANSLATE_NOOP("KujoWorkbench", "KujoWorkbench - Layout and Visualization"),
                           _loadToolbar.getItems("KujoWorkbench - Layout and Visualization"))
        print("Toolbar Spreadsheet Tools items:", _loadToolbar.getItems("KujoWorkbench - Spreadsheet Tools"))
        self.appendToolbar(QT_TRANSLATE_NOOP("KujoWorkbench", "KujoWorkbench - Spreadsheet Tools"), 
                           _loadToolbar.getItems("KujoWorkbench - Spreadsheet Tools"))
        
        #Menu
        self.appendMenu(QT_TRANSLATE_NOOP("KujoWorkbench", "KujoWorkbench"), _loadMenu.getItems())
        print("Menu items:", _loadMenu.getItems())
        FreeCAD.Console.PrintMessage("KujoWorkbench initialized\n")

    def Activated(self):
        FreeCAD.Console.PrintMessage("KujoWorkbench activated\n")
        return

    def Deactivated(self):
        FreeCAD.Console.PrintMessage("KujoWorkbench deactivated\n")
        return
    def ContextMenu(self, recipient):
        return
    def GetClassName(self):
        return "Gui::PythonWorkbench"


if not FreeCADGui.listWorkbenches().get("KujoWorkbench"):
    FreeCADGui.addWorkbench(KujoWorkbench())
