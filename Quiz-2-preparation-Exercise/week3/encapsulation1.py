class Apple:
    def __init__(self, color, weight, price):
        self.__color = color
        self.__weight = weight
        self.__price = price
        
    def set_price(self, price):
        self.__price = price
        
    def get_price(self):
        return self.__price
    
    def set_weight(self, weight):
        self.__weight = weight
        
    def get_weight(self):
        return self.__weight
    
    def set_color(self, color):
        self.__color = color
        
    def get_color(self):
        return self.__color
    
    def __str__(self):
        return f"Color: {self.__color}, Weight: {self.__weight}, Price: {self.__price}"
    
    
    
def main():
    
    a1 = Apple("Green", 0.4, 2.5)
    a2 = Apple("Yellow", 0.8, 2.9)
    a3 = Apple("Red", 0.2, 1.9)
    
    print("a1=", str(a1))
    
    print("\nAfter changing the price")
    a1.set_price(2.8)
    print("a1=", str(a1))

if __name__ == "__main__":
    main()