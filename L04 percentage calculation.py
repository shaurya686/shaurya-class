#take marks as input
print("enter mark of your subjects here ")
math = int(input("enter your mark for math = "))
english = int(input("enter your mark for english = "))

#sum of all subjects
sum = math + english

#calculate percentage
percentage = sum/2 * (100/100)

print("your percentage mark is ",percentage,"%")