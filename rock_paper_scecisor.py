import random




option=["rock","paper","scissors"]
computer_choice=random.choice(option)
user_choice=input("Enter your choice (rock, paper, scissors): ").lower()

if (computer_choice=="rock" and user_choice=="scissors") or (computer_choice=="scissors" and user_choice=="paper") or (computer_choice== "paper" and user_choice=="rock") :
    print("I won you Lose")
elif  (user_choice=="rock" and computer_choice=="scissors") or (user_choice=="scissors" and computer_choice=="paper") or (user_choice== "paper" and computer_choice=="rock"):
    print( " You won")
else:
 print(" Draw")




