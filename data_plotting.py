import matplotlib.pyplot as plt
import plotly.graph_objects as go
import matplotlib.style
import pandas as pd
from data_download import calculate_std


def create_and_save_plot(data, ticker, period, style='default', filename=None):
    plt.figure(figsize=(10, 6))
    # graphic style
    plt.style.use(style)

    if 'Date' not in data:
        if pd.api.types.is_datetime64_any_dtype(data.index):
            dates = data.index.to_numpy()
            plt.plot(dates, data['Close'].values, label='Close Price')
            plt.plot(dates, data['Moving_Average'].values, label='Moving Average')
            std = calculate_std(data)
            plt.fill_between(dates, data['Close'] - std, data['Close'] + std, color='lightgrey', label='Standard Deviation')
        else:
            print("Информация о дате отсутствует или не имеет распознаваемого формата.")
            return
    else:
        if not pd.api.types.is_datetime64_any_dtype(data['Date']):
            data['Date'] = pd.to_datetime(data['Date'])
        plt.plot(data['Date'], data['Close'], label='Close Price')
        plt.plot(data['Date'], data['Moving_Average'], label='Moving Average')
        std = calculate_std(data)
        plt.fill_between(data['Date'], data['Close'] - std, data['Close'] + std, color='lightgrey', label='Standard Deviation')


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


def create_interactive_chart(data, ticker, col_list=None):
    '''Создание интерактивного графика цен'''
    fig = go.Figure()
    if not col_list:
        fig.add_trace(go.Scatter(x=data.index, y=data['Open'], mode='lines', name='Цена открытия'))
        fig.add_trace(go.Scatter(x=data.index, y=data['Close'], mode='lines', name='Цена закрытия'))
        fig.add_trace(go.Scatter(x=data.index, y=data['High'], mode='lines', name='Максимальная цена'))
        fig.add_trace(go.Scatter(x=data.index, y=data['Low'], mode='lines', name='Минимальная цена'))
        fig.update_layout(title=f"{ticker} График цен",
                          xaxis_title="Date", yaxis_title="Price", showlegend=True)
    else:
        for i in col_list:
            fig.add_trace(go.Scatter(x=data.index, y=data[i], mode='lines', name=i))
        fig.update_layout(title=f"{ticker} График по выбранным столбцам",
                          xaxis_title="Date", showlegend=True)
    fig.show()


def create_interactive_rsi(data, ticker, col_list=None):
    '''Создание интерактивного графика индекса RSI'''
    fig = go.Figure()
    if not col_list:
        fig.add_trace(go.Scatter(x=data.index, y=data['RSI'], mode='lines', name='RSI'))
        fig.update_layout(title=f"{ticker} RSI",
                          xaxis_title="Date", yaxis_title="RSI", showlegend=True)
    else:
        for i in col_list:
            fig.add_trace(go.Scatter(x=data.index, y=data[i], mode='lines', name=i))
        fig.update_layout(title=f"{ticker} График RSI",
                          xaxis_title="Date", showlegend=True)
    fig.show()
