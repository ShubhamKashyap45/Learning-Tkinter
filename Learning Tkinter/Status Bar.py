from tkinter import *

def update():
    import time
    status_var.set("Updating......")
    statusbar.update()
    time.sleep(2)
    status_var.set("Updated your file")



root = Tk()
root.geometry("600x500")
root.title("Scroll Bar in Tkinter")

status_var = StringVar()

# Status Bar
statusbar = Label(root, textvariable=status_var, relief=SUNKEN, anchor="w")
status_var.set("This is a Status Bar")
statusbar.pack(side=BOTTOM, fill=X)

Button(root, text="Update File", padx=10, command=update).pack(pady=20)



root.mainloop()
