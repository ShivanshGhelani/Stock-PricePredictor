import os
import sys

# Add the current directory to the Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Configure GPU at startup - This now imports TensorFlow for us
from core.config import configure_gpu
tf = configure_gpu()

# Now it's safe to import other modules that may initialize TensorFlow
import matplotlib.pyplot as plt
import seaborn as sns
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
import uvicorn

# Import routes
from routes.stockprediction import router

# Initialize the app
app = FastAPI(title="Stock Price Predictor")

# Mount static files if needed
if os.path.exists("static"):
    app.mount("/static", StaticFiles(directory="static"), name="static")

# Include routers
app.include_router(router)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=5000, log_level="info", reload=True)