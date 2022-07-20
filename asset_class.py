from dict_functions import *

list_of_assets = []

class Asset:
    def __init__(self, name):
        self.name = name
        self.bids = {}
        self.asks = {}
        list_of_assets.append(self)
    
    def addBid(self, price, quantity):
        self.bids = insertSortedDict(self.bids, price, quantity)
    
    def returnBids(self):
        return self.bids.copy()
    
    def returnHighestBid(self):
        return(dictLastKey(self.bids))

    def fillHighestBid(self):
        highest_bid = self.returnHighestBid()
        self.bids[highest_bid] -= 1
        if self.bids[highest_bid] <= 0:
            self.bids.pop(highest_bid)
        return highest_bid
    
    def returnTotalBidQuantity(self):
        total = 0
        for value in self.returnBids().values():
            total += value
        return total
    



    
    def addAsk(self, price, quantity):
        self.asks = insertSortedDict(self.asks, price, quantity)
    
    def returnAsks(self):
        return self.asks.copy()
    
    def returnLowestAsk(self):
        return(dictFirstKey(self.asks))
    
    def fillLowestAsk(self):
        lowest_ask = self.returnLowestAsk()
        self.asks[lowest_ask] -= 1
        if self.asks[lowest_ask] <= 0:
            self.asks.pop(lowest_ask)
        return lowest_ask
    
    def returnTotalAskQuantity(self):
        total = 0
        for value in self.returnAsks().values():
            total += value
        return total