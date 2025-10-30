import csv
from customer import Customer

class CustomerRepository:
    
    def __init__(self) -> None:
        self.__filename = 'customers.csv'
        
        
    def read_customers(self) -> list[Customer]:
        customers: list[Customer] = []
        
        with open(self.__filename, "r", newline='') as file:
            reader = csv.reader(file, delimiter=';')
            
            for row in reader:
                row_customer = Customer.to_customer(row)
                customers.append(row_customer)
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
    
    new_customer = Customer(5555, "Smith", "John", "123 Main St", 5000.0)
    customers.append(new_customer)
    repos.save_customers(customers)
        
        
    
if __name__ == "__main__":
    main()
        