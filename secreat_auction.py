auction_details={}
bids=[]
max_bid=0
more_bidders="yes"
while more_bidders=="yes":
    Name=input("What is your name? ")
    Bid=int(input("What is your bid? $"))
    auction_details[Name]=Bid
    more_bidders=input("Are there any other bidders? Type 'yes' or 'no'. ")  
    print("\n" *1000)       

for name,bidding_amount in auction_details.items():
     if max_bid<bidding_amount:
          max_bid=bidding_amount
          max_bid_name=name
          
     
print(f"Auction Won by {max_bid_name},with bidding Amount of {max_bid}")

