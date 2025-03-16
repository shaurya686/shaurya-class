def factorial(n):
    if n == 0 or n == 1:#base  case: 0! and 1! are both 1
        return 1
    else:
        return n * factorial(n - 1 )# rec
    
num = int(input("enter the number:  "))

#check if the number is negative
if num < 0:
    print("Factorial does not exist for negative numbers.")
else:
    result = factorial(num)#calling function and  save the return value in a varible 
    print(f"the factorial of {num} is {result}") 