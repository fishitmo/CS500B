# class Animal:
#     def __init__(self, name):
#         self.name = name
        
#     def make_sound(self):
#         print("The animal makes a sound.")
        
#     def eat(self):
#         print(f"{self.name} is eating.")
        
# class Dog(Animal):
#     pass


# dog = Dog("Fido")
# dog.make_sound()
# dog.eat()


class Vehicle:
    def __init__(self, brand):
        self.brand = brand
        
        
    def start(self):
        print(f"{self.brand} is starting.")
        
    def stop(self):
        print(f"{self.brand} is stopping.")
        
        
class Car(Vehicle):
    def start(self):
        print(f"{self.brand} car engine is starting.")
        
        
class ElectricCar(Car):
    def start(self):
        print(f"{self.brand} electric motor starting silently .")
        


vehicle = Vehicle("Generic")
vehicle.start()


car = Car("Toyota")
car.start()
car.stop()


electric = ElectricCar("Tesla")
electric.start()
electric.stop()







