import random
import sys #allows the user to clear terminal
from termcolor import colored #bringing color into game
import nltk
nltk.download('words')
from nltk.corpus import words #imprting library to assist with adding words
def print_menu():
  print("Let's play WORDLE!")
  print("Type a five letter word and hit ENTER!\n")
  #startup menu displays message^

def read_random_word():
  with open("words.text") as f:
    words = f.read().splitlines()
    return random.choice(words)
    #Defines word.text/reads random word/value from worrd.text array ^

nltk.data.path.append('/work/words')#location of list of words
word_list = words.words()#list of all words, even greater than five
words_five = [word for word in word_list if len(word)== 5]#reviews word list and stores any words that equals five letters into words.five
print_menu()
play_again = ""
while play_again != "q":
#Gives user option to play again vv
  #word = read_random_word()
  word = random.choice(words_five)#Produces random word
  #Pulls/select in random variiable from word.text array
  for attempt in range(1,7):
    guess = input().lower()
    #terminal will wait for user to input value on the console and store it in guess. .lower omits capitalization structure
    sys.stdout.write('\x1b[1A')
    sys.stdout.write('\x1b[2K')
    #This module provides access to some variables used or maintained by the interpreter and to functions that interact strongly with the interpreter.
  
    for i in range(min(len(guess), 5) ):  #controls the amount of letters entered
      if guess[i] == word[i]: 
        print(colored(guess[i], 'green'), end="")
      elif guess[i] in word:
        print(colored(guess[i], 'yellow'), end="")
      else:
        print(guess[i], end="")
    print()
  
      
    if guess == word:
        print(colored(f" Congrats! You got the wordle in {attempt}", 'red'))
        break
    elif attempt == 6:

      print(f"Sorry, the wordle was.. {word}")
  #controls if the input/output match
  
  play_again = input("Want to play again? Type q to exit")
  