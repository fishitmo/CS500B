from bank import Bank
from customer import Customer


class BankApp:
    def __init__(self, bank_name: str) -> None:
        self.__bank = Bank(bank_name)
        self.__bank.load_customers()

    def run(self) -> None:
        while True:
            self.__show_menu()
            choice = input("Enter your choice: ").strip()
            print()
            if choice == "1":
                self.__add_customer()
            elif choice == "2":
                self.__display_customers()
            elif choice == "3":
                self.__search_edit_customer()
            elif choice == "4":
                self.__delete_customer()
            elif choice == "5":
                self.__find_negative_balances()
            elif choice == "6":
                self.__find_max_min_balance()
            elif choice == "0":
                print("Bye")
                break
            else:
                print("Invalid choice. Please try again.")

    def __show_menu(self) -> None:
        print()
        print("=== MENU ===")
        print("1. Add Customer")
        print("2. Display Customers")
        print("3. Search and Edit Customer")
        print("4. Delete Customer")
        print("5. Find Negative Balances")
        print("6. Find Max/Min Balance")
        print("0. Exit")

    def __add_customer(self) -> None:
        while True:
            print("-- Add a customer")
            account_number = int(input("Enter account number: "))
            last_name = input("Enter last name: ").strip()
            first_name = input("Enter first name: ").strip()
            address = input("Enter address: ").strip()
            balance = float(input("Enter balance: ").strip())

            customer = Customer(account_number, last_name, first_name, address, balance)
            self.__bank.add_customer(customer)

            choice = input("Do you want to add another customer? (y/n): ").strip()
            if choice.lower() != "y":
                break

    def __display_customers(self) -> None:
        print("-- Display all customers")
        self.__bank.display_customers()

    def __search_edit_customer(self) -> None:
        print("-- Search and edit a customer")
        last_name = input("Enter last name: ").strip()
        first_name = input("Enter first name: ").strip()
        customer = self.__bank.search_customer(last_name, first_name)
        if customer is None:
            print("Customer not found")
        else:
            print("Found customer:")
            print(customer)
            print()

            choice = input("Do you want to edit this customer? (y/n): ").lower()
            if choice.strip() != "y":
                return

            print("Enter new values or leave blank (press Enter) to keep the current value")
            last_name = input("Enter new last name: ").strip()
            if not last_name:
                last_name = None

            first_name = input("Enter new first name: ").strip()
            if not first_name:
                first_name = None

            address = input("Enter new address: ").strip()
            if not address:
                address = None

            balance = float(input("Enter new balance: ").strip())
            if not balance:
                balance = None

            self.__bank.update_customer(customer, last_name, first_name, address, balance)

    def __delete_customer(self) -> None:
        print("-- Delete a customer")
        last_name = input("Enter last name: ").strip()
        first_name = input("Enter first name: ").strip()
        self.__bank.delete_customer(last_name, first_name)

    def __find_negative_balances(self) -> None:
        negative_balances = self.__bank.find_negative_balances()

        if negative_balances:
            print("Negative balances:")
            for customer in negative_balances:
                print(customer)
        else:
            print("The bank has no negative balances")

    def __find_max_min_balance(self) -> None:
        max_customer = self.__bank.find_max_balance()
        if max_customer is None:
            print("The bank has no customers")
        else:
            print("Max balance customer:")
            print(max_customer)
            print()

        min_customer = self.__bank.find_min_balance()
        if min_customer is None:
            print("The bank has no customers")
        else:
            print("Min balance customer:")
            print(min_customer)
            print()


if __name__ == "__main__":
    app = BankApp("SFBU Bank")
    app.run()
