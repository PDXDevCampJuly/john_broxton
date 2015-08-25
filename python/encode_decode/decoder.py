#
#  
#	THE
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
      message.append(chr(int(each)))
    print(''.join(message))

def getSecret(fileName):

    with open(fileName, "r") as f:
      string = f.read()

    return string

main()










