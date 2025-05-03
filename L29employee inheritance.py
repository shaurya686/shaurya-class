class person( object ): #parent class
    # __init__ is knownas the constructor
    def __init__(self , nm, idno):
        self.name = nm
        self.idnumber = idno

    def Display(self):
        print(self.name)
        print(self.idnumber)

class  enployee(person): # child class
    def __init__(self, name , idnumber, wage, postion):
        self.salary = wage 
        self.post = postion

        # invoking the __init__ of the parent class
        person.__init__(self, name, idnumber)


# creation of an odject varible or an instance
a = enployee('jessica', 626012, 500000, "permanent employee")

# calling a function of the class person using it instance
a.Display() 