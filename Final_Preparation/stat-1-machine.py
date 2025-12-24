
from __future__ import annotations
from state_machine import (State, Event, acts_as_state_machine,
after, before, InvalidStateTransition)

@acts_as_state_machine
class OrderProcess:
    
    # define 7 states
    Checkout = State(initial=True)
    SelectPizza = State()
    PlaceOrder = State()
    PreparingOrder = State()
    MakingPizza = State()
    ReadyForPickupOrder = State()
    CompleatedOrder = State()
    
    # define 
    select_pizza = Event(from_states=(Checkout), to_state=SelectPizza)
    cancel_order = Event(from_states=(SelectPizza, PlaceOrder), to_state= Checkout)
    check_ingredients = Event(from_states=(SelectPizza), to_state=PlaceOrder)
    missing_ingredients = Event(from_states=(PlaceOrder), to_state=SelectPizza)
    prepare_order = Event(from_states=(PlaceOrder), to_state=PreparingOrder)
    making_pizza = Event(from_states=(PreparingOrder), to_state=MakingPizza)
    pizza_baked = Event(from_states=(MakingPizza), to_state=ReadyForPickupOrder)
    pick_up_order = Event(from_states=(ReadyForPickupOrder), to_state=CompleatedOrder)
    ready_for_new_order = Event(from_states=(CompleatedOrder), to_state=Checkout)
    
    def __init__(self, store: PizzaStore) -> None:
        self.__store = store
        
    @before("select_pizza")
    def before_select_pizza(self):
        self.__store.choose_pizza()
    @after("select_pizza")
    def after_select_pizza(self):
        print("Pizza has been selected!")
    @after("cancel_order")
    def after_cancel_order(self):
        print("Wait for customers")
        # self.__store.clear_order()
    @before("check_ingredients")
    def before_check_ingredients(self):
        return self.__store.is_enough_ingredients()
    
    @after("check_ingredients")
    def after_check_ingredients(self):
        print("Order has been placed!")
    
    @after("prepare_order")
    def after_prepare_order(self):
        print("preparing dough and ingredients")
        
    @after("making_pizza")
    def after_making_pizza(self):
        print("baking pizza in the oven")
        
    @after("pizza_baked")
    def after_pizza_baked(self):
        print("Wait for the customer to pick up")
        
    @after("pick_up_order")
    def after_pick_up_order(self):
        print("customer picked up the order!")
    
    @after("ready_for_new_order")
    def after_ready_for_new_order(self):
        print("Wait for customers")
        
class PizzaStore:
    def __init__(self) -> None:
        self.__process = OrderProcess(self)
        self.__type = ""
        self.__size = ""
        self.__quantity = 0 
        self.__inventory = {"Margherita": 10, "Pepperoni": 4, "Veggie": 2}
        self.__recipe_size = {"large": 2, "medium": 1, "small": 0.5}
    
    
    def choose_pizza(self):
        self.__type = input("Select type: Margharieta, Peperoni or Veggie:")
        self.__size = input("Select size: large, medium or small:")
        self.__quantity = int(input("Enter quantity: "))
        
    def is_enough_ingredients(self):
        return self.__inventory[self.__type] > self.__recipe_size[self.__size]
    
    def check_ingredients(self):
        self.__process.check_ingredients()       
        
    def prepare_order(self):
        self.__process.prepare_order()
     
    def making_pizza(self):
        self.__process.making_pizza()
    
    def pizza_baked(self):
        self.__process.pizza_baked()
        
    def pick_up_order(self):
        self.__process.pick_up_order()
        
    def ready_for_new_order(self):
        self.__process.ready_for_new_order()
        
    def get_current_state(self):
        return self.__process.current_state
    
    
def show_menu():
    print()
    print("====== MENU ======")
    print("1. Select Pizza")
    print("2. Check Ingredients")
    print("3. Prepare Order")
    print("4. Make Pizza")
    print("5. Bake Pizza")
    print("6. Pick Up Order")
    print("7. Ready for New Order")
    print("8. Cancel Order")
    print("9. Exit")
def main():
    store = PizzaStore()
    while True:
        show_menu()
        choice = int(input("Enter your choice: "))
        try:
            if choice == 1:
                store.choose_pizza()
                store.select_pizza()
            elif choice == 2:
                store.check_ingredients()
            elif choice == 3:
                pass
            elif choice == 4:
                pass
            elif choice == 5:
                pass
            elif choice == 6:
                pass
            elif choice == 7:
                pass
            elif choice == 8:
                pass
            elif choice == 9:
                break
        except InvalidStateTransition as err:
            print(f"Could not perform {choice} in {store.get_current_state()} state")
if __name__ == "__main__":
  main()
  