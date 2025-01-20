import matplotlib.pyplot as plt
import matplotlib.style
import pandas as pd


def create_and_save_plot(data, ticker, period, style='default', filename=None):
    plt.figure(figsize=(10, 6))
    # graphic style
    plt.style.use(style)

    if 'Date' not in data:
        if pd.api.types.is_datetime64_any_dtype(data.index):
            dates = data.index.to_numpy()
            plt.plot(dates, data['Close'].values, label='Close Price')
            plt.plot(dates, data['Moving_Average'].values, label='Moving Average')
        else:
            print("Информация о дате отсутствует или не имеет распознаваемого формата.")
            return
    else:
        if not pd.api.types.is_datetime64_any_dtype(data['Date']):
            data['Date'] = pd.to_datetime(data['Date'])
        plt.plot(data['Date'], data['Close'], label='Close Price')
        plt.plot(data['Date'], data['Moving_Average'], label='Moving Average')


    plt.title(f"{ticker} Цена акций с течением времени")
    plt.xlabel("Дата")
    plt.ylabel("Цена")
    plt.legend()

    if filename is None:
        filename = f"{ticker}_{period}_stock_price_chart.png"
    plt.savefig(filename)
    print(f"График сохранен как {filename}")

    create_rsi_plot(data, ticker, period)


def create_rsi_plot(data, ticker, period):
    plt.figure(figsize=(10, 6))
    if 'Date' not in data:
        if pd.api.types.is_datetime64_any_dtype(data.index):
            dates = data.index.to_numpy()
            plt.plot(dates, data['RSI'], label='RSI')
    else:
        if not pd.api.types.is_datetime64_any_dtype(data['Date']):
            data['Date'] = pd.to_datetime(data['Date'])
        plt.plot(data['Date'], data['RSI'], label='RSI')
    plt.title(f"{ticker} RSI с течением времени")
    plt.xlabel("Дата")
    plt.ylabel("RSI")
    plt.legend()

    filename = f"{ticker}_{period}_RSI.png"
    plt.savefig(filename)
    print(f"График RSI сохранен как {filename}")

    create_macd_plot(data, ticker, period)


def create_macd_plot(data, ticker, period):
    plt.figure(figsize=(10, 6))
    if 'Date' not in data:
        if pd.api.types.is_datetime64_any_dtype(data.index):
            dates = data.index.to_numpy()
            plt.plot(dates, data['macd'], label='macd')
            plt.plot(dates, data['macd_h'], label='macd_h')
            plt.plot(dates, data['macd_s'], label='macd_s')
    else:
        if not pd.api.types.is_datetime64_any_dtype(data['Date']):
            data['Date'] = pd.to_datetime(data['Date'])
        plt.plot(data['Date'], data['macd'], label='macd')
        plt.plot(data['Date'], data['macd_h'], label='macd_h')
        plt.plot(data['Date'], data['macd_s'], label='macd_s')
    plt.title(f"{ticker} MACD с течением времени")
    plt.xlabel("Дата")
    plt.ylabel("MACD")
    plt.legend()

    filename = f"{ticker}_{period}_MACD.png"
    plt.savefig(filename)
    print(f"График MACD сохранен как {filename}")