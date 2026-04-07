import re
import pandas as pd


def detect_year_columns(df: pd.DataFrame):
    try:
        new_columns = []
        year_pattern = re.compile(r"(20\d{2})")

        for col in df.columns:
            match = year_pattern.search(str(col))
            if match:
                new_columns.append(match.group(1))
            else:
                new_columns.append(col)

        df.columns = new_columns
        return df

    except Exception as e:
        raise Exception(f"Column detection error: {str(e)}")