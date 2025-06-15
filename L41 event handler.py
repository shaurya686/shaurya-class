from tkinter import * 

#create window 
window = Tk()
window.title("event Handler")
window.geometry("250x250")

#Event handler for Keypress
def handle_keypress(event):
    print(event.char)

#bind keypress event to handle_keypress()
window.bind("<Key>", handle_keypress)

#event handler for button click
def handle_click(event):
    print("The button was clicked!!")

#add widgets
button = Button(text="Click me!")
button.pack()

#bind click event to handle_click()
button.bind("<Button-1>", handle_click)

window.mainloop()