#dice program
from random import randint

def roll(max):
	r = randint(1, max)
	print(r)

def roll_many(max, numOfDice=5): 
	for i in range(numOfDice): 
		roll(max) 