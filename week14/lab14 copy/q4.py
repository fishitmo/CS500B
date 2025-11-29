from abc import ABC, abstractmethod

class OrderProcess(ABC):
    
    def process_order(self):
        
        self.greet_customer()
        self.take_order()
        self.prepare_order()
        self.serve_order()
        
    def greet_customer(self):
        print("Waiter: Good day! Welcome to our restaurant!")
        
    def take_order(self):
        print("Waiter: What would you like to order today?")
        print("Customer: I'll have burger and fries, please.")
        
    def prepare_order(self):
        print("Chef: Preparing your order ...")
        print("Chef: Order is ready!")
        
    @abstractmethod
    def serve_order(self):
        pass
        
        
class DineInOrder(OrderProcess):
    
    def __init__(self, table_number):
        self.__table_number = table_number
        
    def serve_order(self):
        print(f"Waiter: Serving your order at Table #{self.__table_number}")
        print("Waiter: Here are your dishes. Enjoy your meal!")
        
class TakeOutOrder(OrderProcess):
    
    def serve_order(self):
        
        print("Staff: Warpping your order in a bag ..")
        print("Waiter: Here's your take-out order!")
        print("Waiter: Please check if everything is correct.")
 
        
def main():
    
    print("Restaurant Order System")
    
    print("\nDine_In order")
    # Dine_In order
    
    dine_in  = DineInOrder(table_number=5)
    dine_in.process_order()
    
    print("\nTake-Out Order")
    # Take-out Order
    
    takeout = TakeOutOrder()
    takeout.process_order()
    
if __name__ == "__main__":
    main()
            
        