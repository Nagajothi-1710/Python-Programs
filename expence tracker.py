storage=[]
dic={}
def add_expence():
    
    amount=float(input("Enter the amount: "))
    category=input("Enter the category: ")
    date=input("Enter the date:((YYYY-MM-DD)): ")
    description=input("Enter a description: ")
    dic={"amount":amount,"category":category, "date":date, "description":description}
    storage.append(dic)

def review_expence():
    print("Expense List:")
    for i,values in enumerate(storage,start=1):
        print(i, "Amount:", values['amount'],"Category:", values['category'], "Date:",values['date'],"Description:",values['description'])

def edit_expence():
    ed=input("Enter the field to edit (amount/category/date/description): ")
    new_value=input(f"Enter the new value for {ed}:")
    storage[op][ed]=new_value

def delete_expence():
    del storage[op]

def generate_report():
    total_amount=0
    for i in storage:
       total_amount+=i['amount']
    print(f"Total amount is : {total_amount}")

while True:
    print("Expense Tracker Menu:")
    print("1. Add Expense \n2. View Expenses \n3. Edit Expense \n4. Delete Expense \n5. Exit")
    option=int(input("Enter your choice:"))
    
    if option==1:
        add_expence()
        print("Expense added successfully!")

    if option==2:
        review_expence()
   
    if option==3:
        review_expence()
        op=int(input("Enter index of the expense to edit:"))-1
        if op < len(storage):
            edit_expence()
            print("Expense edited successfully!")
            
    if option==4:
        review_expence()
        op=int(input("Enter the index of the expense to delete:"))-1
        if op< len(storage):
            delete_expence()
        print("Expense deleted successfully!")
        
    if option==5:
        generate_report()
    
    if option==6:
        exit()
            
    
        
      
      
    
    
    
        

    

