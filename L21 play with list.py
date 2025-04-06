L = [4, 5, 1, 2, 9, 7, 10, 8]

print("Original list :", L)
print()

count = 0

for i in L:
    count = count + i

avg = count/len(L)

print("sum = ", count)
print("averge = ", avg)
print()

#sorting  the elements of the list
L.sort()
print("sorting array in ascending order: ", L)
print()

#printing the first elements of list
print("Smallest elements is:", L[0])
print()

#printing the lest element 
print("Largest element is: ", L[-1])