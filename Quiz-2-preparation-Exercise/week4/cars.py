class Engine:
    def __init__(self, horspower: int):
        self.__horespower = horspower
        
    def __str__(self):
        return f"Engine: horsepower= {self.__horespower}"
    
class Tire:
    def __init__(self, size: int):
        self.__size = size
        
    def __str__(self):
        return f"Tire: size= {self.__size}"
    
    def __repr__(self):
        return str(self)
    
    
class Car:
    def __init__(self, name: str, horsepower: int):
        self.__name = name
        self.__engine = Engine(horsepower)
        self.__tires = []
        
    def add_tire(self, tire: Tire):
        self.__tires.append(tire)
        
    def __str__(self):
        return f"Car: {self.__name}, {self.__engine}, {self.__tires}"
    
def main():
    c = Car("Toyota", 400)
    c.add_tire(Tire(20))
    c.add_tire(Tire(20))
    c.add_tire(Tire(20))
    c.add_tire(Tire(20))
    print(c)
    
if __name__ == "__main__":
    main() 