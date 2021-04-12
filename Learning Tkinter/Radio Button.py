from tkinter import *
import tkinter.messagebox as tmsg

def color():
    print(f"The colour you have selected is: {var.get()}")
    tmsg.showinfo("Colour", "We have selected your colour")

root = Tk()
root.geometry("600x400")
root.title("Radiobutton in Tkinter")

var = IntVar()
Label(root, text="What is your favourite colour??", font="Lucida 15 bold", pady=10,).pack()


# Radiobuttons
R_button = Radiobutton(root, text="Yellow", variable=var, padx=15, value=1).pack(anchor="w")
R_button = Radiobutton(root, text="Red", padx=15, variable=var, value=2).pack(anchor="w")
R_button = Radiobutton(root, text="Green", variable=var, padx=15, value=3).pack(anchor="w")
R_button = Radiobutton(root, text="Blue", variable=var, padx=15, value=4).pack(anchor="w")

Button(root, text="Select Colour",pady=10, command=color).pack()
root.mainloop()
