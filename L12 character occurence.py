#Take input of a word
string = input("enter your word or sentence = ")

#take input of a character
char = input("enter your character = ")

i = 0
count = 0

#loop will find the occurence of character
while (i < len (string )): #string operation
    if (string[i] == char):
        count = count + 1

    i = i + 1
    
#display result
print("the number of",char,"character has occurenced ",count,"time") 