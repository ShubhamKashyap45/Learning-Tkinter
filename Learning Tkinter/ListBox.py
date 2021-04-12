from tkinter import *

def add():
    global i
    # print("HEllo World")
    listbox.insert(ACTIVE, f"Number: {i}")
    i=i+1

i=0
root = Tk()
root.geometry("600x500")
root.title("List Box in Tkinter")

listbox = Listbox(root)
listbox.pack()
listbox.insert(END, "Add your items in the list box")

Button(root, text="Add", command=add).pack()


root.mainloop()