class Product:
    def __init__(self, productid: int, product_name: str, price: float)-> None:
        self.__productid = productid
        self.__product_name = product_name
        self.__price = price
    
    @property
    def productid(self) -> int:
        return self.__productid
    
    @property
    def price(self) -> float:
        return self.__price
    
    def __str__(self) -> str:
        return f"Product id= {self.__productid}, name= {self.__product_name}, price= {self.__price}"
    
    

class Customer:
    def __init__(self, name: str, address: str) -> None:
        self.__name = name
        self.__address = address
        
        
    def __str__(self) -> str:
        return f"Customer name= {self.__name}, address= {self.__address}"
    
    
class Orderitem:
    def __init__(self, product: Product, quantity: int) -> None:
        self.__product = product
        self.__quantity = quantity
        
        
    @property
    def product(self):
        return self.__product
    
    @property
    def quantity(self):
        return self.__quantity
    
    @quantity.setter
    def quantity(self, quantity):
        self.__quantity = quantity
        
    def __str__(self) -> str:
        return f"Item Product= {self.__product}, quantity= {self.__quantity}"
    
    
    
class Order:
    def __init__(self, oredrid: int, customer: Customer) -> None:
        self.__oredrid = oredrid
        self.__customer = customer
        self.__order_items: list[Orderitem] = []
        
    def __str__(self) -> str:
        output: str = f"Order id= {self.__oredrid}\n"
        output += f"Customer= {self.__customer}\n"
        # output += f"Item Product= {self.__order_items}"
        if not self.__order_items:
            output += "No items in the order.\n"
        else:
            output += "Items in the order:\n"
            for item in self.__order_items:
                output += f"{item}\n"
        
        return output
    
    def add_item(self, product: Product, quantity: int) -> None:
        
        for item in self.__order_items:
            if item.product == product:
                item.quantity += quantity
                return
            
        self.__order_items.append(Orderitem(product, quantity))
        
        
    def __iter__(self):
        self.__index = -1
        return self
    
    def __next__(self):
        if self.__index >= len(self.__order_items)-1:
            raise StopIteration
        self.__index += 1
        return self.__order_items[self.__index]
    
    def remove_item(self, productid: int) -> None:
        for item in self:
            if item.product.productid == productid:
                self.__order_items.pop(self.__index)
                return
            
    def find_largest_item(self) -> Orderitem | None:
        largest_item = None
        for item in self.__order_items:
            if largest_item is None:
                largest_item = item
            elif item.quantity > largest_item.quantity:
                largest_item = item
        return largest_item
    def get_total_value(self):
        total = 0
        for item in self.__order_items:
            total += item.product.price * item.quantity
        return total
    
    def get_discount_value(self, discount_rate: float):
        total = self.get_total_value()
        discount = total * discount_rate
        return total - discount
    
    
def main():
    p1 = Product(111, "Hammer", 30.90)
    p2 = Product(222, "Screwdriver", 10.90)
    p3 = Product(333, "Table", 200.99)
    
    c1 = Customer("John Doe", "123 Mission Blvd, Fremont, CA 94539")
    order = Order(123, c1)
    
    order.add_item(p1, 10)
    order.add_item(p2, 20)
    order.add_item(p3, 5)
    
    print(order)
    
    item = order.find_largest_item()
    # if item is None:
    #     print("No item found")
    # else:
    #     print(item)
    
    print("\nAfter removing item 222")
    order.remove_item(222)
    print(order)
    
    print("\nOrder total value:", order.get_total_value())
    print("Order total value with 10% discount:", order.get_discount_value(0.1))
   
if __name__ == "__main__": 
    main()
    
    