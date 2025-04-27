class parrot:
    #class attribute
    species = "dog"

    # instance attribute
    def __init__(self, c, h):
        self.color = c
        self.hight = h

#create the object of the parrot class
doge = parrot("blue", 10)
gray = parrot("browon", 15)

#access th class attribute
print(f"blue is a {doge.species}")
print(f"browon is a {gray.species}")

#access the istance attribute
print(f"{doge.color} is {doge.hight} cm")
print(f"{gray.color} is {gray.hight} cm ")