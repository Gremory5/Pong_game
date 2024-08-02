from replit import clear
#HINT: You can call clear() to clear the output in the console.

from art import logo
print(logo)

bids = {}
def find_highest_bidder():
  bidder_name = input(print(f"What is your name?"))
  bid_amount = input(print(f"What is your bid?"))
  bids[bidder_name] = bid_amount
  print(bids)

  