row = int(input("please enter  the total number  of rows :"))
number = 1 #intialise by 1

print("floyd's Triangle")
for i in  range (1, row + 1): #represent rows
    for j in range (1, i + 1): #represant columns
        print(number, end = ' ')
        number = number + 1

    print()