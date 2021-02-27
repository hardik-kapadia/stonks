from django.db import models
# Create your models here.
class stock:
    def __init__(self,name,symbol,current_price,history):
        self.name = name 
        self.symbol = symbol
        self.current_price = current_price
        self.history = history
