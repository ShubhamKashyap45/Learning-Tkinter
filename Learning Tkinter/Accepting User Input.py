from tkinter import *

root = Tk()
root.geometry("644x344")

def getvalue():
    print("Submitting Form")

    print("Name:", namevalue.get())
    print("Phone Number:", phonevalue.get())
    print("Gender:", gendervalue.get())
    print("Payment Method:", paymentvalue.get())
    print("Age:", agevalue.get())
    print("Food Service:", foodvalue.get())

    with open("Airlines Record.txt", "a") as f:
        f.write(f"{namevalue.get(), phonevalue.get(), gendervalue.get(),paymentvalue.get(), agevalue.get(),foodvalue.get()}\n")

# Web Page Title
webpage_title = Label(root, text="Welcome to Indigo Airlines", font="comicsansms 13 bold", pady=20)
webpage_title.grid(row=0, column=4)


# Information of the passanger
name = Label(root, text="Name", padx=10, pady=3)
phonenumber = Label(root, text="Phone Number", padx=10, pady=3)
gender = Label(root, text="Gender", padx=10, pady=3)
age = Label(root, text="Age", padx=10, pady=3)
payment_method = Label(root, text="Payment Method", padx=10, pady=3)

# Packing the information
name.grid(row=1, column=2)
phonenumber.grid(row=2, column=2)
gender.grid(row=3, column=2)
age.grid(row=4, column=2)
payment_method.grid(row=5, column=2)

# Creating variable for the Entry
namevalue = StringVar()
phonevalue = StringVar()
gendervalue = StringVar()
agevalue = StringVar()
paymentvalue = StringVar()
foodvalue = IntVar()

# Taking input from the user for Entry
name_entry = Entry(root, textvariable = namevalue)
phone_entry = Entry(root, textvariable = phonevalue)
gender_entry = Entry(root, textvariable = gendervalue)
age_entry = Entry(root, textvariable = agevalue)
payment_entry = Entry(root, textvariable = paymentvalue)

# Packing the Entry
name_entry.grid(row=1, column=3)
phone_entry.grid(row=2, column=3)
gender_entry.grid(row=3, column=3)
age_entry.grid(row=4, column=3)
payment_entry.grid(row=5, column=3)

# Checkbox
foodservice = Checkbutton(text="Include Meal also", variable = foodvalue, pady=10)
foodservice.grid(row=6, column=3)

# Frame
frame = Frame(root, bg="grey", borderwidth=3, relief=SUNKEN)
frame.grid(row=7, column=3)

# Creating Submit Button
button = Button(frame, text="Submit", command=getvalue)
button.grid(row=7, column=3)


root.mainloop()