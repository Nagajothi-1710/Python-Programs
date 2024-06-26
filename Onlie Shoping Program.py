class Product:
    def __init__(self,name,description,price,quantity):
        self.name=name
        self.description=description
        self.price=price
        self.quantity=quantity
    def display(self):
        print(f"Product Name:{self.name}, \nDescription:{self.description}, \nPrice:{self.price}, \nQuantity:{self.quantity}")

class Shoppingcart:
    def __init__(self):
        self.items=[]
        
    def add_products(self,product):
        self.items.append(product)
        
    def remove_products(self,product):
        self.items.remove(product)

    def calculate_total_price(self):
        total_price=0
        for product in self.items:
            total_price+=product.price
        return total_price

class User:
    def __init__(self,username,email,password):
        self.username=username
        self.email=email
        self.password=password
        self.shopping_cart=Shoppingcart()
        
    def add_to_scart(self,product):
        self.shopping_cart.add_products(product)
        
    def remove_to_scart(self,product):
        self.shopping_cart.remove_products(product)

    def place_order(self,shipping_address,payment_method):
        total_price=self.shopping_cart.calculate_total_price()
        order=Order(self.shopping_cart.items,total_price,shipping_address,payment_method)
        print("Order placed successfully")
        print("Order details:")
        for item in order.products:
            print(f"{item.name}:{item.price}")
        print(f"Total Price: {order.total_price}")
        print(f"Shipping address: {order.shipping_address}")
        print(f"Payement method: {order.payment_method}")
            

class Order:
    def __init__(self,products,total_price,shipping_address,payment_method):
        self.products=products
        self.total_price=total_price
        self.shipping_address=shipping_address
        self.payment_method=payment_method
    
        
              
product1=Product("Laptop","Powerful laptop with high performance", 45000,1)
product2=Product("Smartwatch","Fitness tracker with heart rate monitor",15000,1)
product3=Product("Water bottle","SOLARA Insulated Water Bottle 650ml,Hot Water Bottle",1199,1)
product1.display()
product2.display()
product3.display()

user1=User("Nagajothi","jo.bsc2013@gmail.com","Mojosha@123")

user1.add_to_scart(product1)
user1.add_to_scart(product2)
user1.add_to_scart(product3)

user1.remove_to_scart(product2)

user1.place_order("123 main street","Cridit cart")











