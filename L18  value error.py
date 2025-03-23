try :
    num = int(input("enter your number : "))
    print("the number entered is: ", num)

except ValueError as e: # using value error 
    print("exception: ",e)

print("I am outside the try-except block") #always exected and display ed the message
print()