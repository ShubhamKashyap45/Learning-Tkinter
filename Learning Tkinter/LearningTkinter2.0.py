from tkinter import *

root = Tk()

# Width x Height
# root.geometry("600x400")

# Width, Height
root.minsize(400, 400)

# Width, Height
# root.maxsize(1200, 900)

# Label
text_label = Label(text="This is a GUI", font=("Open Sans", 20, "bold"), bg="red", fg="white")
text_label.config(padx=20, pady=20)
text_label.grid(column=0, row=1)


# Photo
canvas = Canvas(width=128, height=128)
photo = PhotoImage(file="play.png")
canvas.create_image(65, 65, image=photo)
canvas.grid(column=1, row=2)


# Photo Label
# photo_label = Label(image=photo)
# photo_label.pack()

# GUI Logic
mainloop()
