import yfinance as yf
import pandas as pd
import os

def fetch_yfinance_data(ticker, start_date, end_date):
    """
    Fetch historical stock data using YFinance.
    """
    data = yf.download(ticker, start=start_date, end=end_date)
    data.reset_index(inplace=True)
    return data

def save_data_to_csv(data, filename):
    """
    Save the cleaned DataFrame to CSV.
    """
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    data.to_csv(filename, index=False)

def preprocess_data(file_path):
    """
    Load data from CSV, clean, and preprocess.
    """
    df = pd.read_csv(file_path, parse_dates=['Date'])
    df.drop_duplicates(inplace=True)
    df.set_index('Date', inplace=True)
    
    # Handle missing values by interpolation
    df.interpolate(method='linear', inplace=True)
    return df

if __name__ == "__main__":
    # Define tickers and date range
    tickers = ['TSLA', 'BND', 'SPY']
    start_date = '2015-01-01'
    end_date = '2024-10-31'
    
    # Fetch and save raw data
    for ticker in tickers:
        raw_data = fetch_yfinance_data(ticker, start_date, end_date)
        raw_data_path = f'C:/Users/MMM/Documents/10 Academy File/KAIM-Week-11/data/raw/{ticker}.csv'
        save_data_to_csv(raw_data, raw_data_path)
        print(f"Raw data for {ticker} saved successfully at {raw_data_path}!")

    # Preprocess and save cleaned data
    for ticker in tickers:
        raw_data_path = f'C:/Users/MMM/Documents/10 Academy File/KAIM-Week-11/data/raw/{ticker}.csv'
        processed_data = preprocess_data(raw_data_path)
        processed_data_path = f'C:/Users/MMM/Documents/10 Academy File/KAIM-Week-11/data/processed/{ticker}_cleaned.csv'
        save_data_to_csv(processed_data, processed_data_path)
        print(f"Cleaned data for {ticker} saved successfully at {processed_data_path}!")
