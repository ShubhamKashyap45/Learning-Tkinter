from tkinter import *

root = Tk()
root.geometry("600x500")

def getvalue():
    print("Username:", uservalue.get())
    print("Password:", passvalue.get())


username = Label(root, text="Username")
password = Label(root, text="Password")
username.grid(row=0, column=0)
password.grid(row=1, column=0)

# Variable classes in tkinter
# BooleanVar, DoubleVar, IntVar, StringVar

uservalue = StringVar()
passvalue = StringVar()

# Creating Entry
user_entry = Entry(root, textvariable = uservalue)
user_password = Entry(root, textvariable = passvalue)
user_entry.grid(row=0, column=1)
user_password.grid(row=1, column=1)

button1 = Button(root,text="Submit", command=getvalue)
button1.grid()



root.mainloop()