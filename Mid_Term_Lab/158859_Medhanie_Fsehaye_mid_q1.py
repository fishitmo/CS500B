from abc import ABC, abstractmethod
from enum import Enum
class Displayable(ABC):
    @abstractmethod
    def display(self) -> None:
        pass
    
class BuildingType(Enum):
    MANUFACTURING_BUILDING = "Manufacturing_Building"
    WAREHOUSE = "Warehouse"
    DISTRIBUTION_CENTER = "Distribution_Center"
    FLEX_SPACE = "Flex_Space"
    
    
class Employee(Displayable):
    def __init__(self, employee_id, employee_name, annual_income):
        self.__employee_id = employee_id
        self.__employee_name = employee_name
        self.__annual_income = annual_income
    
   
    @property
    def employee_id(self):
        return self.__employee_id
    
    @property
    def employee_name(self):
        return self.__employee_name
    
    @property
    def annual_income(self):
        return self.__annual_income
    
    
    
    def __str__(self):
        return f"Employee:\n{self.__employee_id}\n{self.__employee_name}\n${self.__annual_income}\n"
       
    def display(self):
        print(self)
        
    
class Building(Displayable):
    def __init__(self, building_name: str, area: float, stories: int, building_type: BuildingType):
        self.__building_name = building_name
        self.__area = area
        self.__stories = stories
        self.__type = building_type
        self.__employees: list[Employee] = []
    
    
    @property
    def building_name(self):
        return self.__building_name
    
    @property
    def area(self):
        return self.__area
    
    @property
    def stories(self):
        return self.__stories
    
    @property
    def type(self):
        return self.__type
    
    def __iter__(self):
            self.__index =-1
            return self
    def __next__(self):
         
         if self.__index >= len(self.__employees) -1:
            raise StopIteration()
         self.__index +=1
         student = self.__employees[self.__index]
         return student  
    
    
    def add_employee(self, employee) -> None:
        self.__employees.append(employee)
    
    
        
    
    def __str__(self):
        output = f"Building: \n{self.__building_name} \n Area: {self.__area} sq ft, \n Storeis: {self.__stories} Type: {self.__type.value}"
        
        output += "\nEmployees:\n"
        for employee in self.__employees:
            output += str(employee)
        
        return output
    
    def display(self):
        print(self)

class Company(Displayable):
    def __init__(self, company_name: str) -> None:
        self.__company_name = company_name
        self.__employees = []
    
    # Properties
    @property
    def company_name(self) -> str:
        return self.__company_name
    
    
    def __iter__(self):
        self.__index =-1
        return self
    def __next__(self):
        if self.__index >= len(self.__employees) -1:
            raise StopIteration()
        self.__index +=1
        employee = self.__employees[self.__index]
        return employee
    
    def add_employee(self, employee):
        self.__employees.append(employee)
    
    
    
    def __str__(self):
        output = f"Company: \n{self.__company_name}"
        output += "\nEmployees:\n"
        for employee in self.__employees:
            output += str(employee)
        return output
    
    def display(self):
        print(self)

# Main method to test the implementation
def main():
    print("Testing Employee Class")
    
    # Create employees
    emp1 = Employee(101, "John Smith", 75000.00)
    emp2 = Employee(102, "Sarah Johnson", 82000.00)
    emp3 = Employee(103, "Michael Brown", 68000.00)
    emp4 = Employee(104, "Emily Davis", 91000.00)
    
    print("\nEmployee 1:")
    emp1.display()
    print(f"\n__str__ output: {emp1}")
    
    
    print("Testing Building Class")
    
    
    # Create buildings
    building1 = Building("Tech Plaza", 50000.0, 5, BuildingType.MANUFACTURING_BUILDING)
    building1.add_employee(emp1)
    building1.add_employee(emp2)
    
    print("\nBuilding 1:")
    building1.display()
    print(f"\n__str__ output: {building1}")
    
    building2 = Building("Storage Central", 75000.0, 2, BuildingType.WAREHOUSE)
    building2.add_employee(emp3)
    
    print("\n\nBuilding 2:")
    building2.display()
    print(f"\n__str__ output: {building2}")
    
    
    print("Testing Company Class")
   
    
    # Create company
    company = Company("Global Industries Inc.")
    company.add_employee(emp1)
    company.add_employee(emp2)
    company.add_employee(emp3)
    company.add_employee(emp4)
    
    print("\nCompany:")
    company.display()
    print(f"\n__str__ output: {company}")
    
    
    print("Testing All BuildingType Values")
    
    
    building3 = Building("Distribution Hub", 60000.0, 3, BuildingType.DISTRIBUTION_CENTER)
    building4 = Building("Flex Office", 30000.0, 4, BuildingType.FLEX_SPACE)
    
    print(f"\n{building3}")
    print(f"{building4}")
    
    
    print("All Tests Completed Successfully!")
    

if __name__ == "__main__":
    main()
    

    