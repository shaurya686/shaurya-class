class arkansas():
    def capital(self):
        print("little rock is the capital of arkansas")

    def language(self):
        print("english is the national language of arkansas.")

    def type(self):
        print("arkansnas is a Southern state")

#class 2
class USA():
    def capital(self):
        print("washington is the capital of USA")

    def language(self):
        print("english is the national language of USA.")

    def type(self):
        print("USA is a developed country.")

#object creation
obj_ark = arkansas()
obj_usa = USA()

#common interfrace
for conutry in (obj_ark, obj_usa):
    conutry.capital()
    conutry.language()
    conutry.type()
    print()