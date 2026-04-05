import random
computer_Guess=random.randint(1,100)
print(computer_Guess)
print("Welcome to the Number Guessing Game!")
print("I'm Thinking of a Number between 1 and 100")
Game_mode=input("Choose a difficulty. Type 'easy' or 'hard':")
if Game_mode=='easy':
    game_life=10
elif Game_mode=='hard':
    game_life=5
else:
    print("chose Valid mode")

def keep_Guessing(user_choice):
    if  user_choice> computer_Guess:
        return f"You are on Higher Side"
    elif computer_Guess>user_choice:
        return f"You are on Lower side"
    else:
        return f"You Won"
    
continue_Gueesing=True
lives=game_life
   
while continue_Gueesing:
    print(f"You have {lives} attempts remaining to guess the number.")
    user_guess=int(input("Make a Guess:"))
    result=keep_Guessing(user_guess)
    print(result)
    lives-=1
    if lives<1 or result =="You Won":
        if lives==0:
         print("You've run out of guesses.")
        continue_Gueesing= False
        break
    else:
        print("Guess Again")

    

    
   

  
  



    


