from django.shortcuts import render
from django.http import HttpResponse
from . import get_stocks
from .models import *
import stockquotes

# Create your views here.


def index(request):
    return render(request, 'index.html')


def search(request):

    stock_name = request.POST['name']
    stocks = get_stocks.get_stock(stock_name)

    if(stocks == None):
        return render(request, 'search.html', {'stocks': stocks, 'stocks_found': False})

    return render(request, 'search.html', {'stocks': stocks, 'stocks_found': True})


def get_single_stock(request):
    return render(request, 'single_stock.html')
