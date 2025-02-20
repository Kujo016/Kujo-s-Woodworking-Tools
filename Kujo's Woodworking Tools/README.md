Kujo's Woodworking Tools (FreeCAD)
## Visual Layout Tool Example
![Board Layout Example](images/board_layout_example.png)
Overview
Kujo's Woodworking Tools is a FreeCAD workbench designed for woodworking projects. These tools provide essential functionality for organizing project data, calculating board footage, optimizing board layouts, and exporting data to CSV format.

Built on the framework provided by dprojects, Kujo's tools are developed to streamline woodworking processes within FreeCAD.

Installation
Download and unzip Kujo-s-Woodworking-Tools--FreeCAD--main.zip.
Open the extracted folder Kujo-s-Woodworking-Tools--FreeCAD--main.
Place the folder in the FreeCAD mod directory:
vbnet
Copy
Edit
C:\Program Files\FreeCAD 0.21\Mod\Kujo-s-Woodworking-Tools--FreeCAD--main
Run as admin
Create a FreeCAD Spreadsheet (Kujo's Tools uses the default FreeCAD Spreadsheet).
Use populate_spreadsheet.py to generate headers.
Fill in your data for dimensions, quantity, wood type, and joint types.
Calculate Board Footage using the board_foot_calculator.py.
Generate a Visual Layout using board_layout_macro.py.
Visualize and optimize your board layout.
Export Data to CSV with export_csv.py.
Tool Descriptions
populate_spreadsheet.py
Creates or updates a FreeCAD spreadsheet with predefined headers, covering attributes such as dimensions, quantity, wood type, and joint types. Helps organize data for woodworking projects.

board_foot_calculator.py
Calculates board footage for materials listed in a FreeCAD spreadsheet. Extracts data for length, width, height, and quantity to compute board footage, ensuring accurate material estimates.

board_layout_macro.py
Provides a graphical interface for visualizing and optimizing board layouts. Users can select board sizes, filter parts by category, and adjust the layout for maximum material usage and minimal waste.

export_csv.py
Exports data from a FreeCAD spreadsheet to a CSV file (up to 100 rows and 10 columns by default). Useful for analysis and reporting in other applications.

License
Kujo's Woodworking Tools is built on the framework provided by dprojects.

dprojects' framework is licensed under the MIT License. A copy of the license is included in the tools/LICENSE file.
Kujo's tools (populate_spreadsheet.py, board_foot_calculator.py, board_layout_macro.py, export_csv.py) are distributed under the MIT License as well.
Credits
Special thanks to dprojects for providing the framework: https://github.com/dprojects.

## Support and Contact
For questions or support, please [open an issue](https://github.com/your-repo/issues).

## License
This project is built on the woodworking framework provided by dprojects, with additional tools and modifications by Kujo.  
- The core structure and menu system are adapted from dprojects.  
- All tools (populate_spreadsheet.py, board_foot_calculator.py, etc.) are original works by Kujo.  
