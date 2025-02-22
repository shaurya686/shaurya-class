print("seclect your ride")
print("1. bike")
print("2. car")

choice = int(input("enter your choice 1 or 2 = "))

if choice == 1:
    print("what type of bike? ")
    print("1 scooter")
    print("2 sport bike")

    choice2 = int(input("enter your type of bike 1 or 2 = "))

    if choice2 == 1:
        print("you have selected scooter bike")
    else:
        print(" you have selected sport bike ")

elif choice == 2:
    print("what type of car?")
    print("1. sedan")
    print("2. suv")

    choice3 = int(input("enter your type of car 1 or 2 = "))

    if choice3 == 1:
        print("you have seleced sedan")
    else:
        print("you have selected suv")

else:
    print("wrong choice")