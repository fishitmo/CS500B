from abc import ABC , abstractmethod

class Pizza(ABC):
    
    def __init__(self):
        self.name = ""
        self.dough = ""
        self.sauce = ""
        
    def prepare(self):
        print(f"Preparing {self.name}")
        
    def bake(self):
        print(f"Baking {self.name}")
        
    def cut(self):
        print(f"Cutting {self.name}")
        
class CheesePizza(Pizza):
    def __init__(self):
        super().__init__()
        self.name = "Cheese Pizza"
        self.dough = "Regular Crust"
        self.sauce = "Marinara"
        
        
class PepperoniPizza(Pizza):
    def __init__(self):
        super().__init__()
        self.name = "Pepperoni Pizza"
        self.dough = "Thin Crust"
        self.sauce = "Marinara"
        
class VeggiePizza(Pizza):
    def __inti__(self):
        super().__init__()
        self.name = "Veggie Pizza"
        self.dough = "Thick Crust"
        self.sauce = "Tomato Basil"
        
class SimplePizzaFactory:
    def create_pizza(self, pizza_type):
        pizza = None
        
        if pizza_type == "cheese":
           pizza = CheesePizza()
           
        if pizza_type == "pepperoni":
            pizza = PepperoniPizza()
            
        elif pizza_type == "veggie":
            
            pizza = VeggiePizza()
            
        return pizza
    
class PizzaStore:
    
    def __init__(self):
        self.factory = SimplePizzaFactory()
        
    def order_pizza(self, pizza_type):
        
        pizza = self.factory.create_pizza(pizza_type)
        
        pizza.prepare()
        pizza.bake()
        pizza.cut()
        return pizza
    
def main():
    store = PizzaStore()
    store.order_pizza("cheese")

if __name__ == "__main__":
    main()
                
        