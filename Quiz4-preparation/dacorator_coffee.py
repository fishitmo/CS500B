from abc import ABC, abstractmethod

class Cofee(ABC):
    
    @abstractmethod
    def cost(self) -> float:
        pass
    
    @abstractmethod
    def description(self) -> str:
        pass
    
class SimpleCofee(Cofee):
    
    def cost(self) -> float:
        return 2.0
    
    def description(self) -> str:
        return "Simple Cofee"
    
class CofeeDecorator(Cofee):
    
    def __init__(self, cofee: Cofee)->None:
        
        self.__cofee = cofee
        
    def cost(self):
        return self.__cofee.cost()
    
    def description(self)-> str:
        return self.__cofee.description()
    
class Milk(CofeeDecorator):
    
    def cost(self):
        return super().cost() + 1.5
    
    def description(self) -> str:
        return super().description() + ', Milk'
    
class Whip(CofeeDecorator):
    
    def cost(self):
        return super().cost() + 0.5
    
    def description(self) -> str:
        return super().description() + ", whipe"
    
def main():
    
    cofee1 = Whip(Milk(SimpleCofee()))
    print(cofee1.cost())
    print(cofee1.description())
    

if __name__ =="__main__":
    main()
        