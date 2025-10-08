class Barrel:
    def __init__(self, capacity):
        self.__list = []
        self.__capacity = capacity
        
    @property
    def list(self):
        return self.__list
    
    @property
    def capacity(self):
        return self.__capacity
    
    def get_total_weight(self):
        total_weight = 0
        for apple in self.list:
            total_weight += apple.weight
        return total_weight
    
    def add_apple(self, apple):
        # check if it is over weight
        if self.get_total_weight() + apple.weight > self.capacity:
            print("Error! Total weight exceeds the capacity.")
            return False
            
        self.list.append(apple)
        return True
    
    def __str__(self):
        output = f"Capacity: {self.__capacity}\n"
        for apple in self.__list:
            output += str(apple) + '\n'
        return output
    
    
        