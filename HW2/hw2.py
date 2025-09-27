
from abc import ABC, abstractmethod

class Person(ABC):
    def __init__(self, name,  contact_number, email, address) -> None:
    
        self.__name = name
        self.__contact_number = contact_number
        self.__email = email
        self.__address = address
    @property
    def name(self):
        return self.__name
    
    @property
    def contact_number(self):
        return self.__contact_number
    
    @property
    def email(self):
        return self.__email
    
    @property
    def address(self):
        return self.__address
    
    @email.setter
    def email(self, value):
        # set the person's email with validation 
        if not value or '@' not in value or '.' not in value:
            raise ValueError("Please provide a valid email address (e.g, user@example.com)")
        self.__email = value.strip().lower()
   
    def get_personal_info(self) -> str:
        
        return f"Name: {self.__name}\nContact Number: {self.__contact_number}\nEmail: {self.__email}\nAddress: {self.__address}"
    
    
    @abstractmethod
    def get_full_info(self) -> str:
        """
        abstract method to get complete information
        must be implemented by concrete subclasses.
        
        Returns: 
            str: Complete information specific to the subclass.
        """
        pass
    
    def __str__(self) -> str:
        return f"Person(name ='{self.__name}', email = '{self.__email}')"
    
    def __repr__(self) -> str:
        return f"Person(name ='{self.__name}', conact_number = '{self.__contact_number}',email = '{self.__email}', address = '{self.__address}')"
        
    
    def __eq__(self, other):
        
        if not isinstance(other, Person):
            return False
        return self.__email == other.__email
    
class  Applicant(Person):
    
    
    def __init__(self, name, contact_number, email, address) -> None:
        super().__init__(name, contact_number, email, address)
        
    
    def get_full_info(self) -> str:
        
        
        """
        Implementaion of abstract method from Person class.
        Returns complete application information.
        """
        
        return self.get_personal_info()
    
    def __str__(self) -> str:
        return f"Application(name ='{self.name}', email = '{self.email}')"
    
    def __repr__(self) -> str:
        return f"Application('{self.name}', '{self.contact_number}','{self.email}', '{self.address}')"
    
    
from datetime import datetime

class Education:
    
    """
    class representing a single education record.
    Each applicant can have multiple education entries (high school, undergraduate, graduate, etc.) 
    """
    
    def __init__(self, institution, degree_level, year_completed):
        
        self.__institution = institution
        self.__degree_level = degree_level
        self.__year_completed = year_completed
        self.__validate_year(year_completed)
    
    @property
    def institution(self):
        return self.__institution
    
    @property
    def degree_level(self):
        return self.__degree_level
    @property
    def year_completed(self):
        return self.__year_completed
    
    @year_completed.setter
    def year_completed(self, value):
        self.__validate_year(value)
        self.__year_completed = value
        
        
    def __validate_year(self, year):
        # private method to validate the year
        
        current_year = datetime.now().year
        
        if not isinstance(year, int):
            raise ValueError("Year must be an integer.")
        
        if year < 1950 or year > current_year +5:
            raise ValueError(f"Year must be between 1950 and {current_year +5}.")
        
    def get_education_info(self) -> str:
        return f"{self.__degree_level} from {self.__institution}, completed in {self.__year_completed}"
    
    def is_completed(self) -> bool:
        # check if the education record is complete
        return self.__year_completed <= datetime.now().year
    
    def __str__(self) -> str:
        return f"Education(institution ='{self.__institution}', degree_level = '{self.__degree_level}', year_completed = '{self.__year_completed}')"
    
    def __repr__(self) -> str:
        return f"Education('{self.__institution}', '{self.__degree_level}', '{self.__year_completed}')"
    
    def __eq__(self, other):
        
        if not isinstance(other, Education):
            return False
        return (self.__year_completed == other.__year_completed and        
               self.__degree_level.lower() == other.__degree_level.lower() and 
               self.__institution.lower() == other.__institution.lower())
        
        

        
        
    
    
def main():
    
#     applicant = Applicant(
#         name = "John Doe",
#         contact_number = "123-456-7890",
#         email = "WQyHs@example.com",
#         address = "123 Main St, Anytown, USA"
#     )
#    # test the methods
#     print("---- Appliant Testing----")
#     print("String reprsentation:", applicant)
#     print("Developer reprsentation:", repr(applicant))
    
#     print("\n--PERSONAL INFO--")
#     print(applicant.get_personal_info())
    
#     print("\n--FULL INFO--")
#     print(applicant.get_full_info())
    
#     print("\n--PROPERTY ACCESS--")
#     print("Name:", applicant.name)
#     print("email:", applicant.email)
    
#     print("\n--Email Validation Test--")
#     # try:
#     #     applicant.email = "newemail@example.com"
#     #     print("Updated email:", applicant.email)    
#     # except ValueError as ve:
#     #     print("Error:", ve)
#     try:
#         applicant.email = "invalidemail"
#         print("Updated email:", applicant.email)
#     except ValueError as ve:
#         print("Error:", ve)

    print("\n---- EDUCATION CLASS TESTING ----")
    
    # create education records
    high_school = Education("Anytown High School", "High School Diploma", 2010)
    bachelor = Education("State University", "Bachelor's Degree in Computer Science", 2014)
    
    print("Education 1: ", high_school)
    print("Education 2: ", bachelor)
    
    print("\n -- DETAILED INFORMATION --")
    print(high_school.get_education_info())
    print()
    print(bachelor.get_education_info())
    
    print("\n-- COMPLETION STATUS --")
    print(f"High School Completed: {high_school.is_completed()}")
    print(f"Bachelor  Completed: {bachelor.is_completed()}")

if __name__ == "__main__":
    main()
    
              
    
    