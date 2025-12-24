from __future__ import annotations


from state_machine import (State, Event, acts_as_state_machine,
                           after, before, InvalidStateTransition)


@acts_as_state_machine
class OrderProcess:
    # define 7 states
    CheckOut = State(initial=True)
    SelectPizza = State()
    PlaceOrder = State()
    PreparingOrder = State()
    MakingPizza = State()
    ReadyForPickupOrder = State()
    CompletedOrder = State()


    # define 8 events

    select_pizza = Event(from_states=(CheckOut), to_state=SelectPizza)
    cancel_order = Event(from_states=(SelectPizza, PlaceOrder), to_state=CheckOut)
    check_ingredients = Event(from_states=(SelectPizza), to_state=PlaceOrder)
    missing_ingredients = Event(from_states=(SelectPizza), to_state=SelectPizza)
    prepare_order = Event(from_states=(PlaceOrder), to_state=PreparingOrder)
    making_pizza = Event(from_states=(PreparingOrder), to_state=MakingPizza)
    pizza_baked = Event(from_states=(MakingPizza), to_state=ReadyForPickupOrder)
    pick_up_order = Event(from_states=(ReadyForPickupOrder), to_state=CompletedOrder)
    ready_for_new_order = Event(from_states=(CompletedOrder), to_state=CheckOut)
    
    
    def __init__(self, store: PizzaStore) -> None:
        self.__store = store
    
    @before("select_pizza")
    def before_select_pizza(self):
        self.__store.choose_pizza()
    @after("select_pizza")
    def after_select_pizza(self):
        print("Pizza has been selected!")
    @before("check_ingredients")
    def before_check_ingredients(self):
        return self.__store.is_enough_ingredients()
    
    @after("check_ingredients")
    def after_check_ingredients(self):
        print("Order has been placed!")
        
    @after("missing_ingredients")
    def after_missing_ingredients(self):
        print("Not enough ingredients,please select a different pizza.")
    
    @after("cancel_order")
    def after_cancel_order(self):
        print("Order cancelled!")
        self.__store.clear_order()
    
    @after("prepare_order")
    def after_prepare_order(self):
        print("Preparing your order...")
    
    @after("making_pizza")
    def after_making_pizza(self):
        print("Making pizza in the oven...")
    
    @after("pizza_baked")
    def after_pizza_baked(self):
        print("Pizza is ready for pickup!")
    
    @after("pick_up_order")
    def after_pick_up_order(self):
        print("Customer picked up the order!")
    
    @after("ready_for_new_order")
    def after_ready_for_new_order(self):
        print("Ready for new customer!")



    
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
        self.__type = input("Select size: large, medium or small:")
        self.__quantity = int(input("Enter quantity: "))
        
    def is_enough_ingredients(self):
        # return self.__inventory[self.__type] > self.__recipe_size[self.__size]
        
        if self.__type not in self.__inventory:
            return False
        if self.__size not in self.__recipe_size:
            return False
        
        required = self.__recipe_size[self.__size] * self.__quantity
        available = self.__inventory[self.__type]
        
        return available >= required  
    
    def deduct_inventory(self):
      
        required = self.__recipe_size[self.__size] * self.__quantity
        self.__inventory[self.__type] -= required
        print(f"deducted {required}  of {self.__type} from inventory")
    
    def clear_order(self):
        
        self.__type = ""
        self.__size = ""
        self.__quantity = 0
    
    def show_inventory(self):
       
        for pizza_type, amount in self.__inventory.items():
            print(f"{pizza_type}: {amount} ")
        
    
    def get_order_summary(self):
        
        if self.__type:
            return f"{self.__quantity}* {self.__size} {self.__type}"
        return "No active order"
        
    def select_pizza(self):
        self.__process.select_pizza()
    def check_ingredients(self):
        # self.__process.check_ingredients()
        
        if self.is_enough_ingredients():
            self.__process.check_ingredients()
        else:
            self.__process.missing_ingredients()
            
    def cancel_order(self):
        self.__process.cancel_order()
    
    def prepare_order(self):
        self.__process.prepare_order()
    
    def make_pizza(self):
        self.__process.making_pizza()
    
    def bake_pizza(self):
        self.__process.pizza_baked()
    
    def pickup_order(self):
        self.__process.pick_up_order()
    
    def reset_for_new_order(self):
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
    print("7. Reset for New Order")
    print("8. Cancel Order")
    print("9. Show Inventory")
    print("10. Show Current State")
    print("11. Exit")
def main():
    store = PizzaStore()
    while True:
        show_menu()
        choice = int(input("Enter your choice: "))
        try:
            if choice == 1:
                store.select_pizza()
            elif choice == 2:
                store.check_ingredients()
            elif choice == 3:
                print(f"Current State: {store.get_current_state()}")
                store.prepare_order()
                
            elif choice == 4:
                print(f"Current State: {store.get_current_state()}")
                store.make_pizza()
                
            elif choice == 5:
                print(f"Current State: {store.get_current_state()}")
                store.bake_pizza()
                
            elif choice == 6:
                print(f"Current State: {store.get_current_state()}")
                store.pickup_order()
                
            elif choice == 7:
                print(f"Current State: {store.get_current_state()}")
                store.reset_for_new_order()
                
            elif choice == 8:
                print(f"Current State: {store.get_current_state()}")
                store.cancel_order()
                
            elif choice == 9:
                store.show_inventory()
                
            elif choice == 10:
                print(f"\nCurrent State: {store.get_current_state()}")
                print(f"Order: {store.get_order_summary()}")
                
            elif choice == 11:
                print("Thank you for using Pizza Store!")
                break
            else:
                print("Invalid choice. Please enter 1-11.")
        except InvalidStateTransition as err:
            print(f"Could not perform {choice} in {store.get_current_state()} state")
            
            
    
if __name__ == "__main__":
  main()
  
    
   
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
