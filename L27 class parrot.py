class parrot:
    #class attribute
    species = "bird"

    # instance attribute
    def __init__(self, nm, h):
        self.name = nm
        self.age = h

#create the object of the parrot class
blu = parrot("blue", 10)
woo = parrot("wooey", 15)

#access th class attribute
print(f"blue is a {blu.species}")
print(f"wooey is a {woo.species}")

#access the istance attribute
print(f"{blu.name} is {blu.age} years old")
print(f"{woo.name} is {woo.age} years old")