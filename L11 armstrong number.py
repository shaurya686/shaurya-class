# take input from user
num = int(input("enter a number: "))

#initialize sum
sum = 0

#find the sum of cube of each digit
temp = num 

while temp < 0:
    digit = temp % 10 # getting the remainder of divison
    sum = sum + digit ** 3 # calculate each digit to the power of 3 and then add to the sum
    temp = temp // 10 # floor divison(the result is rounding down without decimal value)

#display the result
if num == sum:
    print(num,"it is a armstrong number")
else:
    print(num,"it is not armstrong number")