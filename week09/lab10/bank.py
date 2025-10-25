
from customer import Customer
from customer_repository import CustomerRepository
class Bank:
    
    def __init__(self, bank_name: str) -> None:
        self.__bank_name = bank_name
        self.__customers: list[Customer] = []
        
    def load_cutomers(self) -> None:
        repos = CustomerRepository()
        customers = repos.read_customers()
        for customer in customers:
            self.__customers.append(customer)
            
    def display_customers(self) -> None:
        for customer in self.__customers:
            print(customer)
            
def main():
    bank = Bank("SFBU Bank")
    bank.load_cutomers()
    bank.display_customers()

if __name__ == "__main__":
    main()