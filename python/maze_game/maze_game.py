def start(): 
	print("Welcome to Fantasy Maze. I dare you to escape!")

	room0()

#description of the current room
#doors: dictionary with door: location sets

def process_user_movement(description, doors): 

	#Print description of the current room
	print(description)

	#Print available doors
	print("There are", len(doors), "doors:", *list(doors.keys()))

	#Prompt for what doors they want
	move = input("Which way would you like to go? \n")
	move = move.title()	

	#Do things based on their response
	#Valid response: Go to the correct location
	
	if move in doors:
		doors[move]()

	else:
		print("Please enter North, South, East or West")		
		process_user_movement(description, doors)
		#Invalid response: Ask them again

def room0():
	#description
	description = "You're in a tiny room. The walls are made of glass."
	#doors
	#where those doors go
	doors = {"South":room2, "East":room1}

	process_user_movement(description, doors)

def room1(): 
	description = "You're now in the library. There's a house elf sitting in an easy chair reading a thick old tome."

	doors = {"West":room0, "South":room3}

	process_user_movement(description, doors)


def room2(): 
	description = "You're in a large antechamber with a fire in the center."
	
	doors = {"North":room0, "South":room4, "East":room3}

	process_user_movement(description, doors)

def room3(): 
	description = "You're in a recording studio. There are several orcs belching out a rendition of 'Amazing Grace'."
	
	doors = {"North":room1, "West":room2}

	process_user_movement(description, doors)

def room4(): 
	description = "You're in a small cave. Three witches stand over a cauldron. When they see you they come rushing over."
	
	doors = {"North":room2, "South":exit}

	process_user_movement(description, doors)

def exit(): 
	print("You made it out alive! Congratulations!!")


start()

		

		




