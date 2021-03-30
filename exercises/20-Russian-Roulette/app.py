import random

bullet_position = 3

def spin_chamber():
	chamber_position = random.randint(1,6)
	return chamber_position

#  DON'T CHANGE THE CODE ABOVE
def fire_gun():
	# YOUR CODE HERE
    camara = spin_chamber()
    if camara == bullet_position:
        return "You are dead!"
    else:
        return "Keep playing!"  


print(fire_gun())