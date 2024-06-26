import tkinter as tk
from tkinter import messagebox
import mysql.connector
from tkinter import ttk

def cancel():
    username_entry.delete(0,tk.END)
    password_entry.delete(0,tk.END)
    username_entry.focus_set()
