from trade_functions import *

class Order:
    def __init__(self, account, item, side, orderType, quantity, price=None):
        self.account = account
        self.item = item #what asset
        self.side = side #buy or sell
        self.orderType = orderType #market or limit
        self.quantity = quantity #how much
        self.price = price #what price
        self.filled = 0 #how much has been filled thus far
        self.lastPrice = None
        self.totalValue = 0
        self.quantityTraded = 0
    

class OrderMarket(Order):
   
    def place(self):

        if self.side == "buy":
            #sets the actual quantity to the total quantity of opposing bids/asks
            if self.quantity > self.item.returnTotalAskQuantity():
                self.quantity = self.item.returnTotalAskQuantity()
            for i in range(self.quantity):
                lowest_ask = self.item.returnLowestAsk()
                if self.item.returnAsks() == {}:
                    return
                self.item.addBid(lowest_ask, 1)
                self.account.addBidForAsset(self.item.name, lowest_ask, 1)
                price_executed = tradeFirst(self.item, self, self.account)
                
        elif self.side == "sell":
            if self.quantity > self.item.returnTotalBidQuantity():
                self.quantity = self.item.returnTotalBidQuantity()
            for i in range(self.quantity):
                highest_bid = self.item.returnHighestBid()
                if self.item.returnBids() == {}:
                    return
                self.item.addAsk(highest_bid, 1)
                self.account.addAskForAsset(self.item.name, highest_bid, 1)
                price_executed = tradeFirst(self.item, self, self.account)
                
    


class OrderLimit(Order):
    def place(self):
        if self.side == "buy":
            for i in range(self.quantity):
                self.item.addBid(self.price, 1)
                self.account.addBidForAsset(self.item.name, self.price, 1)
                #print("bid added for %s at $%s by %s" %(self.item.name, self.price, self.account.owner))
                price_executed = tradeFirst(self.item, self, self.account)
        elif self.side == "sell":
            for i in range(self.quantity):
                self.item.addAsk(self.price, 1)
                self.account.addAskForAsset(self.item.name, self.price, 1)
               # print("ask added for %s at $%s by %s" %(self.item.name, self.price, self.account.owner))
                price_executed = tradeFirst(self.item, self, self.account)


