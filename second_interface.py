from tkinter import *
from tkinter import messagebox
root = Tk()
root.geometry("500x500")
root.title("Exception Handling")
root.config(bg="#fcbf49")

amount = StringVar()
R = StringVar()

Label(root, text="Please Enter Amount in Your Account", font=60, foreground="#000000", bg="#fcbf49").place(x=100, y=30)
Label(root, text="R", font=60, foreground="#000000", bg="#fcbf49").place(x=100, y=80)

amount_ent = Entry(root, text="R", width=25, textvariable=amount)
amount_ent.focus()
amount_ent.place(x=120, y=80)


def clear():
    amount_ent.delete(0, END)


clear_btn = Button(root, cursor="hand2", text="Clear", foreground="#e5e5e5", borderwidth="5", bg="#14213d", command=clear)
clear_btn.place(x=290, y=130)


def check():
    try:
        if int(amount_ent.get()) < 3000:
           messagebox.showinfo("Save More!", "Please deposit more funds for this excursion")
           root.destroy()

    except ValueError:
        if amount_ent.get() != int:
            messagebox.showerror("Entry Invalid ", "Please Enter amount in Numbers")
    else:
        if int(amount_ent.get()) >= 3000:
            messagebox.showinfo("Congratulations!!!", "You qualify for the Malaysia trip")
            root.destroy()


check_btn = Button(root, cursor="hand2", text="Check Qualification", foreground="#e5e5e5", borderwidth="5", bg="#14213d", command=check)
check_btn.place(x=105, y=130)


root.mainloop()
