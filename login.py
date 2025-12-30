#create a login page in bash
#import the tkinter library
import tkinter as tk
from tkinter import messagebox

#create a function to login
def login():
    username = username_entry.get()
    password = password_entry.get()
    if username == "admin" and password == "123456":
        messagebox.showinfo("Login Successful", "Welcome, " + username)
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")

#create a root window
root = tk.Tk()
root.title("Login Page")    
root.geometry("300x200")
root.configure(bg="white")
root.resizable(False, False)

#create a username entry
username_entry = tk.Entry(root)
username_entry.pack(pady=10)

#create a password entry
password_entry = tk.Entry(root)
password_entry.pack(pady=10)

#create a login button
login_button = tk.Button(root, text="Login", command=login)
login_button.pack(pady=10)

#run the application
root.mainloop()