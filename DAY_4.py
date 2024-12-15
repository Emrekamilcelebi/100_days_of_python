############ RANDOM MODULE ###########
import random

rand_num = random.randint(1,10)

print(rand_num)

########## LİSTS ###########
Pneumatics = ["Valve", "Cylinder", "Fittings", "Air Preparation", "Vacuum Pads", "Vacuum Generator", "Sensors"]

print(Pneumatics[3])
print(Pneumatics[-2])

Pneumatics.append("Pressure Sensor")
print(Pneumatics[-1])

########### BANKER ROUTLETTE ###########

import random

friends = ["Eren", "Yiğitcan", "Emir", "Ahmet", "Emre"]

print("Bakalım hesabı kim ödeyecek?")
a = friends[random.randint(0,4)]
print(a,"Üzgünüm ama hesap sana kaldı dostum.")

############## ROCK PAPER SCISSORS #####################

import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_items = [rock, paper, scissors]

usr_ch = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

if usr_ch >= 0 and usr_ch <=2:
    print(game_items[usr_ch])

computer_ch = random.randint(0,2)
print("Computer Chose:")
print(game_items[computer_ch])

if usr_ch >= 3 or usr_ch < 0:
    print("You typed an invalid number. You lose!")
elif usr_ch == 0 and computer_ch == 2:
    print("You win!")
elif computer_ch == 0 and usr_ch == 2:
    print("You lose!")
elif computer_ch > usr_ch:
    print("You lose!")
elif usr_ch > computer_ch:
    print("You win!")
elif computer_ch == usr_ch:
    print("It's a draw!")
