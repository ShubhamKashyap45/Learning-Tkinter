from tkinter import *
import tkinter.messagebox as tmsg


def open():
    print("Open File")

def new_project():
    print("Open New Project")

def save():
    print("You're file has been saved")

# Help
def help():
    print("A Message box will appear")
    tmsg.showinfo("Help", "Get Help on your own")



# Title
root = Tk()
root.geometry("600x400")
root.title("PyCharm")



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

m2 = Menu(M_menu, tearoff=0)
m2.add_command(label="Help", command=help)
root.config(menu=M_menu)

M_menu.add_cascade(label="Help", menu=m2)



root.mainloop()
