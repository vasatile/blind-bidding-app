from replit import clear
#HINT: You can call clear() to clear the output in the console.
from art import logo
print(logo)
new_bid = True
bids = {}


def highest_bidder(bidrecord):
  highest_bid = 0
  winner = ""
  for  bidder in bids:
    bidamount = bidrecord[bidder]
    if bidamount > highest_bid:
      highest_bid = bidamount
      winner = bidder
  print(f"the winner is {winner} and won with ${highest_bid}")
while new_bid:
  bidder_name = input("what your name ?\n").lower()
  bid = int(input("what your bidding price ?\n"))
  bids[bidder_name] = bid
  new_user = input("any other bidder? Yes or No\n").lower()
  clear()

  if new_user == "no":
    new_bid = False
    highest_bidder(bids)
    
