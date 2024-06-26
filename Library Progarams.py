class Library:
    def __init__(self):
        self.books=["C","C++","Java","Php"]
        
    def add_book(self,book):
        self.books.append(book)
        print(f"{book} book is been added to the shelf")
        
    def remove_book(self,book):
        self.books.remove(book)
        print(f"{book} book is been deleted from the shelf successfully")

    def display(self):
        print("The Book in the shelf are:",self.books)

    def lend_book(self,book,name):
        if book in self.books:
            print(f"{book} book is been barrowed by {name}")
            self.books.remove(book)
        else:
            print(f"Sorry {book} book is not available in shelf")
            
       
        
print("Welcome to Central library")
l=Library()

while True:
    print("1. Add Book \n2.Remove Book \n3.Display Book \n4.Lend Book")
    option=int(input("Enter the option: "))
    if option == 1:
        book=input("Enter the book name: ")
        l.add_book(book)
    elif option==2:
        book=input("Enter the book name: ")
        l.remove_book(book)
    elif option==3:
        l.display()

    elif option==4:
        book=input("Enter the book name: ")
        name=input("Enter your name: ")
        l.lend_book(book,name)

        
        
