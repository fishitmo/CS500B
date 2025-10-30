from person import Person
from iobserverInterface import IObserver
from contactInfo import ContactInfo
from search_preferences import SearchPreferences
from property import Property
from property_type import PropertyType
import re
class Buyer(Person, IObserver):
    
    
    def __init__(self, first_name: str, last_name: str, phone_number: str, email: str) -> None:
        super().__init__(first_name, last_name)
        self.__phone_number = phone_number
        self.__email = email
        self.__interested_properties: list[Property] = []
        self.__search_preference: SearchPreferences | None = None
        
    
    @property
    def phone_number(self) -> str:
        return self.__phone_number
    
    @property
    def email(self) -> str:
        return self.__email
    
    
    @phone_number.setter
    def phone_number(self, value: str) -> None:
        self.__phone_number = value
        
    @email.setter
    def email(self, value: str) -> None:
        self.__email = value
        
    @property
    def search_preference(self) -> SearchPreferences | None:
        return self.__search_preference
    
    def add_interested_property(self, property: Property) -> None:
        # check if the property is already in the list
        for prop in self.__interested_properties:
            if prop.address == property.address:
                raise ValueError("Property is already in the list of interested properties")
        
        self.__interested_properties.append(property)
    @property
    def interested_properties(self) -> list[Property]:
        return self.__interested_properties.copy()
    
    def __iter__(self):
        self.__index = 0 # initialize index for each iteration
        return self
    
    def __next__(self):
        if self.__index < len(self.__interested_properties):
            property = self.__interested_properties[self.__index]
            self.__index += 1
            return property
        else:
            raise StopIteration
        
    def remove_interested_property(self, property: Property) -> None:
       try :   
            i = 0
            
            while i < len(self.__interested_properties):
                if self.__interested_properties[i].address == property.address:
                    self.__interested_properties[i] = self.__interested_properties[-1]
                    self.__interested_properties.pop()
                    return
                else:
                    i += 1
                    
       except IndexError:
            raise ValueError("Property is not in the list of interested properties")
        
    
    
    def set_search_preference(self, min_price: float, max_price: float, min_bedrooms: int, property_types: list[PropertyType]) -> None:
        value = SearchPreferences(min_price, max_price, min_bedrooms, property_types)
        self.__search_preference = value
    
    
    
    
    def matches_preferences(self, property: Property) -> bool:
        
        if self.__search_preference is None:
            return True
        
        return self.__search_preference.matches(property) 
    
    def update(self, event: str, data: dict[str, str]):
        notification = {
            'buyer': self.full_name,
            'event': event,
            'data': data
        }
        print(f"Notification: Buyer {self.full_name} {notification['event']} {notification['data']}")
        if 'property_address' in data:
            print(f"Property: {data['property_address']}")
        if 'old_value' in data and 'new_value' in data:
            print(f"Old Value: {data['old_value']}")
            print(f"New Value: {data['new_value']}")
        
    def get_observer_id(self):
        return f"{self.full_name} , {self.email}"
    
    
    
    def to_dict(self):
        
        buyer_dict = {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "full_name": self.full_name,
            "phone_number": self.phone_number,
            "email": self.email,
            "interested_properties_count": len(self.__interested_properties)
        }
        
        if self.__search_preference is not None:
            buyer_dict["search_preference"] = self.__search_preference.to_dict()  
        
        
        return buyer_dict
        
    def validate(self):
        
        if not self.first_name or not self.last_name:
            return False
        
        # validate phone number and email
        if not self._validate_phone(self.phone_number):
            return False
        
        if not self._validate_email(self.email):
            return False
        
        # validate search preferences
        if self.__search_preference is not None:
            if not self.__search_preference.validate():
                return False
        
        return True
    

        
    
    def _validate_phone(self, phone: str) -> bool:
        
        if not phone:
            return False
        
        phone_clean = phone.strip()
        digits_only = re.sub(r'[\s\-\(\)\.]+', '', phone_clean)  
        
        if len(digits_only) >= 10 and len(digits_only) <= 11 and digits_only.isdigit():
            return True
        
        return False
    
    
    def _validate_email(self, email: str) -> bool:
        
        if not email:
            return False
        
        email_clean = email.strip()
        
        email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        
        if re.match(email_regex, email_clean):
            return True
        
        return False
    
    def __str__(self) -> str:
        output = f"Buyer: {self.full_name}\n"
        output += f"Phone Number: {self.phone_number}\n"
        output += f"Email: {self.email}\n"
        output += f"Number of Interested Properties: {len(self.__interested_properties)}\n"
        for prop in self.__interested_properties:
            output += str(prop.property_type) + "\n\n"
        return output
    
    
    

