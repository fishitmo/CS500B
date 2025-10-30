from property_type import PropertyType
from property_status import PropertyStatus
from iobserverInterface import IObserver
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from owner import Owner
    from buyer import Buyer





class Property:

    def __init__(self, address: str, price: float, square_footage: int, num_bedrooms: int, owner: 'Owner', property_type: PropertyType) -> None:
        
    
        if not address:
            raise ValueError("Address cannot be empty.")
        
        if price <= 0:
            raise ValueError("Price must be greater than 0.")
        
        if square_footage <= 0:
            raise ValueError("Square footage must be greater than 0.")
        
        if num_bedrooms <= 0:
            raise ValueError("Number of bedrooms must be greater than 0.")
        
        if owner is None:
            raise ValueError("Owner cannot be None.")
        
        if not isinstance(property_type, PropertyType):
            raise TypeError("Property type must be of type PropertyType.")
        
        self.__address = address
        self.__price = price
        self.__square_footage = square_footage
        self.__num_bedrooms = num_bedrooms
        self.__owner = owner
        self.__property_type = property_type
        self.__status = PropertyStatus.AVAILABLE
        self.__interested_buyers: list['Buyer'] = []
        self.__observers: list[IObserver] = []
        
    @property
    def address(self) -> str:
        return self.__address

    @property
    def price(self) -> float:
        return self.__price

    @property
    def square_footage(self) -> int:
        return self.__square_footage

    @property
    def num_bedrooms(self) -> int:
        return self.__num_bedrooms

    @property
    def property_type(self) -> PropertyType: 
        return self.__property_type
    
    @property
    def status(self) -> PropertyStatus:
        return self.__status
    
    @price.setter
    def price(self, new_price: float) -> None:
        
        if new_price < 0:
            raise ValueError("Price must be greater than 0.")
        old_price = self.__price
        self.__price = float(new_price)
        self.notify_observers("price_change", {"property_address": self.__address, "old_value": old_price, "new_value": self.__price})
    
    @square_footage.setter
    def square_footage(self, new_square_footage: int) -> None:
        
        if new_square_footage < 0:
            raise ValueError("Square footage must be greater than 0.")
        old_square_footage = self.__square_footage
        self.__square_footage = int(new_square_footage)
        self.notify_observers("square_footage_change", {"property_address": self.__address, "old_value": old_square_footage, "new_value": self.__square_footage})
    @num_bedrooms.setter
    def num_bedrooms(self, new_num_bedrooms: int) -> None:
        
        if new_num_bedrooms < 0:
            raise ValueError("Number of bedrooms must be greater than 0.")
        old_num_bedrooms = self.__num_bedrooms
        self.__num_bedrooms = int(new_num_bedrooms)
        self.notify_observers("num_bedrooms_change", {"property_address": self.__address, "old_value": old_num_bedrooms, "new_value": self.__num_bedrooms})
    @property
    def owner(self) -> 'Owner':
        return self.__owner
    @property
    def interested_buyers(self) -> list['Buyer']:
        return self.__interested_buyers.copy()
    
    @status.setter
    def status(self, new_status: PropertyStatus) -> None:
        
        if not isinstance(new_status, PropertyStatus):
            raise ValueError("Status must be a PropertyStatus enum value.")
        old_status = self.__status
        self.__status = new_status
        
        self.notify_observers("status_change", {"property_address": self.__address, 
                                                "old_value": old_status.value, 
                                                "new_value": self.__status.value})
    
    def add_interested_buyer(self, buyer: 'Buyer') -> None:
        
        # check if buyer is already in the list
        for b in self.__interested_buyers:
            if b.full_name == buyer.full_name:
                raise ValueError("Buyer is already in the list of interested buyers")
        self.__interested_buyers.append(buyer)
        
        if isinstance(buyer, IObserver):
            self.attach_observer(buyer)
            
            
    def remove_interested_buyer(self, buyer: 'Buyer') -> bool|None:
        
        try:
            
            i = 0
            while i < len(self.__interested_buyers):
                if self.__interested_buyers[i].full_name == buyer.full_name: 
                    self.__interested_buyers[i] = self.__interested_buyers[-1]
                    self.__interested_buyers.pop()
                    if isinstance(buyer, IObserver):
                        self.detach_observer(buyer)
                    return True
                else:
                    i += 1
                
        except ValueError:         
                return False
    
    def detach_observer(self, observer: 'IObserver') -> None:
        i = 0
        while i < len(self.__observers):
            if self.__observers[i].get_observer_id() == observer.get_observer_id():
                self.__observers[i] = self.__observers[-1]
                self.__observers.pop()
                
                return
            else:
                i += 1
            
            
    def attach_observer(self, observer: IObserver) -> None:
        if not isinstance(observer, IObserver):
            raise ValueError("Observer must implement IObserver interface")
        
        observver_id = observer.get_observer_id()
        for o in self.__observers:
            if o.get_observer_id() == observver_id:
                raise ValueError("Observer is already attached to this property")
        self.__observers.append(observer)
        
    
    
    
    def __iter__(self):
        self.__index = 0
        return self
        
    def __next__(self):
        if self.__index < len(self.__interested_buyers):
            buyer = self.__interested_buyers[self.__index]
            self.__index += 1
            return buyer
        else:
            raise StopIteration
        

        
    def notify_observers(self, event: str, data: dict[str, str|float]):
        for observer in self.__observers:
            observer.update(event, data)
    
    def to_dict(self) -> dict:
        return {
            "address": self.__address,
            "price": self.__price,
            "square_footage": self.__square_footage,
            "num_bedrooms": self.__num_bedrooms,
            "owner": self.__owner.full_name,  
            "property_type": self.__property_type.value,
            "status": self.__status.value,
            "interested_buyers_count": len(self.__interested_buyers),
            "observers_count": len(self.__observers)
        }
    
    def validate(self) -> bool:
        
        
        # validate address
        if not self.__address:
            return False
        
        # validate price
        if self.__price < 0:
            return False
        
        # validate square footage
        if self.__square_footage < 0:
            return False
        
        # validate number of bedrooms
        if self.__num_bedrooms < 0:
            return False
        
        # validate owner
        if not self.__owner.validate():
            return False
        
        # validate property type
        if not isinstance(self.__property_type, PropertyType):
            return False
        
        # validate status
        if not isinstance(self.__status, PropertyStatus):
            return False
        return True
    
    def __str__(self) -> str:
        
        output = f"Property Address: {self.__address}\n"
        output += f"Price: {self.__price}\n"
        output += f"Square Footage: {self.__square_footage}\n"
        output += f"Number of Bedrooms: {self.__num_bedrooms}\n"
        output += f"Owner: {self.__owner.full_name}\n"  # type: ignore
        output += f"Property Type: {self.__property_type.value}\n"
        output += f"Status: {self.__status.value}\n"
        output += f"Number of Interested Buyers: {len(self.__interested_buyers)}\n"
        output += f"Number of Observers: {len(self.__observers)}\n"
        return output
    def __eq__(self, value: object) -> bool:
        
        if not isinstance(value, Property):
            return False                
        
        return self.__address.lower() == value.__address.lower()
    
