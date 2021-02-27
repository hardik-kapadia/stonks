from . import models
import investpy
import yfinance as yf
import stockquotes

# from yahoo_fin import stock_info as si


def get_current_stock_price():
    try:
        _stock_ = stockquotes.Stock('AAPL')
        price = _stock_.current_price
    except:
        return 0
    print(type(price))
    return float(price)


def get_stock(stockname):
    stocks = []
    counter = int(0)
    search_results = investpy.search_quotes(
        text=stockname, products=['stocks'], n_results=10)
    for i in search_results:
        name = i.name
        symbol = i.symbol
        country = i.country
        yfstock = yf.Ticker(symbol)
        hist = yfstock.history(period='7d')

        _stock = models.stock(name, symbol, hist, country)
        stocks.append(_stock)
    return stocks
