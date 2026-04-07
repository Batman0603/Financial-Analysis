def detect_statement_type(df):
    """
    Detect whether sheet is:
    PNL / Balance Sheet / Cash Flow
    """

    try:
        text = " ".join(df.astype(str).fillna("").values.flatten()).lower()

        if any(x in text for x in ["revenue", "profit", "expense"]):
            return "pnl"

        elif any(x in text for x in ["assets", "liabilities", "equity"]):
            return "balance_sheet"

        elif any(x in text for x in ["cash flow", "operating activities"]):
            return "cash_flow"

        return "unknown"

    except Exception:
        return "unknown"


def classify_sheets(sheets: dict):
    classified = {
        "pnl": None,
        "balance_sheet": None,
        "cash_flow": None
    }

    for name, df in sheets.items():
        sheet_type = detect_statement_type(df)

        if sheet_type in classified and classified[sheet_type] is None:
            classified[sheet_type] = df

    return classified