class Product:
    def __init__(self, product_name = "", price = 0.0 , rebate = 0.0,  warranty = 1):
        self.__product_name = product_name
        self.__price = price
        self.__rebate = rebate
        self.__warranty = warranty
        
    def display(self):
        print("Product name: ", self.__product_name)
        print("Price:", self.__price)
        print("Rebate: ", self.__rebate)
        print("Warranty: ", self.__warranty)

class Computer(Product):
    def __init__(self, computer_type, product_name = "", price = 0.0 , rebate = 0.0, warranty = 1):
        super().__init__(product_name, price, rebate, warranty)
        self.__computer_type = computer_type
        
    def display(self):
        super().display()
        print("Computer type: ", self.__computer_type)
        
class Car(Product):
    def __init__(self, horsepower, product_name = "", price = 0.0 , rebate = 0.0, warranty = 1):
        Product.__init__(self, product_name, price, rebate, warranty)
        self.__horsepower = horsepower
        
    def display(self):
        super().display()
        print("Horsepower:", self.__horsepower)

def main():
    '''
    Polymorphism is a feature of inheritance that lets you treat objects of subclasses as 
    if they were objects of the superclass.
    
    if you access a method of a superclass objects and the method is overridden in the subclasses
    of the class, polymorphism determines which method is executed based on the objects type
    '''
    products = []
    products.append(Computer("Desktop", "Computer", 1000.00, 12.5, 2))
    products.append(Car(300.0, "Car", 50000.00, 15.0, 5))
    
    # def display_product(product):
    #     print("PRODUCT DATA")
    #     print("Product Name: ", product._Product__product_name)
    #     if isinstance(product, Computer):
    #         print("Computer Type: ", product._Computer__computer_type)
    #     if isinstance(product, Car):
    #         print("Horsepower: ", product._Car__horsepower)
    #     # print("Best price: {:.2f}".format(product.calculate_price()))
    #     print()
    
    for product in products:
        product.display()
        # display_product(product)
        print()

if __name__ == "__main__":
    main()
    
