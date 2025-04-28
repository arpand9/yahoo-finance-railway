from fastapi import FastAPI
import yfinance as yf

app = FastAPI()

@app.get("/stock/{ticker}")
def get_stock_price(ticker: str):
    stock = yf.Ticker(ticker)
    data = stock.history(period="1d")
    if data.empty:
        return {"error": "Ticker not found or no data available."}
    latest_price = data['Close'].iloc[-1]
    return {
        "ticker": ticker,
        "latest_close_price": latest_price
    }
