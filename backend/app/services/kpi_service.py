import pandas as pd


def get_main_value(df: pd.DataFrame):
    try:
        numeric_cols = df.select_dtypes(include="number").columns

        if len(numeric_cols) == 0:
            return 0

        # Take first meaningful column
        return df[numeric_cols[0]]

    except Exception:
        return 0


def extract_value(df: pd.DataFrame, keyword: str):
    try:
        rows = df[
            df["particulars"]
            .astype(str)
            .str.lower()
            .str.contains(keyword, na=False)
        ]

        if rows.empty:
            return 0

        numeric_cols = df.select_dtypes(include="number").columns

        for _, row in rows.iterrows():
            for col in numeric_cols:
                value = row[col]
                if value != 0 and abs(value) > 1:
                    return float(value)

        return 0

    except Exception:
        return 0


def calculate_kpis(pnl_df: pd.DataFrame):
    try:
        revenue = extract_value(pnl_df, "sales|revenue")
        profit = extract_value(pnl_df, "profit")
        expenses = extract_value(pnl_df, "expense|wages|depreciation")

        profit_margin = (profit / revenue * 100) if revenue else 0
        expense_ratio = (expenses / revenue * 100) if revenue else 0

        return {
            "revenue": round(revenue, 2),
            "profit": round(profit, 2),
            "expenses": round(expenses, 2),
            "profit_margin_%": round(profit_margin, 2),
            "expense_ratio_%": round(expense_ratio, 2),
        }

    except Exception as e:
        raise Exception(f"KPI calculation error: {str(e)}")