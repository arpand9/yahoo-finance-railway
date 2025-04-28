from fastapi import FastAPI, HTTPException, Query
from typing import List, Optional
import yfinance as yf

app = FastAPI(
    title="Stock Market API",
    description="Fetch stock prices, historical data, company info, dividends, splits, and recommendations using yFinance.",
    version="1.0.0"
)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Stock Market API. Visit /docs for API documentation."}

@app.get("/stock/{ticker}")
def get_stock_price(ticker: str):
    stock = yf.Ticker(ticker)
    data = stock.history(period="1d")
    if data.empty:
        raise HTTPException(status_code=404, detail=f"No data found for ticker '{ticker}'.")
    latest_price = data['Close'].iloc[-1]
    return {"ticker": ticker, "price": float(latest_price)}

@app.get("/stocks")
def get_multiple_stock_prices(tickers: str = Query(..., description="Comma-separated stock tickers, e.g., AAPL,MSFT,GOOGL")):
    tickers_list = [ticker.strip() for ticker in tickers.split(",")]
    results = {}
    for ticker in tickers_list:
        stock = yf.Ticker(ticker)
        data = stock.history(period="1d")
        if not data.empty:
            results[ticker] = float(data['Close'].iloc[-1])
        else:
            results[ticker] = "No Data"
    return results

@app.get("/history/{ticker}")
def get_historical_data(ticker: str, period: str = "7d"):
    stock = yf.Ticker(ticker)
    data = stock.history(period=period)
    if data.empty:
        raise HTTPException(status_code=404, detail=f"No historical data found for ticker '{ticker}' and period '{period}'.")
    history = [{"date": idx.strftime("%Y-%m-%d"), "close": float(row['Close'])} for idx, row in data.iterrows()]
    return {"ticker": ticker, "history": history}

@app.get("/info/{ticker}")
def get_company_info(ticker: str):
    stock = yf.Ticker(ticker)
    info = stock.info
    if not info:
        raise HTTPException(status_code=404, detail=f"No company info found for ticker '{ticker}'.")
    return {
        "ticker": ticker,
        "name": info.get("longName"),
        "sector": info.get("sector"),
        "industry": info.get("industry"),
        "marketCap": info.get("marketCap"),
        "peRatio": info.get("trailingPE")
    }

@app.get("/dividends/{ticker}")
def get_dividends(ticker: str):
    stock = yf.Ticker(ticker)
    dividends = stock.dividends
    if dividends.empty:
        raise HTTPException(status_code=404, detail=f"No dividend history found for ticker '{ticker}'.")
    dividends_list = [{"date": idx.strftime("%Y-%m-%d"), "amount": float(amount)} for idx, amount in dividends.items()]
    return {"ticker": ticker, "dividends": dividends_list}

@app.get("/splits/{ticker}")
def get_splits(ticker: str):
    stock = yf.Ticker(ticker)
    splits = stock.splits
    if splits.empty:
        raise HTTPException(status_code=404, detail=f"No stock split history found for ticker '{ticker}'.")
    splits_list = [{"date": idx.strftime("%Y-%m-%d"), "ratio": str(ratio)} for idx, ratio in splits.items()]
    return {"ticker": ticker, "splits": splits_list}

@app.get("/recommendations/{ticker}")
def get_recommendations(ticker: str):
    stock = yf.Ticker(ticker)
    recs = stock.recommendations
    if recs is None or recs.empty:
        raise HTTPException(status_code=404, detail=f"No recommendations found for ticker '{ticker}'.")
    recommendations_list = []
    recs = recs.tail(5)  # Last 5 recommendations
    for idx, row in recs.iterrows():
        recommendations_list.append({
            "date": idx.strftime("%Y-%m-%d"),
            "firm": row.get("Firm"),
            "to_grade": row.get("To Grade"),
            "from_grade": row.get("From Grade"),
            "action": row.get("Action")
        })
    return {"ticker": ticker, "recommendations": recommendations_list}
