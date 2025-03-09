r = int(input("Enter the total number of rows: "))

print("Mirrored right triangle star patten")
for i in range(1,r+1):
    for j in range(1,r+1):
        if (j <= r -i):
            print(' ',end = ' ')
        else:
            print('*', end = ' ')
    print()