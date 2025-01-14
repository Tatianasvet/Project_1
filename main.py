import data_download as dd
import data_plotting as dplt


def main():
    print("Добро пожаловать в инструмент получения и построения графиков биржевых данных.")
    print("Вот несколько примеров биржевых тикеров, которые вы можете рассмотреть: AAPL (Apple Inc), GOOGL (Alphabet Inc), MSFT (Microsoft Corporation), AMZN (Amazon.com Inc), TSLA (Tesla Inc).")
    print("Общие периоды времени для данных о запасах включают: 1д, 5д, 1мес, 3мес, 6мес, 1г, 2г, 5г, 10л, с начала года, макс.")

    ticker = input("Введите тикер акции (например, «AAPL» для Apple Inc):»")
    period = input("Введите период для данных (например, '1mo' для одного месяца): ")

    # Fetch stock data
    stock_data = dd.fetch_stock_data(ticker, period)

    # Add moving average to the data
    stock_data = dd.add_moving_average(stock_data)

    # Calculate RSI
    dd.calculate_rsi(stock_data)

    # Calculate MACD
    dd.calculate_macd(stock_data)

    # Plot the data
    dplt.create_and_save_plot(stock_data, ticker, period)

    dd.calculate_and_display_average_price(stock_data)

    threshold = float(input('Введите значение порога колебания цены, при котором следует уведомлять пользователя: '))
    message = dd.notify_if_strong_fluctuations(stock_data, threshold)
    if message:
        print(message)

    # Принимает DataFrame и имя файла и сохраняет данные об акциях в указанный файл.
    dd.export_data_to_csv(stock_data, filename=f"{ticker}_{period}_stock_price_chart.csv")


if __name__ == "__main__":
    main()
