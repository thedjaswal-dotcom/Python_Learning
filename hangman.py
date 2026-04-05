import random
from hangmanArt import stages ,logo
from wordlist import word_list
lives=6
print(logo)
choosen_word=random.choice(word_list).lower()
placeholder=""
print("choosen_word\n")
word_length=len(choosen_word)
for i in range(word_length):
   placeholder+="_"   
print("Word to guess:",placeholder)

correct_guess=[]
game_over=False

while not game_over:
  print(f"********************{lives}Lives left******************************* ")
  guess_word=input("Guess the word:\n").lower()
  if guess_word in correct_guess:
     print(f" You have already guessed the letter:{guess_word}")
  display=""
  for letter in choosen_word:
     if letter == guess_word:
         display += letter
         correct_guess.append(guess_word)             
     elif letter in correct_guess:
        display += letter
     else:
         display+="_"
  print(display)

  if guess_word not in choosen_word:
     lives-=1
     print(f" You have guessed a wrong letter {guess_word},you loose a life.")
     if lives ==0:
        game_over=True

        print(f"************************It was {choosen_word},You Loose*************************")
 
  if "_" not in display:
     print(" You win")
     game_over=True
  print(stages[lives])
 

 



     

