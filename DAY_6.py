%80 of the day6 is complated only 2 challanges left

def my_function():
    print("Hello")
    print("Bye")



my_function()

############reebog.ca ###############
def turn_around():
    turn_left()
    turn_left()

def turn_right():
    turn_left()
    turn_left()
    turn_left()

#DRAW SQUARE
turn_left()
move()
turn_right()
move()
turn_right()
move()
turn_right()
move()

################### DAY 6 REEBORG HURDLE 1 #####################
def turn_r():
    turn_left()
    turn_left()
    turn_left()


def jump():
    move()
    turn_left()
    move()
    turn_r()
    move()
    turn_r()
    move()
    Turn_left()

for asd in range(6):


######################## DAY 6 REEBORG HURDLE 2 #################################

def turn_r():
    turn_left()
    turn_left()
    turn_left()


def jump():
    move()
    turn_left()
    move()
    turn_r()
    move()
    turn_r()
    move()
    turn_left()


while True:
    jump()
    if at_goal() == True:
        break

######################## DAY 6 REEBORG HURDLE 3 #################################
def turn_r():
    turn_left()
    turn_left()
    turn_left()

def jump():
    turn_left()
    move()
    turn_r()
    move()
    turn_r()
    move()
    turn_left()


while True:
    if wall_in_front() == False:
        move()
    else:
        jump()
    if at_goal() == True:
        break

