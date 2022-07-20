from dict_functions import *
from asset_class import *

list_of_accounts = []

class Account:
    def __init__(self, owner, startBalance):
        self.owner = owner
        self.balance = startBalance
        self.bids = {}
        self.asks = {}
        self.holdings = {}
        for x in list_of_assets:
            self.holdings.update({x: 0})
        list_of_accounts.append(self)
    
    def addBidForAsset(self, item_name, price, quantity):
        if item_name not in self.bids.keys():
            self.bids.update({item_name: {}})
        if price not in self.bids[item_name]:
            self.bids[item_name].update({price: 0})
        self.bids[item_name][price] += quantity
    
    def subtractBidForAsset(self, item_name, price, quantity):
        self.bids[item_name][price] -= quantity

    def addAskForAsset(self, item_name, price, quantity):
        if item_name not in self.asks.keys():
            self.asks.update({item_name: {}})
        if price not in self.asks[item_name]:
            self.asks[item_name].update({price: 0})
        self.asks[item_name][price] += quantity
    
    def subtractAskForAsset(self, item_name, price, quantity):
        self.asks[item_name][price] -= quantity
    
    def returnAsks(self):
        return self.asks.copy()
    
    def returnBids(self):
        return self.bids.copy()
    
    
    def cashTransfer(self, amount):
        self.balance += amount
    
    def assetTransfer(self, item, quantity):
        self.holdings[item] += quantity
    
    def returnBalance(self):
        return self.balance
    
    def returnHoldings(self):
        return self.holdings

def returnListOfPotentialBuyers(item_name, price):
    list_of_bidders = []
    for i in range(len(list_of_accounts)):
        if item_name not in list_of_accounts[i].returnBids():
            continue
        if price not in list_of_accounts[i].returnBids()[item_name]:
            continue
        if not list_of_accounts[i].returnBids()[item_name][price] > 0:
            continue
        #print("add bid", list_of_accounts[i].returnBids())
        list_of_bidders.append(list_of_accounts[i])
    return list_of_bidders

def returnListOfPotentialSellers(item_name, price):
    list_of_askers = []
    for i in range(len(list_of_accounts)):
        if item_name not in list_of_accounts[i].returnAsks():
            continue
        if price not in list_of_accounts[i].returnAsks()[item_name]:
            continue
        if not list_of_accounts[i].returnAsks()[item_name][price] > 0:
            continue
        #print("add ask", list_of_accounts[i].returnAsks())
        list_of_askers.append(list_of_accounts[i])
    return list_of_askers