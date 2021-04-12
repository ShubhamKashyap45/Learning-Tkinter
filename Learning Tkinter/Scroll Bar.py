from tkinter import *
root = Tk()
root.geometry("600x500")
root.title("Scroll Bar in Tkinter")

# To create a scroll bar
# 1. yscrollcommand = scrollbar.set (Put this command inside the widget)
# 2. scroll.config(command=widget.yview) (Put this command after packing the widget)

# Adding Scrollbar
scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)

listbox = Listbox(root, yscrollcommand = scrollbar.set)
for i in range(50):
    listbox.insert(END, f"Number: {i}")

listbox.pack(fill=BOTH, padx=10)
scrollbar.config(command=listbox.yview)


root.mainloop()