from tkinter import *
root = Tk()

root.geometry("500x350")
f1 = Frame(root, bg="grey", borderwidth=3, relief=SUNKEN)
f1.pack(side=LEFT, fill=Y)

f2 = Frame(root, bg="yellow", borderwidth=6, relief=SUNKEN)
f2.pack(side=TOP, fill=X)

l1 = Label(f1, text="Left side of the frame", font="Helvetica 15 bold", fg="red")
l1.pack(pady=120)

l2 = Label(f2, text="Top side of the frame", font="comicsansms 15 bold", fg="green")
l2.pack()

root.title("Creating Frame")


root.mainloop()
