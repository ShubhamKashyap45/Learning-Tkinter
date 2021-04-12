from tkinter import *


class GUI(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("600x400")


    def status(self):
        self.var = StringVar()
        self.var.set("This is a status bar")
        self.statusbar = Label(self, textvar=self.var, relief=SUNKEN, anchor="w")
        self.statusbar.pack(side=BOTTOM, fill=X)


    def createbutton(self, inp):



if __name__ == '__main__':
    window = GUI()
    window.status()
    window.mainloop()