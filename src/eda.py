import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels.tsa.seasonal import seasonal_decompose
import os

# Set plotting style
plt.style.use('seaborn-v0_8-darkgrid')


def plot_closing_price(df, ticker):
    """
    Plot the closing price over time.
    """
    plt.figure(figsize=(12, 6))
    plt.plot(df['Close'], label=f'{ticker} Closing Price', color='blue')
    plt.title(f'{ticker} Closing Price Over Time')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend()
    plt.grid(True)
    plt.show()

def plot_daily_returns(df, ticker):
    """
    Plot daily percentage returns as a histogram with KDE.
    """
    df['Daily Return'] = df['Close'].pct_change()
    
    # Check if Daily Return column has values to avoid empty plots
    if df['Daily Return'].dropna().empty:
        print(f"No daily return data available for {ticker}")
        return

    plt.figure(figsize=(10, 5))
    sns.histplot(df['Daily Return'].dropna(), bins=50, kde=True, color='purple')
    plt.title(f'{ticker} Daily Returns Distribution')
    plt.xlabel('Daily Return')
    plt.ylabel('Frequency')
    plt.grid(True)
    plt.show()

def decompose_time_series(df, ticker):
    """
    Decompose the time series into trend, seasonality, and residuals.
    """
    try:
        decomposition = seasonal_decompose(df['Close'], model='multiplicative', period=365)
        decomposition.plot()
        plt.suptitle(f'{ticker} Time Series Decomposition')
        plt.show()
    except ValueError as e:
        print(f"Could not decompose {ticker} data: {e}")

def load_and_process_data(ticker):
    """
    Load cleaned data from CSV and preprocess if needed.
    """
    file_path = f'C:/Users/MMM/Documents/10 Academy File/KAIM-Week-11/data/processed/{ticker}_cleaned.csv'
    
    if not os.path.exists(file_path):
        print(f"Data file for {ticker} not found at {file_path}. Skipping...")
        return None

    # Load the CSV data
    df = pd.read_csv(file_path, parse_dates=['Date'], index_col='Date')

    # Ensure that the 'Close' column is present
    if 'Close' not in df.columns:
        print(f"'Close' column missing in {ticker} data. Skipping...")
        return None

    return df

if __name__ == "__main__":
    tickers = ['TSLA', 'BND', 'SPY']
    
    for ticker in tickers:
        print(f"\nPerforming EDA for {ticker}...")
        df = load_and_process_data(ticker)
        
        if df is not None:
            plot_closing_price(df, ticker)
            plot_daily_returns(df, ticker)
            decompose_time_series(df, ticker)
        else:
            print(f"Skipping EDA for {ticker} due to data issues.")
