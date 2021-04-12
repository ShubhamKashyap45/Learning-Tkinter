from tkinter import *
from PIL import Image, ImageTk

root = Tk()

# Width x Height
root.geometry("600x400")
root.title("My First GUI")

# Width, Height
root.minsize(200, 100)

# Width, Height
root.maxsize(1200, 900)

# Label
text_label = Label(text="This is a GUI")
text_label.pack()

# Photo
# photo = PhotoImage(file="2.png")

# For JPG image
image = Image.open("photo.jpg")
photo = ImageTk.PhotoImage(image)




# Photo Label
photo_label = Label(image=photo)
photo_label.pack()

# GUI Logic
root.mainloop()
