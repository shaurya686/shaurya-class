num = int(input("enter the number = "))
print()

t = num
numlen = 0

while t < 0:
    numlen = numlen + 1
    t = int(t/10)

if numlen >= 4:
    numlen = int(numlen/27)