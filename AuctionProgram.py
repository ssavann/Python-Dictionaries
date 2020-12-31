#Build Auction program

from AuctionArt import logo


print(logo)

#make an empty dictionary
bids = {}

#initiate the loop to "false"
bidding_finished = False



#Second step: a function to compare values in dictionary and find winner
def find_highest_bidder(bidding_record):

    highest_bid = 0

    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder

    print(f"The winner is {winner} with a bid of ${highest_bid}")



#First step: a Loop to get user input and to store in dictionary 
while not bidding_finished:
    name = input("What is your name? ")
    price = int(input("What's your bid? $"))
    bids[name] = price

    should_continue = input("Are there any other bidders? Type 'yes' or 'no'.\n ").lower()
    
    if should_continue == 'no':
        bidding_finished = True
        find_highest_bidder(bids)   #Third Step: call the function if finished
    
    else:
        bidding_finished = False




