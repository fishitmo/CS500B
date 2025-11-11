from abc import ABC, abstractmethod

# create a pizza base class - abstract class
class Pizza(ABC):
    @abstractmethod
    def get_description(self) -> str:
        pass
    
    @abstractmethod
    def cost(self) -> float:
        pass
    
    def display(self):
        print(f"{self.get_description()}")
        print(f"Toatal Cost: ${self.cost():.2f}")
        

# create concrete pizza class (margarita, Pepperoni, Veggie)

class Margherita(Pizza):
    def get_description(self) -> str:
        return "Margherita"
    
    def cost(self) -> float:
        return 8
    
class Pepperoni(Pizza):
    
    def get_description(self) -> str:
        return "Pepperoni"
    
    def cost(self) -> float:
        return 10
    
class Veggie(Pizza):
    
    def get_description(self) -> str:
        return "Veggie"
    
    def cost(self) -> float:
        return 9
    
# create ToppingDecorator base class

class ToppingDecorator(Pizza):
    def __init__(self, pizza: Pizza):
        self.__pizza = pizza
        
    @property
    def pizza(self):
        return self.__pizza
    
    @pizza.setter
    def pizza(self, pizza: Pizza):
        self.__pizza = pizza
        
    @abstractmethod
    def get_description(self) -> str:
        pass
    

# create concrete topping decorators

class Cheese(ToppingDecorator):
    
    def get_description(self) -> str:
        return self.pizza.get_description() + ", Cheese"
    
    def cost(self) -> float:
        return self.pizza.cost() + 1.50
    
class Olives(ToppingDecorator):
    def get_description(self) -> str:
        return self.pizza.get_description() + ", Olives"
    
    def cost(self)-> float:
        return self.pizza.cost() + 1
    

class Mushrooms(ToppingDecorator):
    
    def get_description(self) -> str:
        return self.pizza.get_description() + ", Mushrooms"
    
    def cost(self) -> float:
        return self.pizza.cost() + 1.25
    

class Bacon(ToppingDecorator):
    
    def get_description(self) -> str:
        return self.pizza.get_description() + ", Bacon"
    
    def cost(self) -> float:
        return self.pizza.cost() + 2.00
    

class Tomatoes(ToppingDecorator):
    
    def get_description(self) -> str:
        return self.pizza.get_description() + ", Tomatoes"
    
    def cost(self) -> float:
        return self.pizza.cost() + 0.75
    

def main():
    
   
    print("\n" + "="*50)
    print("Welcome to Napoli Pizza")
    print("="*50 + "\n")
    # simple pizza
    print("Order 1: Simple pizza Margherita")
    pizza1 = Margherita()
    pizza1.display()
    
    # Order 2: Pepperoni with cheese
    print("\nOrder 2: Pepperoni with Cheese Toping")
    pizza2 = Pepperoni()
    pizza2 = Cheese(pizza2)
    pizza2.display()
    
    # Order 3: Veggie with Olives, Mushroomes and Bacon
    
    print("\n Order 3: Veggie with Olives, Mushrooms and Bacon")
    pizza3 = Veggie()
    pizza3 = Olives(pizza3)
    pizza3 = Mushrooms(pizza3)
    pizza3 = Bacon(pizza3)
    pizza3.display()
    
    
     
    
    
if __name__ == "__main__":
    main()
        
        
