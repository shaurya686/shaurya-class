class A:
    def __init__(self, a):
        self.a = a

    def __lt__(self, other):
        if(self.a < other.a):
            return "ob1 is less then ob2"
        else:
            return "ob2 is less then ob1 or both are equal"
        
    def __eq__(self, other):
        if(self.a == other.a):
            return "both are equal"
        else:
            return "not equal"
        
ob1 = A(2)
ob2 = A(3)
print("passed values :", ob1.a, ob2.a)
print(ob1 < ob2)
print()

ob3 = A(4)
ob4 = A(4)
print("passed values :", ob3.a, ob4.a)
print(ob3 < ob4)
print(ob3 == ob4)



