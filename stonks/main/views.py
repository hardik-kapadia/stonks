from django.shortcuts import render
from django.http import HttpResponse
from . import get_stocks
from .models import *
import stockquotes

# Create your views here.


def index(request):
    # if(request.method == 'POST'):
    #     stock_name = request.POST['name']

    #     stocks = get_stocks.get_stock(stock_name)

    #     for stock in stocks:
    #         print(stock.name)
    #     return HttpResponse("<h1> HEllo there </h1>")
    # else:
    return render(request, 'index.html')


def search(request):

    stock_name = request.POST['name']
    stocks = get_stocks.get_stock(stock_name)

    if(stocks == None):
        return render(request, 'search.html', {'stocks': stocks, 'stocks_found': False})

    return render(request, 'search.html', {'stocks': stocks, 'stocks_found': True})


def get_single_stock(request):
    name = request.POST['name']
    symbol = request.POST['symbol']
    history = request.POST['history']
    country = request.POST['country']

    _stock = stock(name, symbol, history, country)

    print('Stock selected:', end=' ')
    print(_stock.name, ' goes by ', _stock.symbol, ' in ', _stock.country)
    print('History:')
    print(history)

    price = get_stocks.get_current_stock_price(symbol)

    return HttpResponse('<h1> General Kenobi </h1>')
