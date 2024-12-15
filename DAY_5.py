################FOR LOOPS###############
fruits = ["Apple", "Peach", "Pear"]

for fruit in fruits:
    print(fruit[-1])
    print(fruit + " pie")
    print(fruits)

############### HIGHEST SCORE ############

student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]
print(range(1, 10))

total_exam_score = sum(student_scores)
print(total_exam_score)

sum = 0

for score in student_scores:
    sum += score

print(sum)

## The function for finding biggest number in the list. max()
maximum_list = 0
for maximum1 in student_scores:
    if maximum1 > maximum_list:
        maximum_list = maximum1
print(maximum_list)

######################### FOR LOOPS WITH RANGE ##################################
#Range function with For Loop

# 3'er 3'er belirlenen sayiya kadar yazdiriyor
# for number in range(0, 101, 3):
#     print(number)


# asd = 0
# for number in range(0,101):
#     asd += number
# print(asd)

#FizzBuzz Game!
a = 0
b = 0
for number in range(1,101):
    a = number % 3
    b = number % 5
    if a == 0 and b == 0:
        print("FizzBuzz")
    elif b == 0:
        print("Buzz")
    elif a == 0 :
        print("Fizz")
    else:
        print(number)

############################PASSWORD GENERATOR PROJECT####################################

import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

##EASY LEVEL##

# password = ""
#
# for char in range(0, nr_letters):
#     password += random.choice(letters)
#
# for char in range(0, nr_symbols):
#     password  += random.choice(symbols)
#
# for char in range(0, nr_numbers):
#     password += random.choice(numbers)
#
# print(password)

### HARD LEVEL ### ALL RANDOM ####

password = []
rnd_pass = ""
for char in range(0, nr_letters):
    password.append(random.choice(letters))

for char in range(0, nr_symbols):
    password.append(random.choice(symbols))

for char in range(0, nr_numbers):
    password.append(random.choice(numbers))

print(password)
rnd_pas_n = len(password)

for char in range(0, rnd_pas_n):
    rnd_pass += random.choice(password)

print(rnd_pass)




