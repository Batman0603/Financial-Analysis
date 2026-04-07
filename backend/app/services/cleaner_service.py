import pandas as pd


def clean_dataframe(df: pd.DataFrame):
    try:
        # 1. Drop fully empty rows
        df = df.dropna(how="all")

        # 2. Rename first column as 'particulars'
        df = df.rename(columns={df.columns[0]: "particulars"})

        # 3. Remove rows where particulars is NaN
        df = df[df["particulars"].notna()]

        # 4. Remove header-like rows
        df = df[~df["particulars"].astype(str).str.contains("particulars", case=False, na=False)]

        # 5. Convert numeric columns
        for col in df.columns[1:]:
            df[col] = pd.to_numeric(df[col], errors="coerce")

        # 6. Fill NaN with 0
        df = df.fillna(0)

        return df

    except Exception as e:
        raise Exception(f"Cleaning error: {str(e)}")


def filter_financial_rows(df: pd.DataFrame):
    try:
        keywords = [
            "sales",
            "revenue",
            "income",
            "wages",
            "expense",
            "depreciation",
            "tax",
            "profit"
        ]

        exclude_keywords = [
            "ratio",
            "%",
            "decrease",
            "increase",
            "calculation",
            "if the",
            "total actual",
            "budget",
            "disclaimer"
        ]

        # ✅ Include important rows
        df = df[
            df["particulars"]
            .astype(str)
            .str.lower()
            .str.contains("|".join(keywords), na=False)
        ]

        # ❌ Remove calculated / junk rows
        df = df[
            ~df["particulars"]
            .astype(str)
            .str.lower()
            .str.contains("|".join(exclude_keywords), na=False)
        ]

        # ❌ Remove duplicates
        df = df.drop_duplicates(subset=["particulars"])

        return df

    except Exception as e:
        raise Exception(f"Filtering error: {str(e)}")