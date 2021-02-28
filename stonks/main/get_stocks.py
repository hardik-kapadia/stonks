import models
import investpy
import yfinance as yf
import stockquotes
import twitter

# from yahoo_fin import stock_info as si

def get_current_stock_price(symbol):
    try:
        _stock_ = stockquotes.Stock(symbol)
        price = _stock_.current_price
    except:
        return 0
    return float(price)


def get_stock(stockname):
    stocks = []
    counter = int(0)
    try:
        search_results = investpy.search_quotes(
            text=stockname, products=['stocks'], n_results=2)
    except RuntimeError:
        print('no stocks found')
        return None
    for i in search_results:
        name = i.name
        symbol = i.symbol
        country = i.country
        yfstock = yf.Ticker(symbol)
        hist = yfstock.history(period='6d')
        
        # for i, row in hist.iterrows():
        #     print(str(i)[:10], row['Open'])

        _stock = models.stock(name, symbol, hist, country)
        stocks.append(_stock)
    return stocks

# get_stock('Tesla')