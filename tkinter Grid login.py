import tkinter as tk
from tkinter import messagebox
import mysql.connector
from tkinter import ttk

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

def cancel():
    username_entry.delete(0,tk.END)
    password_entry.delete(0,tk.END)
    username_entry.focus_set()
    
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

def dashboard(username):
    def view_user():
        view_user=tk.Tk()
        view_user.geometry("800x600")
        view_user.title("Welcome")
        view_user.configure(background="pink")
        view_user.resizable(False,False)

        welcome_label=tk.Label(view_user,text="Welcome to MOJOSHA super market "+username,bg="pink",font=("arial", 20, "bold"),justify="center")
        welcome_label.grid(row=1,column=0,columnspan=2)
        try:
            con=mysql.connector.connect(host='localhost',database='supermarket',username='root',password='')
            cursor=con.cursor()
            cursor.execute("select * from users")
            data=cursor.fetchall()          
            
            tree=tk.ttk.Treeview(view_user,columns=[str(i) for i in range(len(cursor.column_names))],show='headings')
                        
            # Add column headings
            for i, column in enumerate(cursor.column_names):
                tree.heading(str(i), text=column)

            # Add data rows
            for row in data:
                tree.insert("", "end", values=row)

            # Add treeview to frame
            tree.grid(row=2,column=0)
            
        except mysql.connector.DatabaseError as e:
            if con:
                con.rollback()
                print("The problem is ",e)
                
    def add_product():
        
        def on_select(event):
            global selected_item
            selected_item=event.widget.get()
            
        def insert():
            productid=product_id_entry.get()
            productname=product_name_entry.get()
            discription=discription_entry.get()
            price=price_entry.get()
            quantity=quantity_entry.get()
            manifactuer=manifactuer_entry.get()
            
            try:
                con=mysql.connector.connect(host='localhost',database='supermarket',username='root',password='')
                cursor=con.cursor()
                sql="insert into products values('"+productid+"','"+productname+"','"+selected_item+"','"+discription+"',"+price+","+quantity+",'"+manifactuer+"')"
                cursor.execute(sql)
                con.commit()
                print("Product details added successfully")
        
            except mysql.connector.DatabaseError as e:
                if con:
                    con.rollback()
                    print("The problem is ",e)
           
        add_product=tk.Tk()
        add_product.geometry("800x600")
        add_product.title("Add products")
        add_product.configure(background="pink")
        add_product.resizable(False,False)

        welcome_label=tk.Label(add_product,text="Welcome to MOJOSHA super market ",bg="pink",font=("arial", 20, "bold"),justify="center")
        welcome_label.grid(row=1,column=0,columnspan=2)

        product_id_label=tk.Label(add_product,text="Product ID",bg="pink", font=("arial", 16, "bold"))
        product_id_label.grid(row=2, column=0,padx=10,pady=5)
        product_id_entry=tk.Entry(add_product, font=("arial", 16))
        product_id_entry.grid(row=2, column=1, padx=10,pady=5)
        product_id_entry.focus_set()

        product_name_label=tk.Label(add_product,text="Product Name",bg="pink", font=("arial", 16, "bold"))
        product_name_label.grid(row=3, column=0,padx=10,pady=5)
        product_name_entry=tk.Entry(add_product, font=("arial", 16))
        product_name_entry.grid(row=3, column=1, padx=10,pady=5)

        selected_value=tk.StringVar()
        category_label=tk.Label(add_product,text="Product category",bg="pink", font=("arial", 16, "bold"))
        category_label.grid(row=4, column=0,padx=10,pady=5)
        category_entry=ttk.Combobox(add_product, font=("arial", 16),textvariable=selected_value,state="readonly")
        category_entry.grid(row=4, column=1, padx=10,pady=5)
        category_entry['values']=("Oil","Chocolate","Toys","Milk","Dry Fruit")
        category_entry.bind("<<ComboboxSelected>>",on_select)
        
        discription_label=tk.Label(add_product,text="Discription",bg="pink", font=("arial", 16, "bold"))
        discription_label.grid(row=5, column=0,padx=10,pady=5)
        discription_entry=tk.Entry(add_product, font=("arial", 16))
        discription_entry.grid(row=5, column=1, padx=10,pady=5)

        price_label=tk.Label(add_product,text="Price",bg="pink", font=("arial", 16, "bold"))
        price_label.grid(row=6, column=0,padx=10,pady=5)
        price_entry=tk.Entry(add_product, font=("arial", 16))
        price_entry.grid(row=6, column=1, padx=10,pady=5)

        quantity_label=tk.Label(add_product,text="Quantity",bg="pink", font=("arial", 16, "bold"))
        quantity_label.grid(row=7, column=0,padx=10,pady=5)
        quantity_entry=tk.Entry(add_product, font=("arial", 16))
        quantity_entry.grid(row=7, column=1, padx=10,pady=5)

        manifactuer_label=tk.Label(add_product,text="Manifactuer",bg="pink", font=("arial", 16, "bold"))
        manifactuer_label.grid(row=8, column=0,padx=10,pady=5)
        manifactuer_entry=tk.Entry(add_product, font=("arial", 16))
        manifactuer_entry.grid(row=8, column=1, padx=10,pady=5)

        add_product_button=tk.Button(add_product,text="Add product",bg="green",fg="white",font=("arial", 16, "bold"),command=insert)
        add_product_button.grid(row=9, column=0,padx=10,pady=10)

        cancel_product_button=tk.Button(add_product,text="Cancel product",bg="red",fg="white",font=("arial", 16, "bold"))
        cancel_product_button.grid(row=9, column=1,padx=10,pady=10)

    def view_product():
        view_product=tk.Tk()
        view_product.geometry("1400x600")
        view_product.title("View products")
        view_product.configure(background="pink")
        view_product.resizable(False,False)

        welcome_label=tk.Label(view_product,text="Welcome to MOJOSHA super market "+username,bg="pink",font=("arial", 20, "bold"),justify="center")
        welcome_label.grid(row=1,column=0,columnspan=2)
        try:
            con=mysql.connector.connect(host='localhost',database='supermarket',username='root',password='')
            cursor=con.cursor()
            cursor.execute("select * from products")
            data=cursor.fetchall()
            tree=tk.ttk.Treeview(view_product,columns=[str(i) for i in range(len(cursor.column_names))],show='headings')
                            
                # Add column headings
            for i, column in enumerate(cursor.column_names):
                tree.heading(str(i), text=column)
            for row in data:
                tree.insert("", "end", values=row)
            tree.grid(row=2,column=0)
        except mysql.connector.DatabaseError as e:
            if con:
                con.rollback()
                print("The problem is ",e)
                
    def delete_product():
        def delete():
            productid=product_id_entry.get()
            try:
                con=mysql.connector.connect(host='localhost',database='supermarket',username='root',password='')
                cursor=con.cursor()
                sql="delete from products where productid = '"+productid+"'"
                cursor.execute(sql)
                con.commit()
                print("Product details Deleted successfully")
        
            except mysql.connector.DatabaseError as e:
                if con:
                    con.rollback()
                    print("The problem is ",e)  
            
        delete_product=tk.Tk()
        delete_product.geometry("1400x600")
        delete_product.title("Delete products")
        delete_product.configure(background="pink")
        delete_product.resizable(False,False)

        welcome_label=tk.Label(delete_product,text="Welcome to "+username,bg="pink",font=("arial", 20, "bold"),justify="center")
        welcome_label.grid(row=1,column=0,columnspan=2)

        product_id_label=tk.Label(delete_product,text="product ID",bg="blue",fg="white",font=("arial",16,"bold"))
        product_id_label.grid(row=2,column=0,padx=10,pady=10)
        product_id_entry=tk.Entry(delete_product, font=("arial", 16))
        product_id_entry.grid(row=2, column=1, padx=10,pady=5)

        delete_button=tk.Button(delete_product,text="Delete",bg="blue",fg="white",font=("arial",16,"bold"),command=delete)
        delete_button.grid(row=3,column=0,columnspan=2,padx=10,pady=10)

    dashboard=tk.Tk()
    dashboard.geometry("400x200")
    dashboard.title("Welcome")
    dashboard.configure(background="pink")
    dashboard.resizable(False,False)
    
    welcome_label=tk.Label(dashboard,text="Welcome to "+username,bg="pink",font=("arial", 20, "bold"),justify="center")
    welcome_label.grid(row=1,column=0,columnspan=2)
    
    view_user=tk.Button(dashboard,text="View User",bg="blue",fg="white",font=("arial",16,"bold"),command=view_user)
    view_user.grid(row=2,column=0,padx=10,pady=10)

    add_prod=tk.Button(dashboard,text="Add Product",bg="blue",fg="white",font=("arial",16,"bold"),command=add_product)
    add_prod.grid(row=2,column=1,padx=10,pady=10)

    view_prod=tk.Button(dashboard,text="View Product",bg="blue",fg="white",font=("arial",16,"bold"),command=view_product)
    view_prod.grid(row=3,column=0,padx=10,pady=10)

    delete_prod=tk.Button(dashboard,text="Delete Product",bg="blue",fg="white",font=("arial",16,"bold"),command=delete_product)
    delete_prod.grid(row=3,column=1,padx=10,pady=10)

