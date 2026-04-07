def calculate_growth(current, previous):
    try:
        if previous == 0:
            return 0
        return round(((current - previous) / previous) * 100, 2)
    except Exception:
        return 0


def generate_insights(kpis):
    try:
        insights = []

        if kpis["profit"] < 0:
            insights.append("⚠️ Company is running at a loss")

        if kpis["profit_margin_%"] < 10:
            insights.append("⚠️ Low profit margin")

        if kpis["expense_ratio_%"] > 70:
            insights.append("⚠️ Expenses are too high")

        if not insights:
            insights.append("✅ Financials look stable")

        return insights

    except Exception:
        return ["Insight generation failed"]