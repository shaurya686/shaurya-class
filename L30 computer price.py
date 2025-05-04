class computer:
    def __init__(self):#constructor
        self.__maxprice = 900 #private variable

    def sell(self):
        print(f"selling price: {self.__maxprice}")

    def setmaxprice(self, price):
        self.__maxprice = price

#create object
c = computer()
print("origal price:")
c.sell()
print()

#change the price
print("after try to change it directly")
c.__maxprice = 1000
c.sell()
print()

#using setter function
print("change it using setmaxprice method")
c.setmaxprice(1500)
c.sell()