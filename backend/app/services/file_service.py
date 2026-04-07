import pandas as pd

def read_excel_file(file_path: str):
    try:
        xls = pd.ExcelFile(file_path)
        sheets = {}

        for sheet_name in xls.sheet_names:
            try:
                df = xls.parse(sheet_name)
                sheets[sheet_name] = df
            except Exception:
                continue  # skip bad sheets

        if not sheets:
            raise ValueError("No readable sheets found")

        return sheets

    except Exception as e:
        raise Exception(f"Error reading Excel: {str(e)}")