from pydantic import BaseModel
from typing import Optional

class StockRequest(BaseModel):
    ticker: str

class StockResponse(BaseModel):
    ticker: str
    stock_name: Optional[str] = None
    current_date: str
    last_updated_date: str
    current_price: float
    previous_close: float
    daily_change_amount: float
    daily_change_percent: float
    predicted_price_tomorrow: float
    predicted_change_amount: float
    predicted_change_percent: float
    current_volume: float
    average_volume_100d: float
    volume_ratio: float