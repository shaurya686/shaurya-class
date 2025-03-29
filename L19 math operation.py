import math

print("floor value of23.56 is: " + str(math.floor(23.56)))
print("the ceiling value of 23.56 is:" + str(math.ceil(23.56)))
print()

x = 10
y = -15

print("the value of x after copying the sign from y is:" + str(math.copysign(x, y)))
print()

#using fabs and gcd function
print("absolute value of -96 and 56 are:" + str(math.fabs (-96)) + ", " + str(math.fabs(56)))
print()

print("the GCD of 24 and 56 : " + str(math.gcd(24, 56)))
print()

print("sin, cos, tan of 45:")
print(math.sin(45))
print(math.cos(45))
print(math.tan(45))

print()
print("factoral of 5:",math.factorial(5))