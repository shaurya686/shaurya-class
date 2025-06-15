from tkinter import * 
from tkinter import messagebox

#setup tkinter window
window = Tk()
window.geometry("250x250")
window.title("Virus Detected")

def msg():
    messagebox.showwarning("Alert", "Stop! Virus Found.")

#add widget
btn = Button(window, text="Scan for virus", command=msg)
btn.place(x=75, y=80)


window.mainloop()