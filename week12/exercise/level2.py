from abc import ABC, abstractmethod

class Pizza(ABC):
    
    def __init__(self):
        self.name =""
        
    def prepare(self):
        print(f"Preparing {self.name}")
        
    def bake(self):
        print(f"Baking {self.name}")
        
    def cut(self):
        print(f"Cutting {self.name}")
        
        
class NYCheesePizza(Pizza):
    def __init__(self):
      super().__init__()
      self.name = "NY Style Pepperoni Pizza"
      
class NYPepperoniPizza(Pizza):
    def __init__(self):
        super().__init__()
        self.name = "NY Style Pepperoni Pizza"

# Chicago Style Pizzas
class ChicagoCheesePizza(Pizza):
    def __init__(self):
        super().__init__()
        self.name = "Chicago Deep Dish Cheese Pizza"

class ChicagoPepperoniPizza(Pizza):
    def __init__(self):
        super().__init__()
        self.name = "Chicago Deep Dish Pepperoni Pizza"

# FACTORY METHOD PATTERN
# Abstract Creator
class PizzaStore(ABC):
    def order_pizza(self, pizza_type):
        # Use factory method to create pizza
        pizza = self.create_pizza(pizza_type)
        
        pizza.prepare()
        pizza.bake()
        pizza.cut()
        return pizza
    
    @abstractmethod
    def create_pizza(self, pizza_type):
        """Factory Method - subclasses implement this"""
        pass

# Concrete Creators
class NYPizzaStore(PizzaStore):
    def create_pizza(self, pizza_type):
        if pizza_type == "cheese":
            return NYCheesePizza()
        elif pizza_type == "pepperoni":
            return NYPepperoniPizza()

class ChicagoPizzaStore(PizzaStore):
    def create_pizza(self, pizza_type):
        if pizza_type == "cheese":
            return ChicagoCheesePizza()
        elif pizza_type == "pepperoni":
            return ChicagoPepperoniPizza()


def main():
   ny_store = NYPizzaStore()
   chicago_store = ChicagoPizzaStore()

   ny_store.order_pizza("cheese")      # Creates NY Style
   chicago_store.order_pizza("cheese")  # Creates Chicago Style   
    
    
if __name__ == "__main__":
    main()

