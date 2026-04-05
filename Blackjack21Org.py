import random
from blackjackart import logo

def deal_card():
 '''Returns a Random card from the Deck '''
 cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
 card=random.choice(cards)
 return card


def compare(user_score,computer_score):
 if user_score==computer_score:
  return "Draw 😶"
 elif computer_score==0:
  return "Lose, Opponent has BlackJack 😎"
 elif user_score ==0:
  return "Win with a BlackJack 🥳"
 elif user_score>21:
  return " You went over. You lose 😑"
 elif computer_score >21:
  return " Opponent Went over .You win 👌"
 elif user_score>computer_score:
  return "You Win ❤️"
 else:
  return "You lose 🧞"


def play_game():
 print(logo)
 user_card=[]
 computer_card=[]
 computer_score=-1
 user_score=-1
 is_game_Over=False
 
 def calculate_score(cards):
  ''' It will take a list of cards as input and tells the scores calculated from the cards'''
  if sum(cards)==21 and len(cards)==2:
   return 0
  if 11 in cards and sum(cards)>21:
   cards.remove(11)
   cards.append(1)
  return sum(cards)
 
 for _ in range(2):
  user_card.append(deal_card())
  computer_card.append(deal_card())
 
 while not is_game_Over:
  user_score=calculate_score(user_card)
  computer_score=calculate_score(computer_card)
  print(f"Your cards:{user_card},current score:{user_score}")
  print(f"Computer's First Card:{computer_card[0]}")
  
  if user_score==0 or computer_score==0 or user_score>21:
   is_game_Over=True
  
  else:
   user_should_deal=input("Type 'y' to get another card,type 'n' to pass : ")
   if user_should_deal =='y':
    user_card.append(deal_card())
   else:
    is_game_Over=True
 
 while computer_score !=0 and computer_score < 17:
  computer_card.append(deal_card())
  computer_score=calculate_score(computer_card)
 
 
 print(f" your final hand:{user_card},final score: {user_score}")
 print(f" Computer's final hand:{computer_card},final score: {computer_score}")
 
 print(compare(user_score,computer_score))

while input("Do ypu want to play a game of BalckJack? Type 'y' or 'n' :")=='y':
 print("\n"*20)
 play_game()



 