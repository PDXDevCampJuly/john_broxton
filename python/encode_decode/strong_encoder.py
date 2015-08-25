from sys import argv
from random import randint

def main(message = None):
	if message == None: 
		message = input("Enter a message to be encoded. >>> ")
	
	secret = transform(message)

	makeSecretFile(secret)

#Transform the message using an algorithm

def transform(message):

	#transform message into ordinals

	secret = ''
	num1 = randint(0, 100)
	num2 = randint(0, 100)

	for each in message:
		secret += str(len(str(ord(each)))) + str(num1) + str(ord(each)) + str(num2) + " "

		

	return secret

#Output an encoded text file 

def makeSecretFile(secret):
	with open('secret.txt', 'w') as f:
		f.write(secret)

main()