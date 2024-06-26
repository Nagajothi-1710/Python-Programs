import tkinter as tk
from tkinter import messagebox
import mysql.connector
from tkinter import ttk

def signup():
    def register():
        username_signup=username_entry_up.get()
        password_signup=password_entry_up.get()
        phono_signup=phono_entry_up.get()
        email_signup=email_entry_up.get()
        try:
            con=mysql.connector.connect(host='localhost',database='supermarket',username='root',password='')
            cursor=con.cursor()
            sql="insert into users values('"+username_signup+"','"+password_signup+"','"+phono_signup+"','"+email_signup+"')"
            cursor.execute(sql)
            con.commit()
            print("Register successfully")
        except mysql.connector.DatabaseError as e:
            if con:
                con.rollback()
                print("The problem is ",e)
    signup=tk.Tk()
    signup.geometry("500x300")
    signup.title("MOJOSHA users signup")
    signup.configure(background="pink")
    signup.resizable(False,False)
    welcome_label=tk.Label(signup,text="Welcome to MOJOSHA super market",bg="pink",font=("arial", 20, "bold"),justify="center")
    welcome_label.grid(row=1,column=0,columnspan=2)
    
    username_label_up=tk.Label(signup, text="Username",bg="pink", font=("arial", 16, "bold"))
    username_label_up.grid(row=2, column=0,padx=10,pady=5)
    username_entry_up=tk.Entry(signup, font=("arial", 16))
    username_entry_up.grid(row=2, column=1, padx=10,pady=5)
    username_entry_up.focus_set()

    password_label=tk.Label(signup,text="Password",bg="pink", font=("arial", 16, "bold"))
    password_label.grid(row=3, column=0,padx=10,pady=5)
    password_entry_up=tk.Entry(signup, font=("arial", 16),show="*")
    password_entry_up.grid(row=3, column=1, padx=10,pady=5)

    phono_label_up=tk.Label(signup, text="Phone number",bg="pink", font=("arial", 16, "bold"))
    phono_label_up.grid(row=4, column=0,padx=10,pady=5)
    phono_entry_up=tk.Entry(signup, font=("arial", 16))
    phono_entry_up.grid(row=4, column=1, padx=10,pady=5)

    email_label_up=tk.Label(signup, text="Email",bg="pink", font=("arial", 16, "bold"))
    email_label_up.grid(row=5, column=0,padx=10,pady=5)
    email_entry_up=tk.Entry(signup, font=("arial", 16))
    email_entry_up.grid(row=5, column=1, padx=10,pady=5)

    register_button=tk.Button(signup, text="Register", bg="green", fg="white", font=("arial", 16, "bold"),command=register)
    register_button.grid(row=6,column=0,padx=10,pady=20)
    
    cancel_button=tk.Button(signup,text="Cancel",bg="red",fg="white",font=("arial", 16, "bold"),command=cancel)
    cancel_button.grid(row=6,column=1,padx=10,pady=20)
