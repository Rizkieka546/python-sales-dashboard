from fastapi import APIRouter
from typing import List
from app.services.analytics_service import AnalyticsService
from app.models.metrics import (
    SummaryResponse,
    DailyTimeSeriesItem,
    MonthlyTimeSeriesItem,
    CategoryItem,
)

router = APIRouter(prefix="/metrics", tags=["Metrics"])


@router.get("/summary", response_model=SummaryResponse)
def summary():
    service = AnalyticsService()
    return service.summary()


@router.get("/timeseries/daily", response_model=List[DailyTimeSeriesItem])
def timeseries_daily():
    service = AnalyticsService()
    return service.timeseries_daily()


@router.get("/timeseries/monthly", response_model=List[MonthlyTimeSeriesItem])
def timeseries_monthly():
    service = AnalyticsService()
    return service.timeseries_monthly()


@router.get("/category", response_model=List[CategoryItem])
def category():
    service = AnalyticsService()
    return service.category()


@router.get("/health")
def health():
    return {"status": "ok"}
