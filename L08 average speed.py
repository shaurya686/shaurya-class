a = int(input("enter the speed1 = "))
b = int(input("enter the speed2 = ")) 
c = int(input("enter the speed3 = "))

total = a + b + c 
avg = total / 3

if avg > a and avg > b and avg > c:
    print(avg," is greater then ",a," and ",b," and ",c)
elif avg > a and avg > b:
    print(avg," is greater the ",a," and ",b)
elif avg > a and avg > c:
    print(avg," is greater the ",a," and ",c)
elif avg > b and avg > c:
    print(avg," is greater the ",b," and ",c)
elif avg > a:
    print(avg," is greater the ",a)
elif avg > b:
    print(avg," is greater the ",b)
elif avg > c:
    print(avg," is greater the ",c)
else:
    print("invalid input")
