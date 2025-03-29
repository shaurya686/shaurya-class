def enterage(age):
    if age < 0:
        raise ValueError("only positive integers are allowed")
    if age % 2 == 0:
        print("your age is even")
    else:
        print(" your age is odd")

try:
    num = int(input("enter your age: "))
    enterage(num)
except ValueError:
    print("only positive are allowed")

except:
    print("something is wrong")