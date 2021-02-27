from django.shortcuts import render
from django.http import HttpResponse
from . import get_stocks

# Create your views here.


def index(request):
    if(request.method == 'POST'):
        stock_name = request.POST['name']

        stocks = get_stocks.get_stock(stock_name)

        for stock in stocks:
            print(stock.name)
        return HttpResponse("<h1> HEllo there </h1>")
    else:
        return render(request, 'index.html')


'''
def search(request):

    stock_name = request.GET['name']

    stocks = get_stocks.get_stock(stock_name)

    for stock in stocks:
        print(stock.name)

    # return render(request, 'search.html')
'''
