import yfinance as yf
import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from tensorflow import keras
import tensorflow as tf
import os

from core.config import TIME_STEPS, MODEL_PATH, configure_gpu

# Configure GPU memory growth before loading any models
configure_gpu()
# Initialize scaler for data normalization
scaler = MinMaxScaler(feature_range=(0, 1))

# Create a simple LSTM model
def create_model():
    model = keras.Sequential([
        keras.layers.Input(shape=(TIME_STEPS, 1)),  # Explicit input layer
        keras.layers.LSTM(50, return_sequences=True),
        keras.layers.LSTM(50, return_sequences=False),
        keras.layers.Dense(25, activation='relu'),
        keras.layers.Dense(1)
    ])
    model.compile(optimizer='adam', loss='mse')
    return model

# Try to load the saved model, if it fails, create a new one
try:
    if os.path.exists(MODEL_PATH):
        try:
            model = create_model()  # Create model architecture first
            model.load_weights(MODEL_PATH)  # Then load weights
            print("✅ Saved model loaded successfully!")
        except Exception as e:
            print(f"⚠️ Could not load saved model: {e}")
            print("Creating new model instead...")
            model = create_model()
    else:
        print("⚠️ No saved model found. Creating new model...")
        model = create_model()
except Exception as e:
    print(f"⚠️ Error during model initialization: {e}")
    print("Creating basic model as fallback...")
    model = create_model()

def analyze_stock_prediction(ticker_symbol):
    """
    Display comprehensive analysis of stock data including current values,
    predicted values, and percentage changes.
    
    Args:
        ticker_symbol (str): Stock ticker symbol (e.g., 'AAPL', 'RELIANCE.NS')
        
    Returns:
        dict: A dictionary containing stock data and prediction results
    """
    # Get fresh data for the analysis
    stock_data = yf.download(ticker_symbol, period="90d", interval="1d", progress=False)
    stock_close = stock_data[['Close']]
    
    # Try to get stock name/info
    stock_name = None
    try:
        ticker_obj = yf.Ticker(ticker_symbol)
        stock_info = ticker_obj.info
        if 'shortName' in stock_info:
            stock_name = stock_info['shortName']
        elif 'longName' in stock_info:
            stock_name = stock_info['longName']
    except:
        pass
    
    # Current stock information
    current_price = stock_close.iloc[-1, 0]
    previous_price = stock_close.iloc[-2, 0]
    daily_change = current_price - previous_price
    daily_change_pct = (daily_change / previous_price) * 100
    
    # Fit the scaler using the current data
    scaler.fit(stock_close)
    
    # Generate prediction
    scaled_data = scaler.transform(stock_close)
    
    # Make sure we have enough data points for the time_steps
    if len(scaled_data) < TIME_STEPS:
        raise ValueError(f"Not enough data points. Need at least {TIME_STEPS} days of data.")
        
    x_input = np.array([scaled_data[-TIME_STEPS:]])
    x_input = x_input.reshape((x_input.shape[0], x_input.shape[1], 1))
    
    # Make prediction
    predicted_price = model.predict(x_input, verbose=0)
    predicted_price_tomorrow = scaler.inverse_transform(predicted_price.reshape(-1, 1))[0][0]
    
    # Calculate predicted change
    predicted_change = predicted_price_tomorrow - current_price
    predicted_change_pct = (predicted_change / current_price) * 100
    
    # Additional stock info
    avg_volume = 0
    current_volume = 0 
    volume_ratio = 0
    
    if 'Volume' in stock_data.columns:
        # Extract scalar values from pandas Series objects and convert to native Python types
        avg_volume = float(stock_data['Volume'].mean())
        current_volume = float(stock_data['Volume'].iloc[-1])
        volume_ratio = float(current_volume / avg_volume)  # Explicitly convert to float
    
    # Return results with clear naming
    return {
        "stock_data": stock_data,
        "stock_name": stock_name,
        "current_price": current_price,
        "previous_close": previous_price,
        "daily_change_amount": daily_change,
        "daily_change_percent": daily_change_pct,
        "predicted_price_tomorrow": predicted_price_tomorrow,
        "predicted_change_amount": predicted_change,
        "predicted_change_percent": predicted_change_pct,
        "current_volume": current_volume,
        "average_volume_100d": avg_volume,
        "volume_ratio": volume_ratio
    }