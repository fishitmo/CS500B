from abc import ABC, abstractmethod

class Product(ABC):
    
    def make(self, type):
        return "is making a product" + type
    
    def getName(self):
        pass
    
class ProductA(Product):
    
    def getName(self):
        return "Product A"
    
class ProductB(Product):
    
    def getName(self):
        return "Product B"
    
class BasicFactory:
    
    def createProduct(self, type):
        
        product = ""
        
        if type == "A":
            product = ProductA()
        if type == "B":
            product = ProductB()
        
        return product
class StoreX:
    
    def order(self, customer ,type):
        
        factory = BasicFactory()
        product = factory.createProduct(type)
        print("StoreX", product.make(type))
        print(customer, "ordered", product.getName(), "from Store X")
        return product
    
class StoreY:
    def order(self,  customer, type):
        factory = BasicFactory()
        product = factory.createProduct(type)
        print("Store Y", product.make(type))
        print(customer, "ordered", product.getName(), "from Store Y")
        return product
    

def main():
    
   print("Enter a product type: ")
   type = input()
   store1 = StoreX()
   store1.order("Peter", type)

if __name__ == "__main__":
    main()
        