x = frozenset([1, 2, 3, 4, 5])
y = frozenset([3, 4, 5, 6, 7])

#use isdisjoint(). return ture if the set has no element in common with other.
print(x.isdisjoint(y))
print()

#use difference(). return ture if the set has no element in common with other.
print(x.difference(y))
print()

#new set  with element from both x and y
print(x | y)