import pandas as pd
from app.services.file_service import read_excel_file
from app.services.parser_service import classify_sheets
from app.services.cleaner_service import clean_dataframe, filter_financial_rows

def safe_to_dict(df):
    try:
        return df.where(pd.notnull(df), None).to_dict(orient="records")
    except Exception:
        return []


def process_financial_file(file_path: str):
    try:
        sheets = read_excel_file(file_path)
        classified = classify_sheets(sheets)

        if all(value is None for value in classified.values()):
            raise ValueError("Could not detect financial statements")

        cleaned_data = {}

        for key, df in classified.items():
            if df is not None:
                cleaned_df = clean_dataframe(df)
                cleaned_df = filter_financial_rows(cleaned_df)
                cleaned_data[key] = safe_to_dict(cleaned_df)
            else:
                cleaned_data[key] = None

        return cleaned_data

    except Exception as e:
        raise Exception(f"Processing error: {str(e)}")