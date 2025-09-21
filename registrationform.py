from tkinter import *

root = Tk()
root.title ("Registration")
root.geometry("600x470")
root.resizable(False, False)

Label(root, text="Python Registration form", font=("Arial 25")).pack(pady=50)  # "Arial", not "ariel"
Label(root, text="Name", font=("Ariel",23)).place(x=100, y=150)
Label(root, text="Phone", font=("Ariel",23)).place(x=100, y=200)
Label(root, text="Gender", font=("Ariel",23)).place(x=100, y=250)
Label(root, text="Email", font=("Ariel",23)).place(x=100, y=300)



#entry
nameValue = StringVar()
phoneValue = StringVar()
genderValue = StringVar()
emailValue = StringVar()

nameEntry = Entry(root, textvariable=nameValue, width=30, bd=2, font=("Ariel",20))
nameEntry.place(x=200, y=150)  # ✅ Updated coordinates to match the "Name" label

phoneEntry = Entry(root, textvariable=phoneValue, width=30, bd=2, font=("Ariel",20))
phoneEntry.place(x=200, y=200)

genderEntry = Entry(root, textvariable=genderValue, width=30, bd=2, font=("Ariel",20))
genderEntry.place(x=200, y=250)

emailEntry = Entry(root, textvariable=emailValue, width=30, bd=2, font=("Ariel",20))
emailEntry.place(x=200, y=300)

def submit():
    print("Name:", nameValue.get())
    print("Phone:", phoneValue.get())
    print("Gender:", genderValue.get())
    print("Email:", emailValue.get())
    print("✔️ Registration Successful!")

Button(root, text="Submit", command=submit, font=("Ariel",20), bg="green", fg="white").place(x=250, y=370)

root.mainloop()


