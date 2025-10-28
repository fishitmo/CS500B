from person import Person
from contactInfo import ContactInfo
from property import Property


class Owner(Person):
    
    
    def __init__(self, first_name: str, last_name: str, contact_info: ContactInfo) -> None:
        super().__init__(first_name, last_name) # type: ignore
        self.__properties: list[Property] = []
        self.__contact_info = contact_info

    def add_property(self, address: str, price: float, square_footage: int, num_bedrooms: int, property_type: str) -> None:
        
        # check for duplicate address
        
        for prop in self.__properties:
            if prop.address == address:
                raise ValueError(f"Property with address {address} already exists for this owner.")
            
        new_property = Property(address, price, square_footage, num_bedrooms, property_type)

        self.__properties.append(new_property)

    def remove_property(self, address: str) -> None:
        
        i = 0
        while i < len(self.__properties):
            if self.__properties[i].address == address:
                self.__properties[i] = self.__properties[-1]
                self.__properties.pop()
                return
            else:
                i += 1
                
    def __iter__(self):
        self.__index = 0 # initialize index for each iteration
        return self

    def __next__(self):
        if self.__index < len(self.__properties):
            property = self.__properties[self.__index]
            self.__index += 1
            return property
        else:
            raise StopIteration
    def get_property_count(self) -> int:
        return len(self.__properties)


    @property
    def contact_info(self) -> ContactInfo:
        return self.__contact_info

    @contact_info.setter
    def contact_info(self, contact_info: ContactInfo) -> None:
        self.__contact_info = contact_info
        
    def to_dict(self) -> dict:
        return {
            "first_name": self.first_name, # type: ignore
            "last_name": self.last_name, # type: ignore
            "full_name": self.full_name, # type: ignore
            "contact_info": self.__contact_info.to_dict(), # type: ignore
            "property_count": self.get_property_count() # type: ignore
        }
        
    def validate(self) -> bool:

        if not self.first_name or not self.last_name: # type: ignore
            return False
        
        if not self.__contact_info.validate():
            return False
        
        return True
    
    
    def __str__(self) -> str:
        
        output = f"Owner: {self.full_name}\n" # type: ignore
        output += str(self.__contact_info) + "\n"
        output += f"Number of Properties: {self.get_property_count()}\n"
        for prop in self.__properties:
            output += str(prop) + "\n\n"
        return output



if __name__ == "__main__":
    
    print("Testing Owner class...")
    
    
    print("Creating ContactInfo and Owner1 instances:")
    contact_info = ContactInfo("(555) 123-4567", "john.doe@email.com", "123 Main St, City, State")
    owner1 = Owner("John", "Doe", contact_info)
    
    print(owner1)
    
    print("Second Owner with different contact info:")
    contact_info2 = ContactInfo("(555) 987-6543", "jane.smith@email.com", "789 Oak St, City, State")
    owner2 = Owner("Jane", "Smith", contact_info2)

    print(owner2)
    
    # Testing inherited methods from Person
    print("Testing inherited methods from Person:")
    print(f"First name: {owner1.first_name}") # type: ignore
    print(f"Last name: {owner1.last_name}") # type: ignore
    print(f"Full name: {owner1.full_name}") # type: ignore
    
    #testing contact info access
    
    print("Testing contact info access:")
    print(f"Owner1 Contact Info: {owner1.contact_info}")
    print(f"Owner2 Contact Info: {owner2.contact_info}")
    
    
    # testing property management
    
    print("Testing property management:")
    owner1.add_property("456 Elm St, City, State", 350000.0, 2000, 3, "House")
    owner1.add_property("789 Pine Rd, City, State", 250000.0, 1200, 2, "Condo")
    owner1.add_property("101 Maple St, City, State", 180000.0, 800, 1, "Apartment")
   
   # initial properties count
    print(f"Owner1 Property Count: {owner1.get_property_count()}")
    
    
    # testing duplicate property prevention
    print("Testing duplicate property prevention:")
    try:
        owner1.add_property("456 Elm St, City, State", 360000.0, 2100, 4, "House")
    except ValueError as e:
        print(f"Caught expected exception: {e}")
    
    print("Testing property removal:")
    owner1.remove_property("789 Pine Rd, City, State")
    print(f"Owner1 Property Count: {owner1.get_property_count()}")
    
    # testing set contact info
    print("Testing contact info update:")
    new_contact_info = ContactInfo("(555) 111-2222", "john.new@email", "123 Main St, City, State")
    owner1.contact_info = new_contact_info
    print("Updated Owner1 Contact Info:")
    print(f"New Phone Number: {owner1.contact_info.phone}")
    print(f"New Email: {owner1.contact_info.email}")
    
    # testing to_dict method
    print("Testing to_dict method:")
    owner_dict = owner1.to_dict()
    print("Dictionary Representation of Owner1:")
    for key, value in owner_dict.items():
        print(f"{key}: {value}")
        
    # testing validation method
    print("Testing validation method:")
    if owner1.validate():
        print("Owner1 is valid.")
    else:
        print("Owner1 is invalid.")
        
    # testing equality from Person
    print("Testing equality from Person:")
    owner3 = Owner("John", "Doe", new_contact_info)
    if owner1 == owner3:
        print("Owner1 and Owner3 are equal.")
    else:
        print("Owner1 and Owner3 are not equal.")
        
    # test with invalid contact info type
    print("Testing with invalid contact info type:")
    try:
        invalid_owner = Owner("Invalid", "Owner", "NotAContactInfo") # type: ignore
    except TypeError as e:
        print(f"Caught expected exception: {e}")
        
    # test with empty first name
    print("Testing with empty first name:")
    try:
        contact_test = ContactInfo("(555) 000-1111", "john.doe@email.com", "123 Main St, City, State")
        invalid_owner = Owner("", "Owner", contact_test) # type: ignore
        print(invalid_owner)
    except ValueError as e:
        print(f"Caught expected exception: {e}")
     # testing name modification from Person
    print("Testing name modification from Person:")
    owner1.first_name = "Jane" # type: ignore
    owner1.last_name = "Doe-Smith" # type: ignore
    print(f"Updated Owner1 Full Name: {owner1.full_name}") # type: ignore   
    
    # try to test invalid name 
    print("Testing invalid name modification:")
    try:
        owner1.first_name = "" # type: ignore
    except ValueError as e:
        print(f"Caught expected exception: {e}")
     
     
    print("Testing property iteration:")
    for prop in owner1:
        print(prop)
        
        

    
    