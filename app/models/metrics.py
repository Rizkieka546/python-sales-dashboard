from pydantic import BaseModel


class SummaryResponse(BaseModel):
    total_records: int
    total_amount: float
    average_amount: float
    growth_percentage: float


class DailyTimeSeriesItem(BaseModel):
    date: str
    total_amount: float


class MonthlyTimeSeriesItem(BaseModel):
    month: str
    total_amount: float


class CategoryItem(BaseModel):
    category: str
    total_amount: float
