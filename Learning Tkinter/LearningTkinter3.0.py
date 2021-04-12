from tkinter import *
root = Tk()
root.geometry("600x500")
root.title("COVID-19")

# Important Label attributes
# text = add text
# bd = background
# fg = foreground
# font = To set the font
# 1.font=("comicsansms", 15, "bold") '''As a tuple'''
# 2.font="comicsansms 15 bold" '''As a string'''

# padx = x padding
# pady = y padding
# relief = border styling - SUNKEN, RAISED, GROOVE, RIDGE

title_label = Label(text=''' COVID-19
\n A coronavirus is a kind of common virus that causes an infection in your nose, sinuses, or 
upper throat. Most coronaviruses aren't dangerous."
\n "In early 2020, after a December 2019 outbreak in China, the World Health Organization identified SARS-CoV-2 as 
a new type of coronavirus. The outbreak quickly spread around the world.
\n COVID-19 is a disease caused by SARS-CoV-2 that can trigger what doctors call a respiratory tract infection.
\n It can affect your upper respiratory tract (sinuses, nose, and throat) or lower respiratory tract.''', bg="red",
                    fg="white", padx=25, pady=30, font="comicsansms 15 bold", borderwidth=6, relief=SUNKEN)

# Important pack Attributes
# anchor="nw"
# anchor="se"
# side = TOP, BOTTOM, LEFT, RIGHT


# title_label.pack(anchor="nw")
# title_label.pack(side=BOTTOM, anchor="sw", fill=X)
# title_label.pack(side=LEFT, fill=Y, padx=25, pady=15)
title_label.pack(padx=25, pady=15)

root.mainloop()