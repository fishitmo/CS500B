class Apple:
    def __init__(self, type, weight, price):
        self.__type = type
        self.__weight = weight
        self.__price = price
        
    @property
    def price(self):
        return self.__price
    
    @price.setter
    def price(self, price):
        if price < 0:
            raise ValueError('Apple price must be greater than zero,')
        else:
            self.__price = price
            
    @property
    def weight(self):
        return self.__weight
    
    @property
    def type(self):
        return self.__type
    
    def __str__(self):
        return f"Type: {self.__type}, Weight: {self.__weight}, Price: {self.__price}"
    
    