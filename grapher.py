# File: grapher.py

import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime


def fetch_financial_data(tickers, start_year, end_year, interval="1wk"):
    """
    Fetch historical financial data for the given tickers.

    Args:
        tickers (list of str): List of financial instruments (tickers) to fetch.
        start_year (int): Start year for data retrieval.
        end_year (int): End year for data retrieval.
        interval (str): Data interval ('1d', '1wk', '1mo', '1y').

    Returns:
        dict: Dictionary of DataFrames, one per ticker.
    """
    start_date = f"{start_year}-01-01"
    end_date = f"{end_year}-12-31"
    data = {}

    for ticker in tickers:
        print(f"Fetching data for {ticker}...")
        try:
            df = yf.download(ticker, start=start_date, end=end_date, interval=interval)
            if not df.empty:
                df["Year"] = df.index.year
                yearly_data = df.groupby("Year").mean()
                data[ticker] = yearly_data
        except Exception as e:
            print(f"Failed to fetch data for {ticker}: {e}")

    return data


def plot_financial_data(data, title, ylabel):
    """
    Plot financial data from the fetched data.

    Args:
        data (dict): Dictionary of DataFrames containing financial data.
        title (str): Title for the graph.
        ylabel (str): Label for the Y-axis.
    """
    plt.figure(figsize=(10, 6))

    for ticker, df in data.items():
        if "Close" in df.columns:
            plt.plot(df.index, df["Close"], label=ticker)

    plt.title(title)
    plt.xlabel("Year")
    plt.ylabel(ylabel)
    plt.legend()
    plt.grid()
    plt.show()


def main():
    # Example usage
    tickers = ["GC=F", "SI=F", "PL=F"]  # Gold, Silver, Platinum futures
    start_year = 2000
    end_year = 2023
    data = fetch_financial_data(tickers, start_year, end_year)
    plot_financial_data(data, "Precious Metal Prices (2000-2023)", "Price (USD)")


if __name__ == "__main__":
    main()
