from tkinter import *

root = Tk()

email = Label(root, text= "Email:")
password = Label(root, text = "Password:")
email_entry = Entry(root)
password_entry = Entry(root)

email.grid(row=0)
password.grid(row=2)

email_entry.grid(row=0, column=1)
password_entry.grid(row=2, column=2)


root.mainloop()