class Engine:
    def __init__(self, horsepower: int):
        self.__horsepower = horsepower
        
    def __str__(self):
        return f"Engine: horsepower= {self.__horsepower}"
    
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
        # for composttion, the engine object should be created inside the car
        self.__engine = Engine(horsepower)
        # for aggregation, we create a platform that holds tires
        self.__tires = []
    
    def add_tire(self, tire: Tire):
        self.__tires.append(tire)
    
    def __str__(self):
        return f"Car: name= {self.__name}, engine= {self.__engine}, tires= {self.__tires}"
    
def main():
    c = Car("Toyota", 400)
    c.add_tire(Tire(21))
    c.add_tire(Tire(21))
    c.add_tire(Tire(21))
    print(c)
    

if __name__ == "__main__":
    main()