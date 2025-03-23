try:
    num1, num2 = eval(input("Enter two numbers separed by comma: "))
    result = num1/num2 
    print("result is: ", result)
    print("result is: ", result1)

except ZeroDivisionError:
    print("Divison by zero is not allowed")

except SyntaxError:
    print("comma is missing. enter number with sparated comma like this: 1, 2")

except ValueError:
    print("enter numerical value")

except NameError as ex:
    print("the exception is",ex)

except:
    print("some error has occurred")

else:
    print("no exception or no error ")

finally:
    print("I will execute no matter what happens")