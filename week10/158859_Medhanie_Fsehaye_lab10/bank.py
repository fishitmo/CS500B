
from customer import Customer
from customer_repository import CustomerRepository


class Bank:
    def __init__(self, bank_name: str) -> None:
        self.__bank_name = bank_name

        self.__customers: list[Customer] = []

    @property
    def bank_name(self) -> str:
        return self.__bank_name

    def load_customers(self) -> None:
        repo = CustomerRepository()
        customers = repo.read_customers()
        for customer in customers:
            self.__customers.append(customer)

    def save_customers(self) -> None:
        repo = CustomerRepository()
        repo.save_customers(self.__customers)

    def display_customers(self) -> None:
        for customer in self.__customers:
            print(customer)

    def add_customer(self, customer: Customer) -> None:
        self.__customers.append(customer)

        self.save_customers()

    def search_customer(self, last_name: str, first_name: str) -> Customer | None:
        for customer in self.__customers:
            if customer.lastname == last_name and customer.firstname == first_name:
                return customer
        return None

    def update_customer(self, customer: Customer, last_name: str | None, first_name: str | None, address: str | None, balance: float | None) -> None:
        if last_name is not None:
            customer.lastname = last_name
        if first_name is not None:
            customer.firstname = first_name
        if address is not None:
            customer.address = address
        if balance is not None:
            customer.balance = balance

        self.save_customers()

    def delete_customer(self, last_name: str, first_name: str) -> None:
        customer = self.search_customer(last_name, first_name)
        if customer is None:
            print("Customer not found")
            return

        self.__customers.remove(customer)

        self.save_customers()

    def find_negative_balances(self) -> list[Customer]:
        negative_balances = []
        for customer in self.__customers:
            if customer.balance < 0:
                negative_balances.append(customer)
        return negative_balances

    def find_max_balance(self) -> Customer | None:
        max_balance = 0
        max_customer = None
        for customer in self.__customers:
            if customer.balance > max_balance:
                max_balance = customer.balance
                max_customer = customer
        return max_customer

    def find_min_balance(self) -> Customer | None:
        min_balance = float("inf")
        min_customer = None
        for customer in self.__customers:
            if customer.balance < min_balance:
                min_balance = customer.balance
                min_customer = customer
        return min_customer


def main():
    bank = Bank("SFBU Bank")
    bank.load_customers()
    bank.display_customers()
    print()

    print("-- Add a customer")
    c = Customer(5555, "Smith", "John", "123 Main St, Fremont", 5000.0)
    bank.add_customer(c)
    bank.display_customers()
    print()

    print("-- Search for a customer")
    c2 = bank.search_customer("Smith", "John")
    print(c2)
    print()

    print("-- Update a customer")
    bank.update_customer(c, None, None, "456 Main St, Fremont", -1000.0)
    c3 = bank.search_customer("Smith", "John")
    print(c3)
    print()

    print("-- Find negative balances")
    negative_balances = bank.find_negative_balances()
    for customer in negative_balances:
        print(customer)
    print()

    print("-- Find max balance")
    max_customer = bank.find_max_balance()
    print(max_customer)
    print()

    print("-- Find min balance")
    min_customer = bank.find_min_balance()
    print(min_customer)
    print()

    print("-- Delete a customer")
    bank.delete_customer("Smith", "John")
    bank.display_customers()
    
    
    

if __name__ == "__main__":
    main()
