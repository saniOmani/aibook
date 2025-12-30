#create a login page using python
import tkinter as tk
from tkinter import messagebox

def login():
    username = username_entry.get()
    password = password_entry.get()
    if username == "admin" and password == "123456":
        messagebox.showinfo("Login Successful", "Welcome, " + username)
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")

root = tk.Tk()
root.title("Login Page")    
root.geometry("300x200")
root.configure(bg="white")
root.resizable(False, False)
root.mainloop()