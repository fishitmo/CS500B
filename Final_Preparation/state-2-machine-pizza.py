
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
    missing_ingredients = Event(from_states=(SelectPizza), to_state=SelectPizza)
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
        valid_types = set(self.__inventory.keys())
        valid_sizes = set(self.__recipe_size.keys())

        while True:
            pizza_type = input("Select type (Margherita, Pepperoni, Veggie): ").strip().title()
            if pizza_type in valid_types:
                self.__type = pizza_type
                break
            print("Invalid type. Please choose Margherita, Pepperoni, or Veggie.")

        while True:
            size = input("Select size (large, medium, small): ").strip().lower()
            if size in valid_sizes:
                self.__size = size
                break
            print("Invalid size. Please choose large, medium, or small.")

        while True:
            try:
                qty = int(input("Enter quantity: ").strip() or "0")
                if qty > 0:
                    self.__quantity = qty
                    break
                print("Quantity must be greater than zero.")
            except ValueError:
                print("Please enter a whole number for quantity.")
        
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
  








def show_menu():
    print()
    print("====== MENU ======")
    print("1.  Browse Houses")
    print("2. Select House")
    print("2.  Schedule Viewing")
    print("3.  Finish Viewing")
    print("4.  Make Offer")
    print("5.  Counter Offer")
    print("6.  Accept Offer")
    print("7.  Reject Offer")
    print("8.  Apply Counter Offer")
    print("9.  Apply for Pre-Approval")
    print("10. Evaluate Loan Application")
    print("11. Disapprove Loan")
    print("12. Inspect House")
    print("13. Sign Closing Documents")
    print("14. Receive House Keys")
    print("15. Go Back to Browse")
    print("16. Show Current State")
    print("17. Exit")


def main():
    

    real_estate = RealEstate()

    while True:
        show_menu()

        try:
            choice = input("\nEnter your choice (1-17): ").strip()

            if choice == "1":
                real_estate.get_house_details()

            elif choice == "2":
                real_estate.schedule_viewing()

            elif choice == "3":
                real_estate.finish_viewing()

            elif choice == "4":
                real_estate.make_offer()

            elif choice == "5":
                real_estate.counter_offer()

            elif choice == "6":
                real_estate.accepted_offer()

            elif choice == "7":
                real_estate.rejected_offer()

            elif choice == "8":
                real_estate.apply_counter_offer()

            elif choice == "9":
                real_estate.apply_accepted_offer()

            elif choice == "10":
                real_estate.evaluate_loan()

            elif choice == "11":
                real_estate.disapprove_loan()

            elif choice == "12":
                real_estate.inspect_house()

            elif choice == "13":
                real_estate.sign_closing_documents()

            elif choice == "14":
                real_estate.receive_house_keys()
                print("\n🎉 Congratulations on your new home! 🎉")

            elif choice == "15":
                real_estate.list_houses()

            elif choice == "16":
                print(f"\nCurrent State: {real_estate.get_current_state()}")
                print(f"Selected House: {real_estate.get_house_summary()}")

            elif choice == "17":
                print("\nThank you for using the Real Estate House Buying System!")
                print("Goodbye!")
                break

            else:
                print("\n⚠ Invalid choice. Please enter a number between 1 and 17.")

        except InvalidStateTransition as e:
            print(f"\n✗ Invalid transition: Cannot perform this action in the current state ({real_estate.get_current_state()})")
            print("Please follow the proper sequence of the house buying process.")

        except Exception as e:
            print(f"\n✗ An error occurred: {str(e)}")


if __name__ == "__main__":
    main()
