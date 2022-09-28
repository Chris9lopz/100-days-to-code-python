# Create a function that allow Reborg jump the diferent obstacles using While Loop

# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%202&url=worlds%2Ftutorial_en%2Fhurdle2.json

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump_obstacle():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
 
while at_goal() == False:
    jump_obstacle()