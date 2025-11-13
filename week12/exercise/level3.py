from abc import ABC, abstractmethod

# ===== INGREDIENT FAMILIES =====
# Dough Family
class Dough(ABC):
    pass

class ThinCrustDough(Dough):
    def __str__(self):
        return "Thin Crust Dough"

class ThickCrustDough(Dough):
    def __str__(self):
        return "Thick Crust Dough"

# Sauce Family
class Sauce(ABC):
    pass

class MarinaraSauce(Sauce):
    def __str__(self):
        return "Marinara Sauce"

class PlumTomatoSauce(Sauce):
    def __str__(self):
        return "Plum Tomato Sauce"

# Cheese Family
class Cheese(ABC):
    pass

class MozzarellaCheese(Cheese):
    def __str__(self):
        return "Mozzarella Cheese"

class ParmesanCheese(Cheese):
    def __str__(self):
        return "Parmesan Cheese"

# ⭐ ABSTRACT FACTORY - Creates ingredient families
class PizzaIngredientFactory(ABC):
    @abstractmethod
    def create_dough(self):
        pass
    
    @abstractmethod
    def create_sauce(self):
        pass
    
    @abstractmethod
    def create_cheese(self):
        pass

# NY Ingredient Factory
class NYPizzaIngredientFactory(PizzaIngredientFactory):
    def create_dough(self):
        return ThinCrustDough()
    
    def create_sauce(self):
        return MarinaraSauce()
    
    def create_cheese(self):
        return MozzarellaCheese()

# Chicago Ingredient Factory
class ChicagoPizzaIngredientFactory(PizzaIngredientFactory):
    def create_dough(self):
        return ThickCrustDough()
    
    def create_sauce(self):
        return PlumTomatoSauce()
    
    def create_cheese(self):
        return ParmesanCheese()

# Pizza using ingredients
class Pizza(ABC):
    def __init__(self, name, ingredient_factory):
        self.name = name
        self.ingredient_factory = ingredient_factory
        self.dough = None
        self.sauce = None
        self.cheese = None
    
    def prepare(self):
        print(f"Preparing {self.name}")
        self.dough = self.ingredient_factory.create_dough()
        self.sauce = self.ingredient_factory.create_sauce()
        self.cheese = self.ingredient_factory.create_cheese()
        print(f"  Adding {self.dough}")
        print(f"  Adding {self.sauce}")
        print(f"  Adding {self.cheese}")

class CheesePizza(Pizza):
    def __init__(self, ingredient_factory):
        super().__init__("Cheese Pizza", ingredient_factory)

# Store
class PizzaStore(ABC):
    def order_pizza(self, pizza_type):
        pizza = self.create_pizza(pizza_type)
        pizza.prepare()
        return pizza
    
    @abstractmethod
    def create_pizza(self, pizza_type):
        pass

class NYPizzaStore(PizzaStore):
    def create_pizza(self, pizza_type):
        ingredient_factory = NYPizzaIngredientFactory()
        if pizza_type == "cheese":
            return CheesePizza(ingredient_factory)

class ChicagoPizzaStore(PizzaStore):
    def create_pizza(self, pizza_type):
        ingredient_factory = ChicagoPizzaIngredientFactory()
        if pizza_type == "cheese":
            return CheesePizza(ingredient_factory)
def main():
        # Usage
    ny_store = NYPizzaStore()
    ny_store.order_pizza("cheese")


    chicago_store = ChicagoPizzaStore()
    chicago_store.order_pizza("cheese")
    
if __name__ =="__main__":
    main()