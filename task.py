import tkinter
from tkinter import *
from tkinter import messagebox
root = Tk()
root.geometry("500x500")
root.title("Authentification")
root.config(bg="#1d3557")

user_names = StringVar()
passwords = StringVar()

Label(root, text="Please Enter Login Details", font=60, foreground="#a8dadc", bg="#1d3557").place(x=150, y=30)

Label(root, text="Username: ", foreground="#a8dadc", font=30, bg="#1d3557").place(x=200, y=80)

name_ent = Entry(root, text=" ", width=25, textvariable=user_names)
name_ent.focus()
name_ent.place(x=150, y=110)

Label(root, text="Password: ", font=30, foreground="#a8dadc", bg="#1d3557").place(x=200, y= 150)
password_ent = Entry(root, text=" ", width=25, textvariable=passwords, show="*")
password_ent.place(x=150, y=180)


def access():
    user_names = ["Abdul-Malik"]
    passwords = ["0000"]

    n = len(user_names)
    p = len(passwords)
    found = False

    for x in range(n):

        if name_ent.get() == user_names[x] and password_ent.get() == passwords[x]:
            found = True

    if found == True:
        messagebox.showinfo("Login Successful", "Access Granted!")
        root.destroy()
        import second_interface

    else:
        messagebox.showinfo("Login Failed", "Access Denied!")


def clear():
    name_ent.delete(0, END)
    password_ent.delete(0, END)


def close_program():
    root.destroy()


login = Button(root, text="Login", font=10, foreground="#1d3557", width=20, borderwidth="5", command=access, bg="#a8dadc")
login.place(x=135, y=230)


clear_btn = Button(root, text="Clear", font=10, foreground="#1d3557",borderwidth="5", command=clear, bg="#a8dadc")
clear_btn.place(x=140, y=320)

close = Button(root, text="Close", font=10, foreground="#e63946", borderwidth="5", command=close_program, bg="#a8dadc")
close.place(x=290, y=320)


root.mainloop()
