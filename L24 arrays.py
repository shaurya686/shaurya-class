import array as arr

# create an array
array_num = arr.array('i', [1, 3, 5, 3, 3, 7, 9, 3])
print("origial array: " + str(array_num))
print(array_num)

#count number of occureneces
print("number of occureneces of the number 3 in the said array: "+str(array_num.count(3)))
print()

#reversce the array
array_num.reverse()
print("reverse the order of the items:")
print(str(array_num))