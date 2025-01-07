import yfinance as yf


def fetch_stock_data(ticker, period='1mo'):
    '''Получает исторические данные об акциях для указанного тикера и временного периода. Возвращает DataFrame с данными'''
    stock = yf.Ticker(ticker)
    data = stock.history(period=period)
    return data


def add_moving_average(data, window_size=5):
    '''Добавляет в DataFrame колонку со скользящим средним, рассчитанным на основе цен закрытия'''
    data['Moving_Average'] = data['Close'].rolling(window=window_size).mean()
    return data


def calculate_and_display_average_price(data):
    '''Вычисляет и выводит среднюю цену закрытия акций за заданный период'''
    average_price = data['Close'].mean(axis=0)
    print(f'Среднее значение колонки "Close": {average_price}')
    return data


def notify_if_strong_fluctuations(data, threshold):
    '''Анализирует данные и уведомляет пользователя, если цена акций колебалась более чем на заданный процент за период'''
    max_price = data['Close'].max()
    min_price = data['Close'].min()
    price_fluctuation = (max_price - min_price) / min_price * 100
    if price_fluctuation > threshold:
        return (f'***ВНИМАНИЕ***\n'
                f'Цена акций колебалась более чем на {threshold} % за выбранный период\n'
                f'Колебание составило: {price_fluctuation:.2f} %')
    else:
        return (f'Цена акций не колебалась более чем на {threshold} % за выбранный период\n')
