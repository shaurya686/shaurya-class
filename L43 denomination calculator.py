from tkinter import * 
from tkinter import messagebox
from PIL import Image, ImageTk

#setting up the main window
window = Tk()
window.title("Denomination counter")
window.config (bg="aqua")
window .geometry("650x400")

#adding Image and lables in the main window 
upload = Image.open("app-image.jpeg")

upload = upload.resize((300, 300)) #resize the image using resize()method
image = ImageTk.PhotoImage(upload)
Label = Label(window, image=image, bg="light blue")
Label.place(x=180, y=20)

Label1 = Label(window,
               text="Hello welcome to denomination counter application.",
               bg="aqua")

Label1.place(relx=0.5, y=340, anchor=CENTER)

#function to display a messagebox and proceedif Ok is called
def msg():
    MsgBox = messagebox.showinfo(
        "alert", "do you want to calculate the denomination count?")
    if MsgBox == "ok":
        topwin()

#adding  buttons to the the main window 
button1 = Button(window,
                 text="Let's get stared!",
                 command=msg,
                 bg="green", 
                 fg="white")
button1.place(x=260, y=360)

#function for opening new/top window
def topwin():
    top = Toplevel()
    top.title("denomintion den_counter")
    top.config(bg="light yellow")
    top.geometry("600x350+50+50")


    Label = Label(top, text="enter total amount", bg="light yellow")
    entry = Entry(top)
    lb1 = Label(top, text="here are number of notes for each denomtion", bg="light yellow")

    l1 = Label(top, text="2000", bg="light yellow")
    l2 = Label(top, text="1000", bg="light yellow")
    l3 = Label(top, text="500", bg="light yellow")
    l4 = Label(top, text="100", bg="light yellow")

    t1 = Entry(top)
    t2 = Entry(top)
    t3 = Entry(top)
    t4 = Entry(top)

    def den_counter():
        try:
            global amount
            amount = int(entry.get())
            note2000 = amount // 2000
            amount %=2000