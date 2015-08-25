#hangman.py
# A program about hanging people if you don't spell things correctly.
import random
from random import randint

words = ["test"]
numWrong = 0
letters = [None]

# A function that starts and plays the hangperson game.
# Users can be wrong a maximum of 5 times before they lose,
# the 6th wrong guess triggering Game Over.
def hangperson():

   global letters

   # Greet the user
   print("Let's play a game of hangperson!")

   # Randomly select a word from the list of words

   playWord = random.choice(words)

   # Make the randomly selected word into a list object

   letters = list(playWord)

   # Make another list the same length as the word, but with
   # '_' instead of letters. This will track the user's progress.
   # Use the variable name currentState

   var = len(letters)

   currentState = list(var * "_")

   #currentState is now a list of "_"

   # Print the initial state of the game

   printHangperson(currentState)

   # Start the game! Loop until the user either wins or loses

   while currentState != letters and numWrong < 6:
   	
   	guess = userGuess()

   	currentState = updateState(guess, currentState)

   	printHangperson(currentState)

   # Determine if the user won or lost, and then tell them accordingly

   if currentState == letters: 
   	print("You lived! I wasn't expecting that! Not that I ever doubted you, but seriously, I'm impressed!")

   else: 
   	print("A+ for effort! Nevertheless, you failed. Don't take it too hard!\n This can't be the first time you've lost in your life\n and certainly won't be the last!")

# This helpful function prompts the user for a guess,
# accepting only single letters.
#
# returns a letter

def userGuess():
	guess = ""
	while not guess:
		guess = input("Guess a letter in the word! (Say 'exit' to stop playing) ")
#	while len(guess) != 1:

		if guess == "exit":
			exit()

		elif len(guess) > 1:
			print("Please guess one letter at a time!")
			guess = ""

		elif len(guess) == 0:
			print("Please enter a letter.")
			guess = ""

	return guess


# Update the state of the game based on the user's guess.
#
# guess: a character guessed by the user
# currentState: the current state of the word/game
#
# return currentState
def updateState(guess, currentState):
   global numWrong

   # First, determine if the letter guessed is in the word.

   # If it isn't, tell the user and update the numWrong var

   # If it is, congratulate them and update the state of the game.
   
   #    To update the state, make sure to replace ALL the '_' with
   #    the guessed letter.
   
   numInWord = letters.count(guess)

   for index, char in enumerate(letters): 
   	if char == guess: 
   		currentState[index] = guess

   if numInWord > 0:
   	print("Congrats! That letter is in the word.")

   else:
   	print("That letter is not the word.") 

   	numWrong += 1

   return currentState

   print(currentState)

   

# A helpful function to print the hangman.
# DO NOT CHANGE
#
# state: current state of the word
def printHangperson(state):
   person = [" O "," | \n | ", "\| \n | ", "\|/\n | ", "\|/\n | \n/  ", "\|/\n | \n/ \\"]
   print()

   if numWrong > 0:
      print(person[0])

   if numWrong > 1:
      print(person[numWrong-1])

   print("\n\n")

   for i in state:
      print(i, end=" ")

   print("\n")

# This line runs the program on import of the module

hangperson()
