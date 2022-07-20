from account_class import *
import random

def checkAndFill(item, order, account):
    failed = False
    highest_bid = item.returnHighestBid()
    lowest_ask = item.returnLowestAsk()
    buyer = None
    seller = None
    if highest_bid == None or lowest_ask == None:
        return None
    if not highest_bid >= lowest_ask:
        return None
    if not item.returnBids()[highest_bid] > 0 and item.returnAsks()[lowest_ask] > 0:
        return None
    if failed:
        print("%s: no trade available" %item.name.upper())
        return None
    price_executed = (item.fillHighestBid() + item.fillLowestAsk())/2

    

    if order.side == "buy":
        buyer = account
        askers_at_price = returnListOfPotentialSellers(item.name, lowest_ask)
        seller = random.choice(askers_at_price)
        seller.subtractAskForAsset(item.name, lowest_ask, 1)
        account.subtractBidForAsset(item.name, highest_bid, 1)
    
    elif order.side == "sell":
        seller = account
        bidders_at_price = returnListOfPotentialBuyers(item.name, highest_bid)
        buyer = random.choice(bidders_at_price)
        buyer.subtractBidForAsset(item.name, highest_bid, 1)
        account.subtractAskForAsset(item.name, lowest_ask, 1)

    print("%s %s trade executed at price: $%s (%s %s)" %(item.name.upper(), order.orderType, price_executed, highest_bid, lowest_ask))
    order.quantityTraded += 1
    order.totalValue += price_executed



    buyer.cashTransfer(-price_executed)
    buyer.assetTransfer(item, 1)
    seller.cashTransfer(price_executed)
    seller.assetTransfer(item, -1)
    return price_executed

def tradeAll(item, order, account):
    price_executed = tradeFirst(item, order, account)
    if price_executed == None:
        return
    tradeAll(item, order, account)

def tradeFirst(item, order, account):

    price_executed = checkAndFill(item, order, account)
    return price_executed

def addBuyOrder(item, orderType, price=None):
    highest_bid = item.returnHighestBid()
    lowest_ask = item.returnLowestAsk()
    if orderType == "limit":
        item.addBid(price)
    elif orderType == "market":
        price = lowest_ask
        item.addBid(price)
    
def addSellOrder(item, orderType, price=None):
    highest_bid = item.returnHighestBid()
    lowest_ask = item.returnLowestAsk()
    if orderType == "limit":
        item.addAsk(price)
    elif orderType == "market":
        price = highest_bid
        item.addAsk(price)