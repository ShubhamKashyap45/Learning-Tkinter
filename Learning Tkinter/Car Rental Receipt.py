from tkinter import *

root = Tk()
root.geometry("600x500")
root.title("Car Rental Receipt")

def getvalue():
    print("Date:", datevalue.get())
    print("Receipt:", receiptvalue.get())

# Label
text_label = Label(text="CAR RENTAL RECEIPT", font=("Open Sans", 15, "bold"))
text_label.grid(row=0, column=0)


date = Label(root, text="Date:")
receipt = Label(root, text="Receipt #:")
date.grid(row=1, column=0)
receipt.grid(row=2, column=0)


datevalue = StringVar()
receiptvalue = StringVar()

user_date = Entry(root, textvariable = datevalue)
user_receipt = Entry(root, textvariable = receiptvalue)
user_date.grid(row=1, column=2)
user_receipt.grid(row=2, column=2)

button1 = Button(root,text="Submit", command=getvalue)
button1.grid()



root.mainloop()