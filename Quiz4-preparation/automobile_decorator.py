
import enum
from abc import ABC, abstractmethod

class Automobile(ABC):
    @abstractmethod
    def description(self):
        pass
    
    @abstractmethod
    def price(self):
        pass
    
    def display(self):
        print(self.description() + ",$"+ str(self.price()))
        
class Sedan(Automobile):
    
    @property
    def price(self):
        return 20000
    
    @property
    def description(self):
        return "Passenger Car"
    
class Truck(Automobile):
    
    @property
    def price(self):
        return 25000
    
    @property
    def description(self):
        return "Cargo Vehicle"
    
    
class OptionDecorator(Automobile):
    
    def __init__(self):
        self.__automobile = None
    
    @property
    def automobile(self):
        return self.__automobile
    @automobile.setter
    def automobile(self, automobile: Automobile):
        self.__automobile = automobile
        
        
class Sunroof(OptionDecorator):
    
    def __init__(self, automobile: Automobile):
        self.automobile = automobile
        
    @property
    def description(self):
        return self.automobile.description + ", Sun Roof"
    @property
    def price(self):
        return 1000 + self.automobile.price

class Security(OptionDecorator):
    def __init__(self, automobile: Automobile):
        self.automobile = automobile
        
    @property
    def description(self):
        return self.automobile.description + ", Advanced Security System"
    
    @property
    def price(self):
        return 800 + self.automobile.price
    
class Saftey(OptionDecorator):
    def __init__(self, automobile: Automobile):
        self.automobile = automobile
        
    @property
    def price(self):
        return 500 + self.automobile.price
    
    @property
    def description(self):
        return self.automobile.description + ", Advanced Safety Features"
    
    
    
def main():
    auto1 = Sedan()
    auto1.display()
    
    auto2 = Sedan()
    auto2 = Sunroof(auto2)
    auto2 = Saftey(auto2)
    auto2 = Security(auto2)
    auto2.display()
    
    auto3 = Security(Saftey(Sunroof(Truck())))
    auto3.display()
    
if __name__ == "__main__":
    main()