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

class ConstructionCompanyType(Enum):
    GENERAL_CONTRACTOR = "General_Contractor"
    SUBCONTRACTOR = "Subcontractor"
    CONSTRUCTION_MANAGER = "Construction_Manager"
    
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
    
    def remove_employees(self, employee_name: str) -> None:
        i = 0
        while i < len(self.__employees):
            if self.__employees[i].employee_name == employee_name:
                self.__employees[i] = self.__employees[-1]
                self.__employees.pop()
            else:
                i += 1 
        
    
    
    def __str__(self):
        output = f"Building: \n{self.__building_name} \n Area: {self.__area} sq ft, \n Stories: {self.__stories} Type: {self.__type.value}"
        
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
    
    
    def get_top_five_employees(self) -> list[Employee]:
        
        top_five :list[Employee] = []
        
        for employee in self:
                current_income = employee.annual_income
                
                
                inserted = False
                for i in range(len(top_five)):
                    if current_income > top_five[i].annual_income:
                        top_five.insert(i, employee)
                        inserted = True
                        break
                
                
                if not inserted and len(top_five) < 5:
                    top_five.append(employee)
                
                
                if len(top_five) > 5:
                    top_five = top_five[:5]
        
        return top_five
        
        
    def get_employee(self, employee_id: int) -> Employee|None:
          for employee in self:
            if employee.employee_id == employee_id:
                return employee
          return None
    
    def __str__(self):
        output = f"Company: \n{self.__company_name}"
        output += "\nEmployees:\n"
        for employee in self.__employees:
            output += str(employee)
        return output
    
    def display(self):
        print(self)
class ConstructionCompany(Company):
    def __init__(self, company_name: str, category: ConstructionCompanyType) -> None:
        super().__init__(company_name)
        self.__category = category
        self.__buildings: list[Building] = []
    
    @property
    def category(self) -> ConstructionCompanyType:
        return self.__category
    
    def __iter__(self):
        self.__index =-1
        return self
    def __next__(self):
        if self.__index >= len(self.__buildings) -1:
            raise StopIteration()
        self.__index +=1
        building = self.__buildings[self.__index]
        return building
    
    def add_building(self, building: Building) -> None:
        
        self.__buildings.append(building)
    
    def find_largest_building(self) -> Building | None:
        
        if not self.__buildings:
            return None
        
        largest = self.__buildings[0]
        for building in self.__buildings:
            if building.area > largest.area:
                largest = building
        
        return largest
    
    def get_building_by_type(self) -> dict[BuildingType, list[Building]]:
        
        result: dict[BuildingType, list[Building]] = {}
        
        for building in self:
            building_type = building.type
            if building_type not in result:
                result[building_type] = []
            result[building_type].append(building)
        
        return result
    
    def assign_employee_to_building(self, employee_id: int, building_type: BuildingType) -> None:
        
        # Find the employee in the company
        employee = self.get_employee(employee_id)
        
        if employee is None:
            print(f"Employee with ID {employee_id} not found in company.")
            return
        
        # Assign the employee to all buildings of the specified type
        assigned_count = 0
        for building in self:
            if building.type == building_type:
                building.add_employee(employee)
                assigned_count += 1
        
        if assigned_count > 0:
            print(f"Employee {employee.employee_name} (ID: {employee_id}) assigned to {assigned_count} building(s) of type {building_type.value}")
        else:
            print(f"No buildings of type {building_type.value} found.")
    
    def find_employee_buildings(self, employee_id: int) -> list[Building]:
       
        result: list[Building] = []
        
        for building in self:
            employee = building.get_employee(employee_id)
            if employee is not None:
                result.append(building)
        
        return result
    
    def __str__(self):
        output = f"Construction Company:\n"
        output += f"Company Name: {self.company_name}\n"
        output += f"Category: {self.__category.value}\n"
        output += f"Number of Buildings: {len(self.__buildings)}\n"
        output += f"Number of Employees: {len(list(self))}\n"
        output += "\nBuildings:\n"
        for building in self.__buildings:
            output += f"  - {building.building_name} ({building.type.value}, {building.area} sq ft)\n"
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
    emp5 = Employee(105, "John Smith", 65000.00)  # Duplicate name for testing
    emp6 = Employee(106, "David Wilson", 95000.00)
    emp7 = Employee(107, "Lisa Anderson", 88000.00) 
    
    print("\nEmployee 1:")
    emp1.display()
    print(f"\n__str__ output: {emp1}")
    
    
    print("Testing Building Class")
    
    
    # Create buildings
    building1 = Building("Tech Plaza", 50000.0, 5, BuildingType.MANUFACTURING_BUILDING)
    building1.add_employee(emp1)
    building1.add_employee(emp2)
    building1.add_employee(emp3)
    building1.add_employee(emp4)
    building1.add_employee(emp5)
    building1.add_employee(emp6)
    building1.add_employee(emp7)
    
    
    
    print("\nBuilding 1:")
    building1.display()
    print(f"\n__str__ output: {building1}")
    
    building2 = Building("Storage Central", 75000.0, 2, BuildingType.WAREHOUSE)
    building2.add_employee(emp3)
    
    print("\n\nBuilding 2:")
    building2.display()
    print(f"\n__str__ output: {building2}")
    
    print("\n--- Testing remove_employees() ---")
    print("Removing all employees named 'John Smith'...")
    building1.remove_employees("John Smith")
    print("\nBuilding 1 (after removing 'John Smith'):")
    building1.display()
    
    print("Testing Company Class")
   
    
    # Create company
    company = Company("Global Industries Inc.")
    company.add_employee(emp1)
    company.add_employee(emp2)
    company.add_employee(emp3)
    company.add_employee(emp4)
    company.add_employee(emp5)
    company.add_employee(emp6)
    company.add_employee(emp7)
    
    print("\nCompany:")
    company.display()
    # print(f"\n__str__ output: {company}")
    print("\n--- Testing get_employee() for Company ---")
    found_emp = company.get_employee(104)
    if found_emp:
        print(f"Found employee with ID 104: {found_emp.employee_name}")
    else:
        print("Employee not found")
    # Test get_top_five_employees
    print("\n--- Testing get_top_five_employees() for Company ---")
    top_five_company = company.get_top_five_employees()
    print(f"Top 5 employees by income in Company:")
    for i, emp in enumerate(top_five_company, 1):
        print(f"{i}. {emp.employee_name}: ${emp.annual_income:,.2f}")
        
    # Test get_employee with non-existent ID
    print("\nSearching for non-existent employee ID 999:")
    result = company.get_employee(999)
    print(f"Result: {result}")
    
    
    

if __name__ == "__main__":
    main()
    

    