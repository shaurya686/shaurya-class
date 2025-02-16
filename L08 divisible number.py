a = int(input("enter a number to be divided = "))
b = int(input("enter a divisor = "))

if a % b == 0:
    print(a," can be divided by ",b)
else:
    print(a," cannot be divided by ",b)