import tkinter as tk
from tkinter import messagebox
import mysql.connector
from tkinter import ttk

import signup
import cancel
cancel.cancel()
signup.signup()
signup.register()

def login():
    username=username_entry.get()
    password=password_entry.get()
    u=" "
    p=" "
    try:
        con=mysql.connector.connect(host="localhost",database="supermarket",username="root",password="")
        cursor=con.cursor()
        cursor.execute("select * from users where username='"+username+"'")
        data=cursor.fetchall()
        for d in data:
            u=d[0]
            p=d[1]
        
        if username== u and password== p:
            #messagebox.showinfo("Login successfully","Welcome "+username)
            dashboard(username)
        else:
            messagebox.showerror("Invalid Username and password")
        
    except mysql.connector.DatabaseError as e:
        if con:
            con.rollback()
            print("The problem is ",e)

root=tk.Tk()
root.geometry("500x280")
root.title("Login page")
root.configure(background="pink")
root.resizable(False,False)

label=tk.Label(root, text="Welcome to MOJOSHA super market",bg="pink",font=("arial", 20, "bold"),justify="center")
label.grid(row=1,column=0,columnspan=2)

username_label=tk.Label(root, text="Username",bg="pink", font=("arial", 16, "bold"))
username_label.grid(row=2, column=0,padx=10,pady=5)
username_entry=tk.Entry(root, font=("arial", 16))
username_entry.grid(row=2, column=1, padx=10,pady=5)
username_entry.focus_set()

password_label=tk.Label(root,text="Password",bg="pink", font=("arial", 16, "bold"))
password_label.grid(row=3, column=0,padx=10,pady=5)
password_entry=tk.Entry(root, font=("arial", 16),show="*")
password_entry.grid(row=3, column=1, padx=10,pady=5)

login_button=tk.Button(root, text="Login", bg="green", fg="white", font=("arial",                                                                                                16, "bold"),command=login)
login_button.grid(row=4,column=0,padx=10,pady=20)

cancel_button=tk.Button(root,text="Cancel",bg="red",fg="white",font=("arial", 16, "bold"),command=cancel)
cancel_button.grid(row=4,column=1,padx=10,pady=20)

register_button=tk.Button(root,text="Sign up",bg="blue",fg="white",font=("arial", 16, "bold"),command=signup)
register_button.grid(row=5,column=0,padx=10,pady=10)

forgetpass_button=tk.Button(root,text="Forget password",bg="red",fg="white",font=("arial", 16, "bold"),command=forget_pwd)
forgetpass_button.grid(row=5,column=1,padx=10,pady=10)
