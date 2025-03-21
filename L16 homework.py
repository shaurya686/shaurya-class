import os

shutdown = input ("do you wish to shut down your laptop")

if shutdown.lower() == 'no':
    exit()
elif shutdown.lower() == 'yes':
    os.system("shutdown /s /t 1 ")
else:
    print("invild input")
