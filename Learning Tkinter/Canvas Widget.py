from tkinter import *
root = Tk()

canvas_width = 800
canvas_height = 400

root.geometry(f"{canvas_width}x{canvas_height}")

canvas_widget = Canvas(root, width=canvas_width, height=canvas_height)
canvas_widget.pack()

# To create a line from x1, y1 to x2, y2
canvas_widget.create_line(0,0,800 , 400, fill="green")
canvas_widget.create_line(800, 0, 0,400, fill="red")

# Creating a rectangle
canvas_widget.create_rectangle(5,5,795,395)
# First Coordiantes is of top left then second coordiante is of bottom right
# Top Left = (x1,y1) , Bottom Right = (x2,y2)

# Creating Rectangle
canvas_widget.create_text(400, 200, text="Hello")

# Creating Oval
canvas_widget.create_oval(5, 5, 795, 395)

root.mainloop()