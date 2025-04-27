class IOString():

    #constructor to set default value
    def __init__(self):
        self.str1 = ""

    #method to get input from user
    def get_String(self):
        self.str1 = input("enter string :")

    #method to print the stringin upper case
    def print_String(self):
        print("result is :", self.str1.upper())

#Object creation
str_obj = IOString()

#call method
str_obj.get_String()
str_obj.print_String()      