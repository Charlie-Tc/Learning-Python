import yfinance as yf


'MODULO YFINACE'
# Permite a los desarrolladores a obtener información sobre acciones, indices, divisas, bonos y otros instrumentos finacieros.

# Metodos
# 1.- download(ticker, start=None, end=None, period="1d", interval="1d", group_by='ticker', auto_adjust=True, prepost=False, threads=True,
# proxy=None, rounding=True): Descarga datos históricos de precios de un instrumento financiero específico (como una acción) desde Yahoo Finance.
# Puedes especificar el rango de fechas, el período, el intervalo de tiempo, entre otros parámetros.
def dowload():
    # Descargar datos históricos de Apple desde 2020-01-01 hasta 2021-12-31
    data = yf.download("AAPL", start="2020-01-01", end="2023-09-2")
    print(data)

# 2.- Ticker(ticker): Crea un objeto Ticker que permite acceder a información detallada sobre un instrumento financiero específico.
def ticker():
    # Crear un objeto Ticker para Apple (AAPL)
    apple = yf.Ticker("AAPL")

    # Obtener información sobre la empresa
    info = apple.info
    for i in info.items():
        print(i)

# 3.- Métodos:
    # Ticker.info(): Devuelve información fundamental acerca del activo en cuestión en forma de diccionario {key:value} 1.
    # Ticker.history(): Devuelve el historial de precios del activo en cuestión 1.
    # Ticker.dividends(): Devuelve el historial de dividendos del activo en cuestión 1.
    # Options.option_chain(): Devuelve la cadena de opciones para el activo en cuestión 2.
    # Options.expirations(): Devuelve las fechas de vencimiento disponibles para las opciones del activo en cuestión 2.

# Atributos:
    # Ticker.info: Contiene información fundamental acerca del activo en cuestión en forma de diccionario {key:value} 1.
    # Ticker.history: Contiene el historial de precios del activo en cuestión 1.
    # Ticker.dividends: Contiene el historial de dividendos del activo en cuestión 1.

# Parámetros:
    # period: Especifica el período para el que se desea obtener datos históricos (por ejemplo: 1d, 5d, 1mo) 1.
    # interval: Especifica el intervalo temporal para el que se desea obtener datos históricos (por ejemplo: 1m, 2m, 5m) 1.
    # start y end: Especifican la fecha inicial y final para la que se desea obtener datos históricos 1.
    # Espero que esto te ayude. Si necesitas más información, no dudes en preguntar.


msft = yf.Ticker("MSFT")

history = msft.history(period="1mo", proxy="PROXY_SERVER")
msft.get_actions()