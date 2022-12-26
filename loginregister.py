import time
from tkinter import *
import os
from turtleracing import startgame
import sys

login_success = False
usertrial = False
user_wallet = 0
username_ = 0

def user_register():
    username_string = username.get()
    password_string = password.get()
    file = open(username_string + ".txt", "w")
    file.write("{0}\n".format(username_string))
    file.write("{0}\n".format(password_string))
    file.write("0")
    file.close()
    username_entry.delete(0,END)
    password_entry.delete(0,END)
    Label(screen2, text = "").pack()
    register_label = Label(screen2, text = "Register Successful!", fg="green").pack()
    screen2.after(3000, lambda: [login(), screen2.destroy()])




def user_login():
    global user_wallet
    global username_
    global folders
    username_ = username_verification.get()
    password_ = password_verification.get()
    login_success_label = Label(screen3, text = "Login Successful, Welcome {0} !".format(username_))
    username_invalid_label = Label(screen3, text="Username not found")
    user_invalid_label = Label(screen3, text="Incorrect username or password, please try again")

    folders = os.listdir()
    if (username_ + ".txt") in folders:
        file2 = open(username_+".txt", "r")
        verification_array = file2.read().splitlines()
        if password_ in verification_array:
            user_wallet = float(verification_array[-1])
            file2.close()
            os.chdir('..')
            password_verification_entry.delete(0, END)
            username_verification_entry.delete(0, END)
            Label(screen3, text = "").pack()
            login_success_label.pack()
            Label(screen3, text = "").pack()
            Button(screen3, text="Launch Game", command=lambda: login_success_func()).pack()

        else:
            username_invalid_label.pack()
            password_verification_entry.delete(0, END)

    else:
        user_invalid_label.pack()
        username_verification_entry.delete(0, END)
        password_verification_entry.delete(0, END)



def login():
    global screen3
    global username_verification
    global password_verification
    global username_verification_entry
    global password_verification_entry

    screen3 = Toplevel(screen)
    screen3.title("Login")
    screen3.geometry("350x300")

    username_verification = StringVar()
    password_verification = StringVar()

    Label(screen3, text = "Please enter your login details below").pack()
    Label(screen3, text = "").pack()
    Label(screen3, text = "Username").pack()
    username_verification_entry = Entry(screen3, textvariable=username_verification)
    username_verification_entry.pack()
    Label(screen3, text = "Password").pack()
    password_verification_entry = Entry(screen3, textvariabl=password_verification)
    password_verification_entry.pack()
    Label(screen3, text = "").pack()
    Label(screen3, text = "").pack()
    Button(screen3, text = "Login", command=user_login).pack()


def register():
    global screen2
    global username
    global password
    global username_entry
    global password_entry

    screen2 = Toplevel(screen)
    screen2.title("Register page")
    screen2.geometry("350x300")

    username = StringVar()
    password = StringVar()


    Label(screen2, text ="Please enter your username and password").pack()
    Label(screen2, text = "").pack()
    Label(screen2, text = "Username").pack()
    username_entry = Entry(screen2, textvariable = username)
    username_entry.pack()
    Label(screen2, text = "Password").pack()
    password_entry = Entry(screen2, textvariable = password)
    password_entry.pack()
    Label(screen2, text = "").pack()
    Label(screen2, text = "").pack()
    Button(screen2, text = "Register", command=user_register).pack()


def buttonclicked():
    global usertrial
    usertrial = True


def login_success_func():
    time.sleep(2)
    global login_success
    login_success = True


def Main_window():
    if not usertrial:
        directory = os.getcwd()
        os.chdir("{0}/accounts".format(directory))

    global screen
    screen = Tk()
    screen.geometry("500x200")
    screen.title("Login page")
    Label(text = "Turtle racing",fg="black", font=("Calibri", 13, "bold")).pack()
    Label(text="").pack()
    Button(text="Login", command=lambda: [login(), buttonclicked()]).pack()
    Label(text="").pack()
    Button(text="Register", command=lambda: [register(), buttonclicked()]).pack()
    while True:
        screen.update_idletasks()
        screen.update()
        if login_success:
            sys.argv = ["turtleracing.py", str(user_wallet), username_]
            screen3.destroy()
            screen.destroy()
            startgame()


Main_window()



