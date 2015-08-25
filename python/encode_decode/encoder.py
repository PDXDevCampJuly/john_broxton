#                
#                ***** The ******
# ,------.                        ,--.               
#|  .---',--,--,  ,---. ,---.  ,-|  | ,---. ,--.--. 
#|  `--, |      \| .--'| .-. |' .-. || .-. :|  .--' 
#|  `---.|  ||  |\ `--.' '-' '\ `-' |\   --.|  |    
#`------'`--''--' `---' `---'  `---'  `----'`--'  
#
# The Encoder program takes a message, encodes it, and returns a string. 
########################################################################

#Prompt the user for a message

def main(message = None):
	if message == None: 
		message = input("Enter a message to be encoded. >>> ")
	
	secret = transform(message)

	makeSecretFile(secret)

#Transform the message using an algorithm

def transform(message):

	#transform message into ordinals

	secret = ''

	for each in message:
		secret += random.randint(0, 100) + str(ord(each)) + " "

		len(str(ord(each)))

	return secret

#Output an encoded text file 

def makeSecretFile(secret):
	with open('secret.txt', 'w') as f:
		f.write(secret)

main()