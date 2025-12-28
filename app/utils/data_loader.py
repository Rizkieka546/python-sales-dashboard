import pandas as pd
from app.core.config import settings

def load_data() -> pd.DataFrame:
    df = pd.read_csv(settings.DATA_PATH)
    df["date"] = pd.to_datetime(df["date"])
    return df
