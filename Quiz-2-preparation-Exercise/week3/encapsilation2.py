class Apple:
    def __init__(self, color: str, weight: float, price: float):
        self.__color = color
        self.__weight = weight
        self.__price = price
        
    @property
    def color(self):
        return self.__color
    
    @color.setter
    def color(self, color):
        self.__color = color
        
    @property
    def weight(self):
        return self.__weight    
    
    @weight.setter
    def weight(self, weight):
        self.__weight = weight    
        
    @property
    def price(self):
        return self.__price    
        
    @price.setter
    def price(self, price):
        self.__price = price        
        
    def __str__(self):
        return f"Color: {self.__color}, Weight: {self.__weight}, Price: {self.__price}"

def main():
    apple = Apple("Red", 0.5, 1.0)
    print(apple)
    apple.color = "Green"
    apple.weight = 0.7
    apple.price = 1.5
    print(apple)
    
if __name__ == "__main__":
    main()