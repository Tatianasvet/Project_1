Описание функций:

data_download.py: 


- fetch_stock_data(ticker, period): 
Получает исторические данные об акциях для указанного тикера и временного периода. Возвращает DataFrame с данными.

- add_moving_average(data, window_size): 
добавляет в DataFrame колонку со скользящим средним, рассчитанным на основе цен закрытия.

- calculate_and_display_average_price(data): 
вычисляет и выводит среднюю цену закрытия акций за заданный период

С*реднее значение колонки "Close": 250.04875106811522*

- notify_if_strong_fluctuations(data, threshold): 
анализирует данные и уведомляет пользователя, если цена акций колебалась более чем на заданный процент за период.

_Введите значение порога колебания цены, при котором следует уведомлять пользователя: 5
***ВНИМАНИЕ***
Цена акций колебалась более чем на 5.0 % за выбранный период
Колебание составило: 6.43 %_


main.py:

- main(): Основная функция, управляющая процессом загрузки, обработки данных и их визуализации. 
запрашивает у пользователя ввод данных, вызывает функции загрузки и обработки данных, а затем передаёт результаты 
на визуализацию.


data_plotting.py:

- create_and_save_plot(data, ticker, period, filename): Создаёт график, отображающий цены закрытия и скользящие средние. 
предоставляет возможность сохранения графика в файл. Параметр filename опционален; если он не указан, имя файла 
генерируется автоматически.