if __name__ == "__main__":
    
    
    print("Testing Buyer class:")
    print("\n Creating a Buyer object:")
    buyer1 = Buyer("John", "Doe", "555-123-4567", "jdoe@example.com")
    
    print(buyer1)
    
    # test second buyer
    print("\n Creating a second Buyer object:")
    buyer2 = Buyer("Jane", "Diese", "555-987-6543", "4wC0g@example.com")
    
    print(buyer2)
    
    print("\nTested Inherited Method from Person class:")
    
    print(f"First Name: {buyer1.first_name}")
    print(f"Last Name: {buyer1.last_name}")
    print(f"Full Name: {buyer1.full_name}")
    print(f"Phone Number: {buyer1.phone_number}")
    print(f"Email: {buyer1.email}")
    
    
    print("\nTestting property Interest Management")
    
    # create properties (address, price, square_footage, num_bedrooms, property_type)
    property1 = Property("123 Main St", 100000, 1200, 2, "Apartment")
    property2 = Property("456 Elm St", 200000, 1400, 3, "Condo")
    property3 = Property("789 Oak St", 150000, 1600, 3, "Townhouse")
   
    
   
    
    # add properties to interested properties
    buyer1.add_interested_property(property1)
    print(f"{buyer1.full_name} is interested in {property1.address}")
    print(buyer1)
   
    buyer1.add_interested_property(property2)
    print(f"{buyer1.full_name} is interested in {property2.address}")
    print(buyer1)
    
    buyer1.add_interested_property(property3)
    print(f"{buyer1.full_name} is interested in {property3.address}")
    print(buyer1)
    
    
    print("\nTesting Dublicated Properties")
   
    try:
        duplicated_property = Property("123 Main St", 100000, 1200, 2, "Apartment")
        buyer1.add_interested_property(duplicated_property)
        print("Duplicated property added to interested properties.")
    except Exception as e:
        print(type(e), e)
        print("Property already in interested properties.")
        
    print("\nTesting Interested Properties removal:")
    
    print(f"property before removal: {property1.address}")
    buyer1.remove_interested_property(property1)
    print(f"property after removal: {property1.address}")
    print(buyer1)
    # try to remove non existing property
    print("\nTrying to remove non existing property:")
    
    non_existing_property = Property("999 Main St", 100000, 1100, 2, "Apartment")
    result = buyer1.remove_interested_property(non_existing_property)
    
    print(f"\nTrying to remove non existing property: {result}")
    
    print("\nTesting SearchPreference Integraton:")
    
    # create search preference
    
    
    
    
    # assign via property setter
    prefs =buyer1.set_search_preference(20000, 500000, 2, [PropertyType.APARTMENT, PropertyType.CONDO, PropertyType.TOWNHOUSE])
    
    retrives_prefs = buyer1.search_preference
    print(retrives_prefs)
    
    print("\nTesting Matches Preferences Method:")
    
    # Creating test properties (match/non-match scenarios)
    matching_property1 = Property("123 Main St", 300000, 1300, 2, "Apartment")
    non_matching_price = Property("456 Elm St", 600000, 1400, 3, "Condo")
    non_matching_sqft = Property("789 Oak St", 250000, 1500, 1, "Townhouse")
    non_matching_type = Property("101 Main St", 220000, 1200, 2, "House")
    non_matching_address = Property("111 Main St", 280000, 1350, 2, "Apartment")
    
    
    
    print(f"Testing against {prefs}")
    print(f"Matches preferences: {buyer1.matches_preferences(matching_property1)}")
    print(f"Does not match preferences: {buyer1.matches_preferences(non_matching_price)}")
    print(f"Does not match preferences: {buyer1.matches_preferences(non_matching_sqft)}")
    print(f"Does not match preferences: {buyer1.matches_preferences(non_matching_type)}")
    print(f"Does not match preferences: {buyer1.matches_preferences(non_matching_address)}")
    
    
    
    print("\nTesting observer pattern Update Method:")
   
    # simulate property change notification
    event_data = {'property_address': '123 Main St', 'old_value': 'Apartment', 'new_value': 'Condo'}
    print("\nTrigiering property change notification:")
    buyer1.update("property_changed", event_data)
    
    print("\nTesting get_observer_id Method:")
    print(f"Observer ID: {buyer1.get_observer_id()}")
    
    print("\nTesting to_dict Method:")
    buyer1_dict = buyer1.to_dict()
    print(buyer1_dict)
    print("\nDictioanary representation")
    for key, value in buyer1_dict.items():
        print(f"{key}: {value}")
        
    print("\nTesting validate Method:")
    print(buyer1.validate())
    print(buyer2.validate())
    
    print("\n\n14. Testing Setter Methods with Validation:")
    print("-" * 70)
    
    
    print(f"Current phone: {buyer1.phone_number}")
    buyer1.phone_number="555-999-8888"
    print(f"✓ Updated phone: {buyer1.phone_number}")
    
    print(f"\nCurrent email: {buyer1.email}")
    buyer1.email= "john.new@email.com"
    print(f"✓ Updated email: {buyer1.email}")
    

    
    
   
    
                                                              
    
    
                
         
        
        
        
    