if __name__ == "__main__":
    
    # print("\Testing Property Status Enum: ")
    # for status in PropertyStatus:
    #     print(f"{status.name}, {status.value}")
        
    # print("\nCreating PropertyStatus Instances:")
    # available = PropertyStatus.AVAILABLE
    # pending = PropertyStatus.PENDING
    # sold = PropertyStatus.SOLD
    # withdrawn = PropertyStatus.WITHDRAWN
    # print(f"Available: {available} (type: {type(available)})")
    # print(f"Pending: {pending}")
    # print(f"Sold: {sold}")
    # print(f"Withdrawn: {withdrawn}")
    
    
    # print("\n\n Testing PropertyStatus.from_string():")
    
    # try:
    #     status1 = PropertyStatus.from_string("AVAILABLE")
    #     print(f"'AVAILABLE' : {status1}")
        
    #     status2 = PropertyStatus.from_string("pending")
    #     print(f"'pending' : {status2}")
        
    #     status3 = PropertyStatus.from_string("SOLD")
    #     print(f"'SOLD': {status3}")
    # except ValueError as e:
    #     print(f"Error: {e}")
    
    # # Test invalid status
    # try:
    #     invalid = PropertyStatus.from_string("RENTED")
    #     print(f" ERROR: 'RENTED' should be invalid!")
    # except ValueError as e:
    #     print(f"Correctly rejected 'RENTED': {e}")
    
    # print("\n\ Testing PropertyStatus.get_all_statuses():")
    # print("-" * 70)
    # all_statuses = PropertyStatus.get_all_statuses()
    # print(f"All statuses: ")
    # for status in all_statuses:
    #     print(f"{status}")
    # print(f"Count: {len(all_statuses)}")
    
    # print("\n\n Testing PropertyStatus Equality: ")
    
    # available1 = PropertyStatus.AVAILABLE
    # available2 = PropertyStatus.AVAILABLE
    # pending = PropertyStatus.PENDING
    
    # print(f"available1 == available2: {available1 == available2}")
    # print(f"available1 == pending: {available1 == pending}")
    # print(f"available1 == 'AVAILABLE': {available1 == 'AVAILABLE'}")
    # print(f"available1 == 'available': {available1 == 'available'}")
    
    # print("\nTesting Property class:")
    
    # owner1 = Owner("John", "Smith")
    # owner2 = Owner("Jane", "Doe")
    # owner3 = Owner("Bob", "Johnson")
    
    # property1 = Property("123 Main St", 100000, 2000, 3, owner1, PropertyType.HOUSE)
    # property2 = Property("456 Elm St", 80000, 1500, 2, owner2, PropertyType.APARTMENT)    
    # property3 = Property("789 Oak St", 120000, 2500, 4, owner1, PropertyType.CONDO)
    # property4 = Property("321 Pine St", 60000, 1000, 1, owner3, PropertyType.HOUSE)
    
    # properties = [property1, property2, property3, property4]
    
    # for prop in properties:
    #     print(f"Property: {prop}")
       
    
    # print("\nTesting Getter Methods:")
   
    # print(f"Address: {property1.address}")
    # print(f"Price: ${property1.price}")
    # print(f"Square Footage: {property1.square_footage}")
    # print(f"Bedrooms: {property1.num_bedrooms}")
    # print(f"Owner: {property1.owner.full_name}")
    # print(f"Property Type: {property1.property_type}")
    # print(f"Status: {property1.status}")
    
    # print("\nTesting set_price() with Notification:")
    
    # print(f"Original price: ${property1.price}")
    
    # # Create buyer observers
    # buyer1 = Buyer("Alice Brown", "alice@email.com")
    # buyer2 = Buyer("Charlie Davis", "charlie@email.com")
    
    # # Attach observers
    # property1.attach_observer(buyer1)
    # property1.attach_observer(buyer2)
   
    
    # # Change price (should notify observers)
    # print(f"\nChanging price to $240,000...")
    # property1.price= 240000
    # print(f"New price: ${property1.price}")
    
    # print("\n Testing set_status() with Notification:")
    
    # print(f"Original status: {property1.status}")
    
    # print(f"\nChanging status to PENDING...")
    # property1.status = PropertyStatus.PENDING
    # print(f"New status: {property1.status}")
    
    # print(f"\nChanging status to SOLD...")
    # property1.status = PropertyStatus.SOLD
    # print(f"New status: {property1.status}")
    
    # # ----------
    # print("\nTesting Interested Buyers Management:")
   
    
    # # Create new property for testing
    # property5 = Property("321 Elm St", 300000, 2000, 3, owner1, PropertyType.HOUSE)
    
    # print(f"Initial interested buyers: {property5.to_dict()}")
    
    # # Add interested buyers
    # buyer3 = Buyer("David Lee", "david@email.com")
    # buyer4 = Buyer("Emma Wilson", "emma@email.com")
    
    # property5.add_interested_buyer(buyer3)
    # print(f"Added buyer: {buyer3.full_name}")
    # print(f"Interested buyers count: {property5.to_dict()}")
    
    
    # property5.add_interested_buyer(buyer4)
    # print(f"\nAdded buyer: {buyer4.full_name}")
    # print(f"Interested buyers count: {property5.to_dict()}")
   
    
    # print("\nTesting Duplicate Buyer Prevention:")
    
    # try:
    #     property5.add_interested_buyer(buyer3)
    #     print("ERROR: Duplicate buyer should not be allowed!")
    # except ValueError as e:
    #     print(f"Correctly rejected duplicate: {e}")
        
    # print("\nTesting Observer Notifications:")
    # print("Changing price (should notify interested buyers)...")
    # property5.price = 290000
    
    # print(f"\nBuyer3 notifications: {len(buyer3.get_notifications())}")
    # print(f"Buyer4 notifications: {len(buyer4.get_notifications())}")
    
    # print("\nTesting remove_interested_buyer():")
    
    # print(f"Buyers and observers before removal: {property5}")
    
    
    # result = property5.remove_interested_buyer(buyer3)
    # print(f"\nRemoved buyer: {result}")
    # print(f"Buyers and observers after removal: {property5}")
    
    
    # print("Testing to_dict() Method:")
    
    # property_dict = property1.to_dict()
    # print("Dictionary representation:")
    # for key, value in property_dict.items():
    #     print(f"  {key}: {value}")
        
    # print("\n Testing validate() Method:")
    
    # # print(f"Is property1 valid? {property1.validate()}")
    # # print(f"Is property2 valid? {property2.validate()}")
    # # print(f"Is property3 valid? {property3.validate()}")
    
    
    # print("\nTesting Invalid Property Creation:")
    
    
    # # Empty address
    # try:
    #     invalid = Property("", 100000, 1000, 2, owner1, PropertyType.HOUSE)
    #     print("ERROR: Should reject empty address!")
    # except ValueError as e:
    #     print(f"Correctly rejected empty address: {e}")
    
    # # Negative price
    # try:
    #     invalid = Property("123 Test", -100000, 1000, 2, owner1, PropertyType.HOUSE)
    #     print("ERROR: Should reject negative price!")
    # except ValueError as e:
    #     print(f"Correctly rejected negative price: {e}")
    
    # # Zero square footage
    # try:
    #     invalid = Property("123 Test", 100000, 0, 2, owner1, PropertyType.HOUSE)
    #     print("ERROR: Should reject zero square footage!")
    # except ValueError as e:
    #     print(f"Correctly rejected zero sqft: {e}")
    
    # # Negative bedrooms
    # try:
    #     invalid = Property("123 Test", 100000, 1000, -2, owner1, PropertyType.HOUSE)
    #     print("ERROR: Should reject negative bedrooms!")
    # except ValueError as e:
    #     print(f"Correctly rejected negative bedrooms: {e}")
    
    # # None owner
    # try:
    #     invalid = Property("123 Test", 100000, 1000, 2, None, PropertyType.HOUSE)
    #     print("ERROR: Should reject None owner!")
    # except ValueError as e:
    #     print(f"Correctly rejected None owner: {e}")
    
    # # Invalid property type (string instead of enum)
    # try:
    #     invalid = Property("123 Test", 100000, 1000, 2, owner1, "HOUSE")
    #     print("ERROR: Should reject string property type!")
    # except TypeError as e:
    #     print(f"Correctly rejected string property type: {e}")
    
    # print("\nTesting __str__ :")
    
    # print(f"str(property1):  {str(property1)}")
    
    
    # print("\nTesting Equality (__eq__):")
   
    # property_same_address = Property("123 Main Street, City, State", 999999, 9999, 9, owner2, PropertyType.CONDO)
    # print(f"property1 == property2: {property1 == property2}")
    # print(f"property1 == property_same_address: {property1 == property_same_address}")
    
    pass
