import os
from art import logo

print(logo)
welcome_message = ("Welcome to the Secret Auction!")
print(welcome_message)

secretAuctionBids = {}

def theSecretAuction():
    moreParticipants = True
    while moreParticipants:
        name = input("Your name is: ")
        bid = int(input("Your bid is: $"))
        moreBidders = input("Are there any more bidders? Type 'yes' or 'no': ")
        os.system('clear')

        secretAuctionBids[name] = bid

        if moreBidders == "no":
            moreParticipants = False
    
    list_of_bids = []
    for participant in secretAuctionBids:
        list_of_bids.append(secretAuctionBids[participant])

    highest_bid = max(list_of_bids)
    highest_bidder = list(secretAuctionBids.keys())[list(secretAuctionBids.values()).index(highest_bid)]

    print(f'The highest bid is {highest_bidder} with a bid of ${highest_bid}')

theSecretAuction()
