valid = False

while not valid:
    try:
        n = int(input("enater a number: "))

        #enter a even number 
        while n%2 == 0: #inner loop
            print("bye")
            valid = True

    except ValueError:
        print("invaild")    