def forget_pwd():
    def getpwd():
        username=username_entry.get()
        phone=phono_entry.get()
        u=" "
        p=" "
        try:
            con=mysql.connector.connect(host="localhost",database="supermarket",username="root",password="")
            cursor=con.cursor()
            cursor.execute("select * from users where username='"+username+"'")
            data=cursor.fetchall()
            for d in data:
                u=d[0]
                p=d[2]
            if username==u and phone==p:
                messagebox.showinfo("Your password is",d[1])
            else:
                messagebox.showerror("Invalid details")
        except mysql.connector.DatabaseError as e:
            if con:
                con.rollback()
                print("The problem is ",e)
                
    forget_pwd=tk.Tk()
    forget_pwd.geometry("500x200")
    forget_pwd.title("Forget Password")
    forget_pwd.configure(background="pink")
    forget_pwd.resizable(False,False)

    welcome_label=tk.Label(forget_pwd,text="Find your account",bg="pink",font=("arial", 20, "bold"),justify="center")
    welcome_label.grid(row=1,column=0,columnspan=2)

    username_label=tk.Label(forget_pwd, text="Username",bg="pink", font=("arial", 16, "bold"))
    username_label.grid(row=2, column=0,padx=10,pady=5)
    username_entry=tk.Entry(forget_pwd, font=("arial", 16))
    username_entry.grid(row=2, column=1, padx=10,pady=5)
    username_entry.focus_set()

    phono_label=tk.Label(forget_pwd, text="Phone number",bg="pink", font=("arial", 16, "bold"))
    phono_label.grid(row=3, column=0,padx=10,pady=5)
    phono_entry=tk.Entry(forget_pwd, font=("arial", 16))
    phono_entry.grid(row=3, column=1, padx=10,pady=5)

    getpwd_button=tk.Button(forget_pwd, text="Get password",bg="blue", fg="white",font=("arial", 16, "bold"),command=getpwd)
    getpwd_button.grid(row=4,column=0,columnspan=2,padx=10, pady=10)
       
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

login_button=tk.Button(root, text="Login", bg="green", fg="white", font=("arial", 16, "bold"),command=login)
login_button.grid(row=4,column=0,padx=10,pady=20)

cancel_button=tk.Button(root,text="Cancel",bg="red",fg="white",font=("arial", 16, "bold"),command=cancel)
cancel_button.grid(row=4,column=1,padx=10,pady=20)

register_button=tk.Button(root,text="Sign up",bg="blue",fg="white",font=("arial", 16, "bold"),command=signup)
register_button.grid(row=5,column=0,padx=10,pady=10)

forgetpass_button=tk.Button(root,text="Forget password",bg="red",fg="white",font=("arial", 16, "bold"),command=forget_pwd)
forgetpass_button.grid(row=5,column=1,padx=10,pady=10)



