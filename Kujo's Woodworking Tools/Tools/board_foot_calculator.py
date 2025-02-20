import FreeCAD

def extract_numeric(value):
    value = value.strip()
    if value.startswith('='):
        value = value[1:]  # Remove '='
    value = value.replace('in', '').strip()  # Remove 'in'

    try:
        # Try evaluating simple expressions like '13.25 / 3.5'
        return float(eval(value))
    except:
        return float(value) if value else 0

def calculate_board_feet():
    doc = FreeCAD.ActiveDocument
    spreadsheet = doc.getObject("Spreadsheet")

    row = 2
    total_board_feet = 0  # Initialize total board feet

    while True:
        length_cell = spreadsheet.getContents(f"C{row}")
        print(f"Checking row {row}, Length cell: '{length_cell}'")

        if not length_cell.strip():
            print(f"Stopping at row {row} because Length is empty.")
            break

        print(f"Proceeding to try block for row {row}")

        try:
            quantity = extract_numeric(spreadsheet.getContents(f"B{row}"))  # Column B
            length = extract_numeric(spreadsheet.getContents(f"E{row}"))    # Column E
            width = extract_numeric(spreadsheet.getContents(f"F{row}"))     # Column F
            height = extract_numeric(spreadsheet.getContents(f"G{row}"))    # Column G

            print(f"Row {row}: Quantity={quantity}, Length={length}, Width={width}, Height={height}")

            if quantity <= 0 or length <= 0 or width <= 0 or height <= 0:
                print(f"Invalid data in row {row}: Values must be > 0.")
                row += 1
                continue

            board_feet = (quantity * length * width * height) / 144
            spreadsheet.set(f"H{row}", str(round(board_feet, 2)))  # ✅ Corrected this line
            print(f"Board feet written: {round(board_feet, 2)}")

            total_board_feet += board_feet  # Accumulate the total

        except ValueError as ve:
            print(f"Invalid data format in row {row}: {ve}")
        except Exception as ex:
            print(f"Unexpected error in row {row}: {ex}")

        row += 1

    # Write the total board feet at the bottom of the Board Feet column
    total_row = row  # This is the first empty row after the data
    spreadsheet.set(f"G{total_row}", "Total Board Feet:")
    spreadsheet.set(f"H{total_row}", str(round(total_board_feet, 2)))

    doc.recompute()
    print("Board feet calculations completed successfully.")
