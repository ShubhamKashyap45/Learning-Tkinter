from tkinter import *

# def File():
#     print("Open File")

# def for File Menu
def open():
    print("Open File")

def new_project():
    print("Open New Project")

def save():
    print("You're file has been saved")


# def for Edit menu
def cut():
    print("Cut")

def copy():
    print("Copied")

def paste():
    print("Print")

def delete():
    print("Delete")

# View
def view():
    print("View")

# Title
root = Tk()
root.geometry("600x400")
root.title("PyCharm")

# my_menu = Menu(root)
# my_menu.add_command(label="File", command=File)
# my_menu.add_command(label="Exit", command=quit)
# root.config(menu=my_menu)


# File Menu
M_menu = Menu(root)
m1 = Menu(M_menu, tearoff=0)
m1.add_command(label="New Project", command=new_project)
m1.add_command(label="Open", command=open)
m1.add_command(label="Save As", command=save)
m1.add_separator()
m1.add_command(label="Exit", command=quit)
root.config(menu=M_menu)

M_menu.add_cascade(label="File", menu=m1)

#Edit Menu
m2 = Menu(M_menu, tearoff=0)
m2.add_command(label="Cut",command=cut)
m2.add_command(label="Copy", command=copy)
m2.add_command(label="Paste", command=paste)
m2.add_separator()
m2.add_command(label="Delete", command=delete)
root.config(menu=M_menu)

M_menu.add_cascade(label="Edit", menu=m2)

#View
View = Menu(M_menu)
M_menu.add_cascade(label="View")

# Navigate
Navigate = Menu(M_menu, tearoff=0)
M_menu.add_cascade(label="Navigate")


root.mainloop()
