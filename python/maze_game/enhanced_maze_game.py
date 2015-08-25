unlock = False

def start(): 
	print("Welcome to the Maze.")

	room0()

#description of the current room
#doors: dictionary with door: location sets

def process_user_movement(description, doors): 

	#Print description of the current room
	print(description)

	#Print available doors
	print("There are", len(doors), "doors:", *list(doors.keys()))

	#Prompt for what doors they want
	move = input("You can move through a door by entering North, South, East or West.\nOr, you can search the room by entering Search.\nWhat would you like to do? >>> ")
	move = move.title()	

	#Do things based on their response
	#Valid response: Go to the correct location
	
	if move in doors:
		doors[move]()
			
	else:
		print("Please enter North, South, East or West, or Search the room.")

		process_user_movement(description, doors)
		#Invalid response: Ask them again

def room0():
	#description
	description = "You're in a tiny room. The walls are made of glass."
	#doors
	#where those doors go
	doors = {"South":room2, "East":room1, "Search":empty1}

	process_user_movement(description, doors)

def room1(): 
	description = "You're now in the library. There's a house elf sitting in an easy chair reading a thick old tome."

	doors = {"West":room0, "South":room3, "Search":key}

	process_user_movement(description, doors)


def room2(): 
	description = "You're in a large antechamber with a fire in the center."
	
	doors = {"North":room0, "South":room4, "East":room3, "Search":empty2}

	process_user_movement(description, doors)

def room3(): 
	description = "You're in a recording studio. There are several orcs belching out a rendition of 'Amazing Grace'."
	
	doors = {"North":room1, "West":room2}

	process_user_movement(description, doors)

def room4(): 
	description = "You're in a small cave. Three witches stand over a cauldron. When they see you they come rushing over."
	
	doors = {"North":room2, "South":exit}

	process_user_movement(description, doors)

def empty1(): 
	
	print("There is nothing in this room of value.")

	room0()

def empty2():

	print("There is nothing in this room of value.")

	room2()

def empty3():

	print("There is nothing in this room of value.")

	room3()

def empty4():

	print("There is nothing in this room of value.")

	room4()

def empty5():

	print("There is nothing in this room of value.")

	room5()
	




def key(): 
	global unlock
	
	pick_it_up = input("There is a key on the floor. Would you like to pick it up? Y or N >>> ")
	pick_it_up = pick_it_up.upper()

	if pick_it_up == 'Y':
		unlock = True
	else: 
		unlock = False


	room1()





def exit():
 	if unlock == True: 
 		print("You made it out alive! Congratulations!!")
 	else: 
 		print("You didn't find the key! Go back and find it!!")
 		room4()
 		


start()

		

		




