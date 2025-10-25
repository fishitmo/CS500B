from bank import Bank



class BankApp:
    
    def __init__(self, bank_name: str) -> None:
        self.__bank = Bank(bank_name)
        self.__bank.load_cutomers()
        
        
    def show_menu(self) -> None:
        print("=== Menu ===")
        print("1: Add new customer")
        print("2: Display Customers")
        
        
        
        print("7: Exit")
        
        
    def runapp(self) -> None:
        while True:
            self.show_menu()
            choice = int(input("Enter your choice: "))
            
            if choice == 1:
                pass
            
            elif choice == 2:
                self.__bank.display_customers()
                
            elif choice == 7:
                print("Bye")
                break
            

if __name__ == "__main__":
    app = BankApp("SFBU Bank")
    app.runapp()