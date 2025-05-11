from abc import ABC, abstractmethod

#create parent class
class absclass(ABC):
    #function to print a value 
    def display (self,x):
        print("passed value: ", x)

    #abstract method
    @abstractmethod
    def task(self):
        print("we are inside absclass task")

#create sud class / child class 
class test_class(absclass):
    def task(self):
        print("we are inside test_class task")

#object of test_class create
test_obj = test_class()

test_obj.task()
test_obj.display(100)