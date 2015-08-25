#
#  
#	THE ***STRONG***
#
#	████████▄     ▄████████  ▄████████  ▄██████▄  ████████▄     ▄████████    ▄████████ 
#	███   ▀███   ███    ███ ███    ███ ███    ███ ███   ▀███   ███    ███   ███    ███ 
#	███    ███   ███    █▀  ███    █▀  ███    ███ ███    ███   ███    █▀    ███    ███ 
#	███    ███  ▄███▄▄▄     ███        ███    ███ ███    ███  ▄███▄▄▄      ▄███▄▄▄▄██▀ 
#	███    ███ ▀▀███▀▀▀     ███        ███    ███ ███    ███ ▀▀███▀▀▀     ▀▀███▀▀▀▀▀   
#	███    ███   ███    █▄  ███    █▄  ███    ███ ███    ███   ███    █▄  ▀███████████ 
#	███   ▄███   ███    ███ ███    ███ ███    ███ ███   ▄███   ███    ███   ███    ███ 
#	████████▀    ██████████ ████████▀   ▀██████▀  ████████▀    ██████████   ███    ███ 
#	                                                                        ███    ███ 
#   The Decoder takes a message, decodes it, and returns a file.
#
#
######################################################################################


def main(fileName = "secret.txt"):

	string = getSecret(fileName)

	detransform(string)

def detransform(string):

    message = []
    string = string.split()
    for each in string:
    	n = int(each[0])
    	message.append(chr(int(each[3:3+n])))
    print(''.join(message))

def getSecret(fileName):

    with open(fileName, "r") as f:
      string = f.read()

    return string

main()










