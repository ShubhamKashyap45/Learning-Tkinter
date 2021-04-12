from tkinter import *

def enter(event):
    print(f"You clicked button to enter at {event.x}, {event.y}")

def exit(event):
    print(f"You double clicked button to exit at {event.x}, {event.y}")


root = Tk()
root.geometry("600x400")
root.title("Event Handling in tkinter")

widget = Button(root, text="Click Here")
widget.pack()

widget.bind('<Button-1>', enter)
widget.bind('<Double-1>', exit)


root.mainloop()



