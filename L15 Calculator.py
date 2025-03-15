def add(P, Q):
    return P + Q

def subtract(P, Q):
    return P - Q

def multiply (P, Q):
    return P * Q

def divide(P, Q):
    return P / Q

print("select operation")
print("A. Add")
print("B. sudtract")
print("C. Multiply")
print("D. divide")

choies = input("enter your choies (a/b/c/d)= ")

num_1 = int(input("enter your first number: "))
num_2 = int(input("enter your second number: "))
print()

if choies.lower() == 'a':
    result = add(num_1, num_2)
    print(num_1, "+", num_2, "=" ,result)

elif choies.lower() == 'b':
    result = subtract(num_1, num_2)
    print(num_1, "-", num_2, "=" ,result)

elif choies.lower() == 'c':
    result = multiply(num_1, num_2)
    print(num_1, "*", num_2, "=" ,result)

elif choies.lower() == 'd':
    result = divide(num_1, num_2)
    print(num_1, "/", num_2, "=" ,result)

else:
    print("this is a invild input")