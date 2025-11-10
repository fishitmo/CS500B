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
    
    
class CondimentDecorator(Beverage):
    pass


        