#PRINTING
# Write your code below this line 👇
print("Hello world!")

#STRING MANIPULATION
# Write your code below this line 👇
print("Hello" + " " + "Emre")

#INPUTS
name = input("Enter your name:")
print("Hello",name)

#Variables
name = "Angela"

print(type(name))
print(name)

print(len(input("Enter a name and find out how many letters in your name: ")))

username = input("What is your name:")
lenght = len(username)
print("There are",lenght,"Letters in your name")

# Variable Naming

#  Learn the rules of variable naming in Python.
#1 Make sure your variable names are descriptive
#2 Don't have spaces between words
#3 Don't start with numbers
#4 Don't use special words like print or input
#5 Choose simple words that are less likely to become typos
#6 Check the company style guidelines if you start work at a company

#Band Name Generator Project
#Create a greeting for your program.
#Ask the user for the city that they grew up in and store it in a variable.
#Ask the user for the name of a pet and store it in a variable.
#Combine the name of their city and pet and show them their band name.

print("Welcome to Band Name Generator Project Program!")
color = input("What is your favourite color?:")
animal = input("What is your favourite animal?:")
print("Your band name could be: " + color, animal)
