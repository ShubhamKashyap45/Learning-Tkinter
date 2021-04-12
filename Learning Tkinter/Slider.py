from tkinter import *
import tkinter.messagebox as tmsg

def info():
    print("The number you chose is:", slider2.get())
    tmsg.showinfo("Info", "Your response has been recorded")



root = Tk()
root.geometry("600x400")
root.title("Slider in tkinter")

randomQ = Label(root, text="Choose a number from the slider", font=("default", 10, "bold")).pack(pady=10)

# How to create a vertical slider
# slider1 = Scale(root, from_=0, to=200)
# slider1.pack()

# How to create a Horizontal slider
slider2 = Scale(root, from_=0, to=300, orient=HORIZONTAL)
slider2.set(56)
slider2.pack()


button = Button(root, text="Click Here", padx=15, command=info).pack(pady=20)




root.mainloop()
