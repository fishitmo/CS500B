from abc import ABC, abstractmethod


class Beverage(ABC):
    @abstractmethod
    def get_description(self) -> str:
        pass
    
    @abstractmethod
    def cost(self) -> float:
        pass
    
    def display(self):
        print(f"{self.get_description()}")
        print(f"Total Cost: ${self.cost():.2f}")
        
        
# Create Concrete Components 

class Espresso(Beverage):
    def get_description(self) -> str:
        return "Espresso"
    
    def cost(self) -> float:
        return 1.99
    
class HouseBlend(Beverage):
    def get_description(self) -> str:
        return "House Blend Coffee"
    
    def cost(self) -> float:
        return 0.89
    
    
class DarkRoast(Beverage):
    
    def get_description(self) -> str:
        return "Dark Rost Coffee"
    
    def cost(self)-> float:        
        return 0.99
    
# create the decorator base class
  
class CondimentDecorator(Beverage):
    def __init__(self, beverage: Beverage):
        self.__beverage = beverage
    
    @property
    def beverage(self):
        return self.__beverage
        
    @beverage.setter
    def beverage(self, beverage):
        self.__beverage = beverage
    @abstractmethod
    def get_description(self) -> str:
        pass
    
    
class Milk(CondimentDecorator):
    def get_description(self) -> str:
        return self.beverage.get_description() + ", Milk"
    
    def cost(self) -> float:
        return self.beverage.cost() + 0.50
    
class Mocha(CondimentDecorator):
    def get_description(self) -> str:
        return self.beverage.get_description() + ", Mocha"
    
    def cost(self) -> float:
        return self.beverage.cost() + 0.70
    
class Whip(CondimentDecorator):
    
    def get_description(self) -> str:
        return self.beverage.get_description() + ", Soy"
    
    def cost(self) -> float:
        return self.beverage.cost() + 0.45
    
class Caramel(CondimentDecorator):
    
    def get_description(self) -> str:
        return self.beverage.get_description() + ", Caramel"
    
    def cost(self) -> float:
        return self.beverage.cost() + 0.55
    


def main():
    
    print("\n" + "=" * 50)
    print("Wlcome to the coffee shop!")
    print("=" *50 + "\n")
    
    # order simple Espreso
    print("Order 1: Plain Espresso")
    beverage1 = Espresso()
    beverage1.display()  
    
    # order2 : Dark Roast with Milk and Mocha 
    print("\nOrder 2: Dark Roast with Milk and Mocha")
    beverage2 = DarkRoast()
    beverage2 = Milk(beverage2)
    beverage2 = Mocha(beverage2)
    beverage2.display()
    
if __name__ == "__main__":
    main() 


        