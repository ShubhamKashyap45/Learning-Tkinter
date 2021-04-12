from tkinter import *

root = Tk()
root.geometry("600x500")

def hello():
    print("Hello, You have pressed button1")

frame = Label(root, borderwidth=6, bg="grey", relief=SUNKEN)
frame.pack(side=LEFT, anchor="nw")

b1 = Button(frame, fg="red", text="Button1", command=hello)
b1.pack(side=LEFT, padx=1)

b2 = Button(frame, fg="blue", text="Button2")
b2.pack(side=LEFT, padx=1)

b3 = Button(frame, fg="orange", text="Button3")
b3.pack(side=LEFT, padx=1)

b4 = Button(frame, fg="green", text="Button4")
b4.pack(side=BOTTOM, padx=1)

root.mainloop()
