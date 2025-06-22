from tkinter import * 
from tkinter.filedialog import askopenfilenames, asksaveasfilename

#setup root window 
window = Tk()
window.title("My Text Editor")
window.geometry("600x500")#width = 600 height = 500
window.rowconfigure(0, minsize=800, weight=1)
window.columnconfigure(0, minsize=800, weight=1)

#function to open a files
def open_file():
    #open file 
    filepath = askopenfilenames(filetypes=[("Text Files", "*.txt"), ("All file", "*.*")])

    if not  filepath:
        return 
    
    txt_edit.delete(1.0, END)

    #if a file is opended the display the context of the file 
    with open(filepath, "r") as input_file:
        text = input_file.read() #read contents of the input file

        txt_edit.insert(END, text)

        input_file.close()
    window.title(f"My Text Editor - {filepath}")

#function to save a file
def save_file():
    #save the current  file as a new file
    filepath = asksaveasfilename(
                                defaultextension="txt",
                                filetypes=[("Text Files", "*.txt"), ("All file", "*.*")]
                                )
    if not filepath:
        return
    
    with open(filepath, "w") as output_file:
        text = txt_edit.get(1.0, END)# read the edited content
        output_file.write(text)#update in the output file 

    window.title(f"My Text Editor - {filepath}")

# create widgets
txt_edit = Text(window)
fr_buttons = Frame(window, relief= RAISED, bd=2)
bnt_open = Button(fr_buttons, text="open", command=open_file)
bnt_save = Button(fr_buttons, text="save", command=save_file)

#arrange the widgets
bnt_open.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
bnt_save.grid(row=1, column=0, sticky="ew", padx=5)

fr_buttons.grid(row=0, column=0, sticky="ns")
txt_edit.grid(row=0, column=1, sticky="nsew")

window.mainloop()