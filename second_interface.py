from tkinter import *
from tkinter import messagebox
root = Tk()
root.geometry("500x500")
root.title("Exception Handling")
root.config(bg="#fcbf49")

amount = StringVar()
R = StringVar()

Label(root, text="Please Enter Amount in Your Account", font=60, foreground="#000000", bg="#fcbf49").place(x=100, y=30)




amount_ent = Entry(root, text="R", width=25, textvariable=amount)

amount_ent.place(x=120, y=80)


check_btn = Button(root, text="Check Qualification", font="5", foreground="#e5e5e5", width=15, borderwidth="5", bg="#14213d")
check_btn.place(x=135, y=130)


root.mainloop()
