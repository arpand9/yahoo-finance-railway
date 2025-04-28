# 📈 yFinance Stock API on Railway

This template deploys a simple FastAPI application that uses [yfinance](https://github.com/ranaroussi/yfinance) to fetch real-time stock data from Yahoo Finance.

## 🚀 How to Deploy

Click the button below to deploy to Railway:

[![Deploy on Railway](https://railway.app/button.svg)](https://railway.app/new/template?templateUrl=https://github.com/YOUR-USERNAME/yfinance-api-template)

# 📈 Stock Market API (powered by yFinance)

A simple, fast, production-ready Stock API built with FastAPI and yFinance,  
fetching real-time stock prices, historical data, dividends, splits, and more!

---

## 🚀 Features
- Get the latest stock price
- Fetch multiple stock prices at once
- Retrieve historical stock data (1d, 7d, 1mo, 6mo, 1y, etc.)
- Company financial info (market cap, sector, industry, P/E ratio)
- Dividend payment history
- Stock split history
- Analyst recommendations
- Interactive API docs powered by Swagger at `/docs`

---

## 🛠️ Technologies Used
- FastAPI
- Uvicorn
- yFinance
- Pydantic

---

## 🧩 API Endpoints

| Method | Endpoint | Description |
|:------|:---------|:------------|
| `GET` | `/` | Welcome message. |
| `GET` | `/docs` | Swagger UI for API exploration. |
| `GET` | `/stock/{ticker}` | Get the latest stock price for a single ticker. |
| `GET` | `/stocks?tickers=AAPL,MSFT` | Get the latest prices for multiple tickers. |
| `GET` | `/history/{ticker}?period=7d` | Get historical price data for a stock. |
| `GET` | `/info/{ticker}` | Fetch company info (sector, industry, market cap, etc.). |
| `GET` | `/dividends/{ticker}` | Fetch dividend history of a stock. |
| `GET` | `/splits/{ticker}` | Fetch stock split history. |
| `GET` | `/recommendations/{ticker}` | Fetch analyst recommendations. |

---
