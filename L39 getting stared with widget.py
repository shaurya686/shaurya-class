from tkinter import *
from datetime import date 

#create window
window = Tk()
window .title("getting stared with widgets")
window.geometry("400x300")

def display(): #function to display a message 

    name = name_entry.get()

    #declaring gloable variable
    # to make it accessible anywherein the program
    global Message
    Message = "welcome to the application! \nToday's date is: "
    greet = "Hello "+name+"\n"

    #display detail in a text box
    #specfic where to add the detail inside the box 
    text_box.insert(END, greet)
    text_box.insert(END, Message)
    text_box.insert(END, date.today())

#add widgets
lb1 = Label(text="Hey there!", fg="white", bg="#072F5F", height=1, width=300)

name_lb1 = Label(text="Enter your full name below", bg="blue", fg="white")
name_entry = Entry()# text input

text_box = Text(height=3)

btn = Button(text="Display message", command=display, height=1, bg="red", fg="white")


#organzie all the widget in the window
lb1.pack()
name_lb1.pack()
name_entry.pack()
btn.pack()
text_box.pack()

window.mainloop()
