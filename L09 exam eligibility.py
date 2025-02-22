sick = input("are you currently sick (y/n)? ")

attendance = int(input("enter the attendance day of the student = "))

if sick.lower() == "y":
    print("you are not allow to take exam ")
elif sick.lower() == "n":
    if attendance >= 75:
        print("you are allow to take exam")
    else:
        print("you are not allow to take exam")
else:
    print("invild opinion")