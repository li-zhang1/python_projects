import os
import art
#HINT: You can call clear() to clear the output in the console.
print(art.logo)
def clear_console():
    os.system('clear')
#def clear_console(): return os.system('clear')
bid_info = {}
to_continue = True
while to_continue:
  name = input("What is your name?: ")
  bid =float(input("What's your bid?: $"))
  bid_info[name] = bid
  bidder = input("Are there any other bidders?(Type 'yes' or 'no'): ")
  clear_console()
  if bidder == 'yes':
    to_continue = True
  elif bidder == 'no':
    to_continue = False
  else:
      print("Invalid input")
      quit()

# Find the highest bid. this block of code can be included in a function.
largest_bid = -1
for name in bid_info:
  if bid_info[name] > largest_bid:
    winner_name = name
    largest_bid = bid_info[name]
print(f"The winner is {winner_name} with the bid of ${largest_bid}")

  