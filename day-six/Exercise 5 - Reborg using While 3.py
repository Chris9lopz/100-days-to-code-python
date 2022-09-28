# Create a function that allow Reborg jump the diferent obstacles using While Loop

# The wall will be random so you have to identify when you have to jump the obstacle

# The size of each obstacle will change

# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%204&url=worlds%2Ftutorial_en%2Fhurdle4.json

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def top_obstacle():
    turn_right()
    move()
    turn_right()
    move()
  
while not at_goal():
    if wall_on_right() and not wall_in_front():
        move()
    elif not wall_on_right() and not wall_in_front():
        top_obstacle()
    elif wall_in_front() and not wall_on_right():
        top_obstacle()
    elif wall_in_front():
        turn_left()