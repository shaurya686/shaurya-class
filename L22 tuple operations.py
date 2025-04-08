# create a tuple with difference with data types
tuplex = ("tuple", False, 3.2, 1)
print(tuplex)
print()

# create a numeric tuple
tuplex =(4, 6, 2, 8, 3, 1)
print(tuplex)
#tuples are immutable, so you can not add new element 
print()

#using merge of tuples with the + operator you can add an element and it will create a new tuple
tuplex = tuplex + (9,)
print(tuplex)
print()

#counts the number of occurrencen of item  50 from a tuple
tuple1 = (50, 10, 60, 70, 50)
print(tuple1.count(50))
print()

#crate a tuple 
tuplex = (2, 4, 3, 5, 4, 6, 7, 8, 6, 1)

#used tuple[start:stop] the star idex is inculed is incusive and the index is exclusive
_slice = tuplex[3:5]
print(_slice)
print()

#if the start index isn't defined, is taken from the beg inning of the tuple 
_slice = tuplex[:6]
print(_slice)