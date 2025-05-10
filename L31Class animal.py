from abc import ABC

#create class a base class / parent class
class Animal(ABC):
    #should be implemented by all the sub-classes
    def move(self):
        pass

#sub classes
class Human(Animal):
    def move(self):
        print("i can walk and run")

class Snake(Animal):
    def move(self):
        print("i can crawl")

class Dog(Animal):
    def move(self):
        print("i can bark")

class Lion(Animal):
    def move(self):
        print("i can roar")

#create an obj
R = Human()
R.move()

K = Snake()
K.move()

R = Dog()
R.move()

K = Lion()
K.move()