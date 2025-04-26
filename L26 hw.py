import random

print("starting password generator...")

character = "abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"

password_length = int(input("enter a password length"))

password = []

for i in range(password_length):
    password.append(random.choice(character))

password = ''.join(password)
print("your new password is: "+ password)