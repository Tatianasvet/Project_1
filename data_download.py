import yfinance as yf
import pandas as pd


def fetch_stock_data(ticker, period='1mo', start=None, end=None):
    '''Получает исторические данные об акциях для указанного тикера и временного периода. Возвращает DataFrame с данными'''
    data = yf.Ticker(ticker).history(start=start, end=end, period=period)
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
        return f'Цена акций не колебалась более чем на {threshold} % за выбранный период\n'


def export_data_to_csv(data, filename):
    """Принимает DataFrame и имя файла и сохраняет данные об акциях в указанный файл"""
    df = pd.DataFrame(data)
    df.to_csv(filename, index=False)
    print(f'Данные сохранены в файле {filename}')


def calculate_rsi(data, window_size=5):
    """Расчет индекса RSI"""
    delta = data['Close'].diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=window_size).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=window_size).mean()
    rs = gain / loss
    rsi = 100 - (100 / (1 + rs))
    data['RSI'] = rsi
    return rsi

def calculate_macd(data):
    """Расчет индекса MACD"""

    # Получить 26-дневную EMA цены закрытия
    k = data['Close'].ewm(span=12, adjust=False, min_periods=12).mean()
    # Получить 12-дневную EMA цены закрытия
    d = data['Close'].ewm(span=26, adjust=False, min_periods=26).mean()
    # Вычтите 26-дневную EMA из 12-дневной EMA, чтобы получить MACD
    macd = k - d
    # Получите 9-дневную экспоненциальную скользящую среднюю MACD для линии триггера
    macd_s = macd.ewm(span=9, adjust=False, min_periods=9).mean()
    # Рассчитайте разницу между MACD — триггером для значения конвергенции/дивергенции
    macd_h = macd - macd_s
    # Добавьте все наши новые значения для MACD во фрейм данных
    data['macd'] = data.index.map(macd)
    data['macd_h'] = data.index.map(macd_h)
    data['macd_s'] = data.index.map(macd_s)
    # Просмотр наших данных
    pd.set_option("display.max_columns", None)

