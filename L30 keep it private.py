class myClass:
    # private variable
    __privateVar = 27;

    #private method
    def __privmeth(self):
        print("i'm inside class myClass")

    # function to print value of private variable
    def hello(self):
        print("private variable value: ",myClass.__privateVar)

 #object cretion and method call
foo = myClass()
foo.hello()
foo.__privmeth()# this will give error cz private can't be accessed