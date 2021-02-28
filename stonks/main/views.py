from django.shortcuts import render
from django.http import HttpResponse
from . import get_stocks
from . import scores
from .models import *
import stockquotes
import yfinance as yf

# Create your views here.


def index(request):
    return render(request, 'index.html')


def search(request):

    stock_name = request.POST['name']
    stocks = get_stocks.get_stock(stock_name)

    if(stocks == None):
        return render(request, 'search.html', {'stocks': stocks, 'stocks_found': False})

    print(len(stocks))

    return render(request, 'search.html', {'stocks': stocks, 'stocks_found': True})


def get_single_stock(request):

    name = request.POST['name']
    symbol = request.POST['symbol']
    country = request.POST['country']

    yfstock = yf.Ticker(symbol)
    history = yfstock.history(period='6d')

    print(name, symbol, country)

    stock_ = stock(name, symbol, history, country)

    print(type(history))

    result, future_price, current_price = scores.get_score(stock_)

    return render(request, 'single_stock.html', {'stock': stock_, 'result': result, 'future_price': future_price, 'cp': current_price})
