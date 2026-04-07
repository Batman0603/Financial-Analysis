import pandas as pd

from app.services.file_service import read_excel_file
from app.services.parser_service import classify_sheets
from app.services.cleaner_service import clean_dataframe, filter_financial_rows
from app.services.column_service import detect_year_columns
from app.services.kpi_service import calculate_kpis
from app.services.insight_service import generate_insights


# ✅ Safe DataFrame → JSON converter
def safe_to_dict(df: pd.DataFrame):
    try:
        if df is None or df.empty:
            return []

        df = df.copy()

        # Convert NaN / inf to safe values
        df = df.replace([float("inf"), float("-inf")], 0)
        df = df.fillna(0)

        return df.to_dict(orient="records")

    except Exception as e:
        raise Exception(f"Conversion error: {str(e)}")


# ✅ Main analysis pipeline
def process_financial_file(file):
    try:
        # -----------------------------
        # STEP 1: Read Excel
        # -----------------------------
        excel_data = read_excel_file(file)

        if not excel_data:
            raise Exception("Empty or invalid Excel file")

        # -----------------------------
        # STEP 2: Classify sheets
        # -----------------------------
        classified = classify_sheets(excel_data)

        if not isinstance(classified, dict):
            raise Exception("Sheet classification failed")

        cleaned_data = {}
        kpis = {}

        # -----------------------------
        # STEP 3: Process each sheet
        # -----------------------------
        for key in ["pnl", "balance_sheet", "cashflow"]:
            df = classified.get(key)

            if df is None or not isinstance(df, pd.DataFrame):
                cleaned_data[key] = []
                continue

            try:
                # 👉 Detect year columns
                df = detect_year_columns(df)

                # 👉 Clean data
                df = clean_dataframe(df)

                # 👉 Filter important financial rows
                df = filter_financial_rows(df)

                # 👉 Convert to JSON-safe format
                cleaned_data[key] = safe_to_dict(df)

                # 👉 KPI calculation (only for PnL)
                if key == "pnl":
                    kpis = calculate_kpis(df)

            except Exception as sheet_error:
                cleaned_data[key] = {
                    "error": f"{key} processing failed: {str(sheet_error)}"
                }

        # -----------------------------
        # STEP 4: Final response
        # -----------------------------
        insights = generate_insights(kpis)
        return {
            "status": "success",
            "data": cleaned_data,
            "kpis": kpis,
            "insights": insights
        }
    except Exception as e:
        return {
            "status": "error",
            "message": f"Processing error: {str(e)}"
        }