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
        if price < 0.0:
            raise ValueError("Apple Price must be greater than zero")
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
    
    
    
class Barrel:
    
    def __init__(self, capacity):
        self.__list = []
        self.__capacity = capacity
        
    @property
    def capacity(self):
        return self.__capacity
    
    def get_total_weight(self):
        totalWeight = 0.0
        for apple in self.__list:
            totalWeight += apple.weight
            
        return totalWeight
    
    def add_apple(self, apple):
        # check if it is overweight
        if self.get_total_weight() + apple.weight > self.capacity:
            print('Error! Totol weight exceeds the capacity.')
            return False
        self.list.append(apple)
        return True
    
    def __str__(self):
        output = f"Capacity: {self.capacity}\n"
        for apple in self.list:
            output += str(apple) + '\n'
        return output       
        
