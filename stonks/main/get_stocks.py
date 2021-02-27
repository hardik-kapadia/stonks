import models
import investpy
import yfinance as yf
from yahoo_fin import stock_info as si

def get_stock(stockname):
    stocks = []
    counter = int(0)
    search_results = investpy.search_quotes(text=stockname,products=['stocks'],n_results=10)
    for i in search_results:
        name = i.name
        symbol = i.symbol
        country = i.country
        yfstock = yf.Ticker(symbol)
        hist = yfstock.history(period = '7d')
        try:
            current = si.get_live_price(symbol)
        except AssertionError:
            current = 0
        except:
            continue
        _stock = models.stock(name,symbol,current,hist,country)
        stocks.append(_stock)
    return stocks

ss = get_stock('Reliance')

for s in ss:
    print(s.name)
    print(s.words)
