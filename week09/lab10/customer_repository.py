import csv
from customer import Customer

class CustomerRepository:
    
    def __init__(self) -> None:
        self.__filename = 'customers.csv'
        
        
    def read_customers(self) -> list[Customer]:
        customers: list[Customer] = []
        
        with open(self.__filename, "r") as file:
            reader = csv.reader(file, delimiter=';')
            
            for row in reader:
                row_customer = Customer.to_customer(row)
                customers.append(row_customer)
            # for row in reader:
            #     account_no = int(row[0])
            #     firstname = str(row[1])
            #     balance = float(row[2])
            #     customer = Customer(account_no, firstname, balance)
            #     customers.append(customer)
        return customers
    def save_customers(self, customers: list[Customer])-> None:
        
        with open(self.__filename, "w", newline='') as file:
            writer = csv.writer(file, delimiter=';')
            for customer in customers:
                writer.writerow(customer.to_list())
                
                
    
    
def main():
    repos = CustomerRepository()
    customers = repos.read_customers()
    for customer in customers:
        print(customer)
    
    new_customer = Customer(5555, "Alice", 15000)
    customers.append(new_customer)
    repos.save_customers(customers)
        
        
    
if __name__ == "__main__":
    main()
        