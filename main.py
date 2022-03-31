from replit import clear
#HINT: You can call clear() to clear the output in the console.
from art import logo
print(logo)
print('Welcome to Online Auction.')
bids={}

def highest(record):
  highest_bid=0
  winner=''
  for i in record:
    amnt=record[i]
    if amnt>highest_bid:
      highest_bid=amnt
      winner=i
  print(f'The winner is {winner} with a bid of highest bid {highest_bid} .')


finish=False
while not finish:
  name = input('What is your name? ')
  bid = int(input('What is your bid? '))
  bids[name] = bid
  g=input('Are there any other biders? YES or NO.').lower()
  if g=='no':
    finish=True
    highest(bids)
  elif g=='yes':
    finish=False
    clear()


      
    
  

