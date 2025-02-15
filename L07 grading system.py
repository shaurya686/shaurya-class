print("enter marks obtained in 5 different subjects  ")
english = int(input("enter your mark for english =  "))
math = int(input("enter your mark for math = "))
science = int(input("enter your mark for science = "))
history = int(input("enter your mark for history = "))
social = int(input("enter your mark for social = "))

total = english + math + science + history + social
avg = total/5

if avg >= 91 and avg <= 100:
    print("your grade is A1")
elif avg >= 81 and avg <= 90:
    print("grade is A2")
elif avg >= 71 and avg <= 80:
    print("your grade is B1")
elif avg >= 61 and avg <= 70:
    print(" your grade is B2")
elif avg >= 51 and avg <= 60:
    print("your grade is C1")
elif avg >= 41 and avg <= 50:
    print("your grade is C2")
elif avg >= 33 and avg <= 40:
    print("your grade is D")
elif avg <= 32:
    print("your grade is E")
else:
    print("invalid input")


