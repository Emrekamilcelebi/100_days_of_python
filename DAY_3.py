################IF ELSE#######################

# Condition Check
# Learn to use conditionals in Python to check a conditions and tell the computer what to do in each case. e.g.
# 
# if <this condition is true>:
# 
#     <then execute this line of code>
# 
# What if the condition is false?
# The else keyword is used to define a block of code that will execute if the condition checked in the if statement is false.
# 
# if pigs can fly:
# 
#     <Some code that will never execute>
# 
# else:
# 
#     print("This is real life")
# 
# Python Indentation
# Understand the importance of indentation in Python as a way to make certain lines of code subsidaries of other lines of code.
# 
# e.g.
# 
# if 5 > 2: #This is a parent line of code
# 
#     print("yes") #this is a child line of code
# 
# Comparator Operators
# > Greater than
# < Less than
# >= Greater than or equal to
# <= Less than or equal to
# == Equal to
# != Not equal to

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster")
else:
    print("Sorry you have to grow taller before you can ride")

############MODULO###############
#The modulo operator gives you the remainder of a division.
# 
# 6 % 2 #will be 0
# 
# 6 % 5 #will be 1
# 
# 6 % 4 #will be 2
# 
# PAUSE 1 - What is 10 % 3?
# What do you think this will output?
# 
# print(10 % 3)
# 
# PAUSE 2 - Check Odd or Even
# Write some code using what you have learnt about the modulo operator and conditional checks in Python to check if the number in he input area is odd or even. If it's odd print out the word "Odd" otherwise printout "Even".
#Even Number 12 % 2 == 0

print("Lutfen Bir Sayı Girin: ")

_Number = int(input())

even_or_odd = _Number % 2

if even_or_odd == 1:
    print(f"{_Number} TEK SAYIDIR")
else:
    print(f"{_Number} ÇİFT SAYIDIR")
  
###########NESTING AND ELIF###############

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("WHAT IS YOUR AGE? "))
    if age <= 12:
        print("Please pay 5$")
    elif age <= 18:
        print("PLEASE PAY 7$")
    elif age >= 50:
        print("FREE FOR OLD PEOPLE")
    else:
        print("PLEASE PAY 12$")
else:
    print("Sorry you have to grow taller before you can ride.")

################MULTIPLE IFS##############

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0
if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age <= 12:
        bill = 5
        print("Child tickets are $5.")
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7.")
    else:
        bill = 12
        print("Adılt tickets are $12.")

    want_photo = input("Do you want to have a photo take? type y for YES and n for NO.")
    if want_photo == "y":
        #Add $3 to their bill
        bill += 3

    print(f"your final bill is {bill}")
else:
    print("Sorry you have to grow taller before you can ride.")

##############PYTHON PIZZA#############################

print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
bill = 0
if size == "S":
    bill += 15
elif size == 'M':
    bill += 20
elif size == 'L':
    bill +=25
else:
    print("INVALID VALUE, YOU SHOULD TYPE S, M or L")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
if pepperoni == 'Y':
    if size == "S":
        bill += 2
    else:
        bill += 3
else:
    bill += 0
extra_cheese = input("Do you want extra cheese? Y or N: ")
if extra_cheese == "Y":
    bill += 1
else:
    bill += 0
print(f"Your final bill is: ${bill}.")

################## LOGICAL OPERATORS #############################

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age < 12:
        bill = 5
        print("Child tickets are $5.")
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7.")
    elif (age >= 45) or (age <= 55):
        bill = 0
        print("You dont have to pay money for ride.")
    else:
        bill = 12
        print("Adult tickets are $12.")

    wants_photo = input("Do you want a photo taken? Y or N. ")
    if wants_photo == "Y" or wants_photo =="y":
        bill += 3

    print(f"Your final bill is ${bill}")

else:
    print("Sorry, you have to grow taller before you can ride.")

################## TREASURE ISLAND PROJECT ###########################

from shutil import which

print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
left_or_right = input("So lets start! Which way you wanna go? Left or Right? type L for left, type R for right: ")
if left_or_right == "L" or left_or_right == "l":
    print("You... choosed the left way... Huh? Road is clear you are alive...")
    swim_or_wait = input("There is a river and you need to across the river. Do you wanna swim or wait? type S to swim, type W to wait. What is your choise: ")
    if swim_or_wait == 'W' or swim_or_wait == 'w':
        print("You prevented from a trout attack and there is a stone way revealed to across the river")
        which_door = input("There are 3 doors in front of you. One of them Red, one of them Blue and last one is Yellow. Type Red for R, Blue for B, Yellow for Y. What ise your choise?: ")
        if which_door == "Y" or which_door == "y":
            print("You Win!")
        elif which_door == "B":
            print("You have been eaten by beasts. Game Over")
        elif which_door == "R":
            print("You have burned by fire to death. Game Over")
        else:
            print("Game over")
    else:
        print("You have been attacked by trout")
else:
    print("You fall in to hole. Game Over.")
