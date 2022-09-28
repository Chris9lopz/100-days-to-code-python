# Create a function that allow Reborg jump the diferent obstacles using While Loop

# The wall will be random so you have to identify when you have to jump the obstacle

# use function wall_in_front() and front_is_clear()

# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%203&url=worlds%2Ftutorial_en%2Fhurdle3.json


def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump_obstacle():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
 
while not at_goal():
    if front_is_clear():
        move()
    elif wall_in_front():
        jump_obstacle()