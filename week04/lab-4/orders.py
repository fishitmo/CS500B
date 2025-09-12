class Product:
    def __init__(self, productid: int, product_name: str, price: float)-> None:
        self.__productid = productid
        self.__product_name = product_name
        self.__price = price
        
    def __str__(self) -> str:
        return f"Product id= {self.__productid}, name= {self.__product_name}, price= {self.__price}"
    
    def __repr__(self) -> str:
        return str(self)
    
    def __eq__(self, value: object) -> bool:
        if isinstance(value, Product):
            return value.__productid == self.__productid
        return False    

    @property
    def productid(self) -> int:
        return self.__productid

    @property
    def price(self) -> float:
        return self.__price

    @price.setter
    def price(self, price) -> None:
        self.__price = price
    
   
class Customer:
    def __init__(self, name: str, address: str) -> None:
        self.__name = name
        self.__address = address

    def __str__(self) -> str:
        return f"Customer name= {self.__name}, address= {self.__address}"  

    def __repr__(self) -> str:
        return str(self)

    def __eq__(self, value: object) -> bool:
        if isinstance(value, Customer):
            return value.__name == self.__name
        return False

    @property
    def name(self) -> str:
        return self.__name


class OrderItem:
    def __init__(self, product: Product, quantity: int) -> None:
        self.__product = product
        self.__quantity = quantity

    def __str__(self) -> str:
        return f"Item Product= {self.__product}, quantity= {self.__quantity}"

    def __repr__(self) -> str:
        return str(self)

    def __eq__(self, value: object) -> bool:
        if isinstance(value, OrderItem):
            return value.__product == self.__product
        return False

    @property
    def product(self) -> Product:
        return self.__product

    @property
    def quantity(self) -> int:
        return self.__quantity
    
    @quantity.setter
    def quantity(self, quantity) -> None:
        self.__quantity = quantity
        
class Order:
    
    def __init__(self, oredrid: int, customer: Customer) -> None:
        self.__oredrid = oredrid
        self.__customer = customer
        self.__order_items: list[OrderItem] = []
    
    def __str__(self) -> str:
        output: str = f"Order id= {self.__oredrid}\n"
        output += f"Customer= {self.__customer}\n"
        output += f"Item Product= {self.__order_items}"
        
        return output
        
    def __repr__(self) -> str:
        return str(self)
    
    def add_item(self, product: Product, quantity: int) -> None:
        for item in self.__order_items:
            if item.product == product:
                item.quantity += quantity
                return
        self.__order_items.append(OrderItem(product, quantity)) # Composition
        
    def remove_item(self, productid: int) -> None:
        for item in self.__order_items:
            if item.product.productid == productid:
                self.__order_items.remove(item)
                return
    def remove_item2(self, productid: int) -> None:
        for i in range(len(self.__order_items)):
            if self.__order_items[i].product.productid == productid:
                self.__order_items.pop(i)
                return
    def find_largest_item(self) -> OrderItem | None:
        largest_item: None
        for item in self.__order_items:
            if largest_item is None:
                largest_item = item
            elif item.total_value > largest_item.total_value:
                largest_item = item
        return item
    def get_total_value(self) -> float:
        total_value: float = 0
        for item in self.__order_items:
            total_value += item.total_value
        return total_value
        
def main():
    p1= Product(111, "Hammer", 30.90)
    p2 = Product(222, "Screwdriver", 10.90)
    p3 = Product(333, "Table", 200.99)
    print(p1)
    # products: list[Product] = [p1, p2, p3]
    # print(products)
    # p4 = Product(111, "Hammer", 30.90)
    # if p1 == p4:
    #     print("Equal")
    # else:
    #     print("Not Equal")
    
    c1 = Customer("John Doe", "123 Mission Blvd, Fremont, CA 94539")
    order = Order(123, c1)
    order.add_item(p1, 10)
    order.add_item(p2, 20)
    order.add_item(p3, 5)
    print(order)
    
    item = order.find_largest_item()
    if item is None:
        print("No item found")
    else:
        print(item)
        
    order.remove_item(222)
    print(order)
    
    order.remove_item2(333)
    print(order)
    
    print(order.get_total_value())
    
    
    # c2 = Customer("Jane Doe", "456 Main St, San Francisco, CA 94109")
    # item = OrderItem(p1, 100)
    
    # print(c1)
    # print(item)
    # customers: list[Customer] = [c1, c2]
    # print(customers)
if __name__ == "__main__": 
    main()