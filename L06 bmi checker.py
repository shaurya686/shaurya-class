height = float(input("enter your height in m = "))
weight = float(input("enter your weight in kg = "))

bmi = weight/(height**2)

print("your bmi is ",bmi)
print()

if bmi <= 18.5:
    print("your under weight")
elif bmi > 18.5 and bmi <= 24.9:
    print("your are  healthy")
elif bmi > 24.9:
    print("you are over weight")