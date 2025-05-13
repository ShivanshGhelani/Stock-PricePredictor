# Stock Price Predictor

A FastAPI-based web application that demonstrates stock price prediction using LSTM deep learning models. This project is intended for educational purposes only and should not be used for real financial decisions.

## ⚠️ Important Disclaimer

**THIS IS AN ACADEMIC PROJECT AND SHOULD NOT BE USED FOR REAL TRADING OR FINANCIAL DECISIONS**

- This application is created purely for educational and demonstration purposes
- The predictions are NOT financial advice
- The model's accuracy is limited and not suitable for real-world trading
- Past performance does not indicate future results
- Always consult with qualified financial advisors for investment decisions
- The developers are not responsible for any financial losses incurred from using this tool

## Features
- Stock price prediction using LSTM (Long Short-Term Memory) neural networks
- Interactive web interface with real-time visualizations
- RESTful API endpoints for programmatic access
- Historical data analysis and trend visualization
- Pre-trained models included for demonstration
- Support for multiple stock symbols via Yahoo Finance API

## Tech Stack
- **Backend**: FastAPI, Python 3.9+
- **Machine Learning**: TensorFlow, Keras, Scikit-learn
- **Data Processing**: Pandas, NumPy, yfinance
- **Frontend**: HTML5, Bootstrap CSS
- **Visualization**: Matplotlib, Seaborn
- **Development**: Jupyter Notebooks for model training

## Project Structure
```
├── main.py              # FastAPI application entry point
├── core/               # Core application logic
│   ├── config.py       # Configuration settings
│   ├── models.py       # Data models and schemas
│   └── prediction.py   # Prediction logic
├── models/             # Trained models and datasets
│   ├── final_lstm_model.h5
│   └── all_stocks_5yr.csv
├── routes/             # API route handlers
│   └── stockprediction.py
├── templates/          # HTML templates
│   └── index.html
└── notebooks/          # Jupyter notebooks for model development
    ├── MakeModel.ipynb
    └── TestModel.ipynb
```

## Model Architecture
- LSTM neural network with multiple layers
- Input: 90 days of historical price data
- Hidden layers: 2 LSTM layers (50 units each)
- Dropout layers for regularization
- Dense output layer for price prediction
- Trained on historical stock data from multiple companies

## Setup and Installation

1. Clone the repository:
```bash
git clone <your-repo-url>
cd StockPricePredictor
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the application:
```bash
uvicorn main:app --host 0.0.0.0 --port 8000
```

## API Documentation
- Interactive API documentation available at `/docs`
- Swagger UI documentation at `/redoc`
- Main endpoints:
  - `GET /`: Web interface
  - `POST /predict`: Get stock price predictions

## Model Limitations
- Predictions are based solely on historical price data
- Does not account for:
  - Company fundamentals
  - Market sentiment
  - Economic indicators
  - News and external events
  - Market manipulation
  - Global economic conditions

## Contributing
This is an educational project and contributions are welcome. Please ensure:
1. Code follows PEP 8 style guide
2. Add appropriate tests
3. Update documentation
4. Maintain the educational focus

## License
MIT License. See LICENSE file for details.

## Acknowledgments
- Data provided by Yahoo Finance API
- LSTM implementation inspired by TensorFlow tutorials
- UI components from Bootstrap

## Contact
For academic and educational inquiries only. Not for financial advice or consulting.
