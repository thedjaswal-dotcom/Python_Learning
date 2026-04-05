import random
cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]

user_card=[]
system_card=[]

def pick_random(picked_card):
 picked_card=[]
 for i in range(2):
    random_index=random.randint(0,12)
    picked_card.append(cards[random_index])
 return picked_card

def sum_of_picked_card(pc):
  sum=0
  for i in pc:
    sum+=i
  return sum

GameOn=True
while GameOn:
 user_input=input("want to play the game ,type 'y' or 'n':")
 if user_input=='y':
      user_pick=pick_random(user_card)
      system_card=pick_random(system_card)
      print(f"Your Cards are: {user_pick}")
      print(f"Dealera's one of Card is : {system_card[0]}")
      first_2_card_sum=sum_of_picked_card(user_pick)
      dealers_2card_sum=sum_of_picked_card(system_card)
      first_2_card_sum=21
      if first_2_card_sum==21:
        print(f"you won ,your cards are {user_pick} =>{first_2_card_sum} and dealer's card are {system_card}=>{dealers_2card_sum}")
        GameOn=False       
      user_next_choice=input("type 'hit' to pick one more card  or type 'show' to close the game:")
      if user_next_choice=='hit':
       random_index=random.randint(0,12)
       user_pick.append(cards[random_index])
       if 11 in user_pick and sum_of_picked_card(user_pick)>21:
         print(f"Debug statment 11 in the userPick and sum is {sum_of_picked_card(user_pick)}")
         index_of_11=user_pick.index(11)
         user_pick[index_of_11]=1
         print(user_pick)

      user_card_sum=sum_of_picked_card(user_pick)
      dealer_card_sum=sum_of_picked_card(system_card)
      
      if user_card_sum>dealer_card_sum or dealer_card_sum>21 or user_card_sum<=21  :
       print(f"you won ,your cards are {user_pick} =>{user_card_sum} and dealer's card are {system_card}=>{dealer_card_sum}")
      
      else :
        print(f"you loose, your cards are {user_pick} =>{user_card_sum} and dealer's card are {system_card}=>{dealer_card_sum}")     
 else:
  GameOn=False 
 
 
   
    
 
 








  















