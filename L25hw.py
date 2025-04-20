num = int(input("you want odd and even number under what value? : "))

odd_list = [i for i in range(num) if i%2!=0]
print("list of odd numbers:", odd_list)
print()

even_list = [i for i in range(num) if i%2==0]
print("list of even numbers:", even_list)
print()

fruit = ['apple', 'banana', 'mango', 'papaya', 'grapes']
Fruit = [x[0].upper()+x[1:] for x in range]
print(("Fruitas proper nouns :", fruit))