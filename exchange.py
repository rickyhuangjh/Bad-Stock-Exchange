import random
from dict_functions import *
from order_class import *
from asset_class import *
import os

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)



#print(bids[-1])
#print(asks[0])


#takes in an item and executes the first valid trade

        

#trade(bids, asks)


    


    

book = Asset("book")
laptop = Asset("laptop")



ricky = Account("Ricky", 1000)
john = Account("John", 1000)
henry = Account("Henry", 1000)

limit1 = OrderLimit(ricky, book, "sell", "limit", 100, 4)
limit2 = OrderLimit(john, book, "sell", "limit", 100, 4)
limit3 = OrderMarket(henry, book, "buy", "market", 100)

limit4 = OrderLimit(ricky, laptop, "sell", "limit", 100, 4)
limit5 = OrderLimit(john, laptop, "sell", "limit", 100, 4)
limit6 = OrderMarket(henry, laptop, "buy", "market", 100)

sell_order_list = []
buy_order_list = []

def coinFlip():
    result = random.randint(0, 1)
    return result

def main():
    while True:

        sell_order_list.append(OrderLimit(ricky, book, "sell", "limit", 1, random.randint(0, 10000)/100))
        sell_order_list.pop(0).place()
        buy_order_list.append(OrderLimit(john, book, "buy", "limit", 1, random.randint(0, 10000)/100))
        buy_order_list.pop(0).place()

clearConsole()
print()
main()