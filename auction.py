from replit import clear

from art import logo
print(logo)
bidderlist = {}
clearTheScreen = False
def findHighest(biddingFile):
    bids = 0
    winner = ""
    for bidder in biddingFile:

        pricebid = biddingFile[bidder]
        if pricebid > bids:
            bids = pricebid
            winner = bidder
    print(f"the winner is {winner} with the bid of {bids} ")
while not clearTheScreen:
    name = input("Please input your name \n")
    bid = int(input("please input your biding price: \n$"))
    bidderlist[name] = bid
    otherBidders = input("do we have any other bidders answer with 'yes' or 'no' \n")
    if otherBidders == 'no':
        clearTheScreen = True
        findHighest(bidderlist) 
    elif otherBidders == 'yes':
        clear()
        

