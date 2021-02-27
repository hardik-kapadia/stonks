from . import models
import investpy
import yfinance as yf
import stockquotes

# from yahoo_fin import stock_info as si


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

        # apple = stockquotes.Stock('AAPL')
        # price = apple.current_price


        # try:
        #     current = si.get_live_price(symbol)
        # except AssertionError:
        #     current = 0
        # except:
        #     continue
        
        _stock = models.stock(name, symbol, hist, country)
        stocks.append(_stock)
    return stocks

