from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import pandas as pd

from core.models import StockRequest, StockResponse
from core.prediction import analyze_stock_prediction

# Create router
router = APIRouter()

# Set up templates
templates = Jinja2Templates(directory="templates")

@router.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    # Serve the index.html template
    return templates.TemplateResponse("index.html", {"request": request})

@router.post("/predict", response_model=StockResponse)
async def predict_stock_price(stock_request: StockRequest):
    result = analyze_stock_prediction(stock_request.ticker)
    
    # Use the results returned from analyze_stock_prediction with proper field names
    return {
        "ticker": stock_request.ticker,
        "stock_name": result["stock_name"],
        "current_date": pd.Timestamp.now().strftime('%Y-%m-%d'),
        "last_updated_date": result["stock_data"].index[-1].strftime('%Y-%m-%d'),
        "current_price": float(result["current_price"]),
        "previous_close": float(result["previous_close"]),
        "daily_change_amount": float(result["daily_change_amount"]),
        "daily_change_percent": float(result["daily_change_percent"]),
        "predicted_price_tomorrow": float(result["predicted_price_tomorrow"]),
        "predicted_change_amount": float(result["predicted_change_amount"]),
        "predicted_change_percent": float(result["predicted_change_percent"]),
        "current_volume": float(result["current_volume"]),
        "average_volume_100d": float(result["average_volume_100d"]),
        "volume_ratio": float(result["volume_ratio"])
    }