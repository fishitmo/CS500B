class Product:
    def __init__(self, product_name ="", price = 0.0, rebate = 0.0, warranty = 1):
        self.__product_name = product_name
        self.__price = price
        self.__rebate = rebate
        self.__warranty = warranty
    
    def display(self):
        print("Product Name:", self.__product_name)
        print("Price:", self.__price)
        print("Rebate:", self.__rebate)
        print("Warranty:", self.__warranty)
        
class Computer(Product):
    def __init__(self, computer_type, product_name = "", price = 0.0, rebate = 0.0, warranty =1):
        super().__init__(product_name, price, rebate, warranty)
        self.__computer_type = computer_type
    def display(self):
        super().display()
        print("Computer Type:", self.__computer_type)

class Car(Product):
    def __init__(self, horsepower, product_name = "", price = 0.0, rebate = 0.0, warranty = 1):
        Product.__init__(self,product_name, price, rebate, warranty)
        self.__horsepower = horsepower
        
    def display(self):
        super().display()
        print("Horsepower:", self.__horsepower)
        
def main():
    
    
    products = []
    products.append(Computer("Desktop", "Product 1", 1000, 100, 2))
    products.append(Car(300.0, "Product 2", 50000.00, 0.5, 5))
    
    for product in products:
        product.display()
        
        print()
        
    
    
# def display_product(product):
#     print("PRODUCT DATA")
#     print("Product Name:", product.product_name)
#     if isinstance(product,  Computer):
#         print("Computer Type:", product.computer_type)
#     if isinstance(product, Car):
#         print("Horsepower:", product.horsepower)
#     print("Best price:   {:.2f}".format(product.calculate_price()))
#     print()       
        
if __name__ == "__main__":
    main()
    
