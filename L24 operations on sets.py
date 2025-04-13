# a set of integers
my_set = (1, 2, 3)
print(my_set)
print()

#set of mixed datetype
my_set = {1.0, "hello", (1, 2, 3)}
print(my_set)
print()

# set can not have duplicate
my_set = {1, 2, 3, 4, 3, 2}
print(my_set)
print()

#we can make set of list
my_set = ([1, 2, 3, 2])
print(my_set)
print()

# remove  a number from set
num_set = set([0, 1, 2, 3, 4, 5])
print("origial set: ")
print(num_set)
print()

num_set.pop()
print(" after removing the first element from the said  set:")
print(num_set)