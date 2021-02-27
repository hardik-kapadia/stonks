from django.db import models
from calc import factor as f
# Create your models here.


class stock:
    def __init__(self, name, symbol, current_price, history,country):
        self.name = name
        self.symbol = symbol
        self.current_price = current_price
        self.history = history
        self.words = [symbol,self.name.split(' ')[0]]
        self.country = country
