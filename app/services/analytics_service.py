import pandas as pd
from app.utils.data_loader import load_data


class AnalyticsService:
    def __init__(self):
        self.df = load_data()
        self.df["date"] = pd.to_datetime(self.df["date"])

    # =====================
    # SUMMARY
    # =====================
    def summary(self):
        total_records = len(self.df)
        total_amount = float(self.df["amount"].sum())
        average_amount = float(self.df["amount"].mean())

        daily = self.df.groupby("date")["amount"].sum().sort_index()
        growth = 0.0

        if len(daily) > 1 and daily.iloc[0] != 0:
            growth = ((daily.iloc[-1] - daily.iloc[0]) / daily.iloc[0]) * 100

        return {
            "total_records": total_records,
            "total_amount": total_amount,
            "average_amount": average_amount,
            "growth_percentage": round(growth, 2),
        }

    # =====================
    # DAILY TIMESERIES (📈)
    # =====================
    def timeseries_daily(self):
        grouped = (
            self.df
            .groupby("date")["amount"]
            .sum()
            .reset_index()
            .sort_values("date")
        )

        return [
            {
                "date": row["date"].strftime("%Y-%m-%d"),
                "total_amount": float(row["amount"]),
            }
            for _, row in grouped.iterrows()
        ]

    # =====================
    # MONTHLY TIMESERIES (📊)
    # =====================
    def timeseries_monthly(self):
        df = self.df.copy()
        df["month"] = df["date"].dt.to_period("M")

        grouped = (
            df
            .groupby("month")["amount"]
            .sum()
            .reset_index()
            .sort_values("month")
        )

        return [
            {
                "month": row["month"].strftime("%b"),  # Jan, Feb, Mar
                "total_amount": float(row["amount"]),
            }
            for _, row in grouped.iterrows()
        ]

    # =====================
    # CATEGORY
    # =====================
    def category(self):
        grouped = (
            self.df
            .groupby("category")["amount"]
            .sum()
            .reset_index()
            .sort_values("amount", ascending=False)
        )

        return [
            {
                "category": row["category"],
                "total_amount": float(row["amount"]),
            }
            for _, row in grouped.iterrows()
        ]
