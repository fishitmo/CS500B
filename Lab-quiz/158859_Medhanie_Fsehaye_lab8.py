from abc import ABC, abstractmethod

class Displayable(ABC):
    @abstractmethod
    def display(self):
        pass
    
class AbstractCompany(ABC):

        
  _maxNumberEmployees = 10
  
  @abstractmethod
  def getEmployeeNameList() -> list[str]:
      pass
        
        
class Employee(Displayable):
    def __init__(self, empid: int, name: str, salary: float):
        self.__empid = empid
        self.__name = name
        self.__salary = salary
    @property
    def salary(self) -> float:
        return self.__salary
    @property
    def name(self) -> str:
        return self.__name
    
        
    def display(self):
        print(f" Employee: name: {self.__name} , salary: {self.__salary}")
        
class Company(Displayable, AbstractCompany):
    def __init__(self, compName: str) -> None:
        self.__compName = compName
        self.__employees: list[Employee] = []
    
    @property
    def employees(self) -> list[Employee]:
        return self.__employees
        
    def addEmployee(self, employee: Employee):
        if len(self.__employees) >= self._maxNumberEmployees:
            print(f"Can not add more employees , {self._maxNumberEmployees} reached")
        else: 
            self.__employees.append(employee)
            
    def getEmployeeNameList(self) -> list[str]:
        employee_names= []
        for employee in self.__employees:
            employee_names.append(employee.name)
        return employee_names
    
    def display(self):
        
        print(f"compName: {self.__compName}")
        output = "The company has these employees:\n"
        employees = self.getEmployeeNameList()
        for employee in employees:
            output += str(employee) + "\n"
        print(output)
        print(f"Number of employees: {len(self.__employees)}")
        print(f"Max number of employees: {self._maxNumberEmployees}")
        
        
class TradingCompany(Company):
    def __init__(self, compName: str, productType: str, numOfOffices: int) -> None:
        super().__init__(compName)
        self.__productType = productType
        self.__numOfOffices = numOfOffices
        
        
    def getEmployeesHighSalary(self, limit: float) -> list[Employee]:
        highSalhigh_salary_employee: list[Employee] = []
        for employee in self.employees:
            if employee.salary > limit:
        
             highSalhigh_salary_employee.append(employee)
        return highSalhigh_salary_employee
    
    def display(self):
        super().display()
        print(f"productType: {self.__productType} , numOfOffices: {self.__numOfOffices}")
        
    
    
    
        
        
def main():
    print("\n Creating TradingCompany...")
    trading_company = TradingCompany("Global Trade Corp", "Electronics", 5)
    print("\n Creating Employees...")
    emp1 = Employee(101, "Alice Johnson", 75000.0)
    emp2 = Employee(102, "Bob Smith", 85000.0)
    emp3 = Employee(103, "Charlie Brown", 65000.0)
    emp4 = Employee(104, "Diana Prince", 95000.0)
    emp5 = Employee(105, "Eve Martinez", 72000.0)
    print("\n Adding Employees to TradingCompany...")
    trading_company.addEmployee(emp1)
    trading_company.addEmployee(emp2)
    trading_company.addEmployee(emp3)
    trading_company.addEmployee(emp4)
    trading_company.addEmployee(emp5)
    print("\n4. Displaying TradingCompany...")
    trading_company.display() 
    
    print("\n Displaying Employees with salary > $70,000")
    high_salary_employees = trading_company.getEmployeesHighSalary(70000.0)
    for employee in high_salary_employees:
        employee.display()
    
    print("Maximum Employee Capacity:")
    print(trading_company._maxNumberEmployees)
    
    print("\n Adding more Employees to test the limit")
    for i in range(6, 13):
        emp = Employee(100 + i, f"Employee {i}", 60000.0)
        trading_company.addEmployee(emp)
    
    
    
    
    
if __name__ == "__main__":
    main()
        
    
        
    
        
    
        
             
        
    
    
    