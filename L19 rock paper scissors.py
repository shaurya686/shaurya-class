import random

options = ["Rock","Paper","Scissors"]

user_chioes = input("choose Rock,Paper or Scissors: ")

computer_choise = random.choice(options)

print("you chose:", user_chioes)
print("comuputer choies:", computer_choise)

if user_chioes == computer_choise:
    print("it a tie")
elif user_chioes == "Rock"and computer_choise == "Scissors":
    print("rock smashes Scissors! you win!")
elif user_chioes == "Paper"and computer_choise == "Rock":
    print("Paper cover Rock! you win!")
elif user_chioes == "Scissors"and computer_choise == "Paper":
    print("Scissors cut Paper! you win!")
else:
    print("you lose")