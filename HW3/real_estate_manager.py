
from isearchable import ISearchable
from property import Property
from owner import Owner
from buyer import Buyer
from data_persisitence_factory import DataPersistenceFactory
from contactInfo import ContactInfo
from idata_persistence import IDataPersistence
from property_status import PropertyStatus
class RealEstateManager(ISearchable):
    
    
    def __init__(self):
        
       
        self.__properties: list[Property] = []
        self.__owners : dict[str, Owner] = {}  
        self.__buyers : list[Buyer] = []
        
        # Persistence objects (composition - will be set by factory)
        self.__property_persistence: IDataPersistence = None
        self.__owner_persistence: IDataPersistence = None
        self.__buyer_persistence: IDataPersistence = None
        
        # Factory reference (composition)
        self.__factory: DataPersistenceFactory = None
    
    def set_persistence_objects(self, property_persistence, owner_persistence, buyer_persistence):
        
        self.__property_persistence = property_persistence
        self.__owner_persistence = owner_persistence
        self.__buyer_persistence = buyer_persistence
    
    def add_property(self, address, price, square_footage, num_bedrooms, owner_first_name, owner_last_name, property_type) -> Property:
        
        # Validate address uniqueness
        if self.get_property_by_address(address) is not None:
            raise ValueError(f"Property at {address} already exists")
        
        # Get or create owner
        owner = self.__get_or_create_owner(owner_first_name, owner_last_name)
        
        # Create property
        property_obj = Property(address, price, square_footage, num_bedrooms, owner, property_type)
        
        # Add to collections
        self.__properties.append(property_obj)
        owner.add_property(address, price, square_footage, num_bedrooms, property_type)
        
        return property_obj
    
    def update_property(self, address, price=None, square_footage=None, num_bedrooms=None, status=None):
        
        property_obj = self.get_property_by_address(address)

        if property_obj is None:
            return False

        # Update fields if provided
        if price is not None:
            property_obj.price = price

        if square_footage is not None:
            property_obj.square_footage = square_footage

        if num_bedrooms is not None:
            property_obj.num_bedrooms = num_bedrooms

        if status is not None:
            property_obj.status = status

        return True
    def __iter__(self):
        self.__index = 0
        return self
    
    def __next__(self):
        if self.__index < len(self.__properties):
            result = self.__properties[self.__index]
            self.__index += 1
            return result
        else:
            raise StopIteration
        
    def delete_property(self, address):
        
        property_obj = self.get_property_by_address(address)
        
        if property_obj is None:
            return False
        
        # Remove from properties list
        i =0 
        while i < len(self.__properties):
            if self.__properties[i].address == address:
                self.__properties[i] = self.__properties[-1]
                self.__properties.pop()
                break
            i += 1
        
        return True
    
    def get_property_by_address(self, address):
        
        for prop in self.__properties:
            if prop.address.lower() == address.lower():
                return prop
        return None
    
    def add_buyer(self, first_name, last_name, phone_number, email):
        
       
        full_name = f"{first_name} {last_name}"
        if self.__find_buyer(full_name) is not None:
            raise ValueError(f"Buyer {full_name} already exists")
        
      
        buyer = Buyer(first_name, last_name, phone_number, email)
        
        
        self.__buyers.append(buyer)
        
        return buyer
    
    def add_buyer_interest(self, buyer_name, property_address):
        
       
        buyer = self.__find_buyer(buyer_name)
        if buyer is None:
            return False
        
        
        property_obj = self.get_property_by_address(property_address)
        if property_obj is None:
            return False
        
        
        buyer.add_interested_property(property_obj)
        property_obj.add_interested_buyer(buyer)
        
        return True
    
    def get_interested_buyers(self, property_address):
        
        property_obj = self.get_property_by_address(property_address)
        
        if property_obj is None:
            return []
        
        return property_obj.interested_buyers
    
    def get_buyer_info(self, buyer_name):
        
        return self.__find_buyer(buyer_name)
    
    def search_by_criteria(self, criteria):
        
        results = self.__properties.copy()

        # Filter by min_price
        if 'min_price' in criteria:
            filtered = []
            min_price = criteria['min_price']
            for p in results:
                if p.price >= min_price:
                    filtered.append(p)
            results = filtered

        # Filter by max_price
        if 'max_price' in criteria:
            filtered = []
            max_price = criteria['max_price']
            for p in results:
                if p.price <= max_price:
                    filtered.append(p)
            results = filtered

        # Filter by min_bedrooms
        if 'min_bedrooms' in criteria:
            filtered = []
            min_bedrooms = criteria['min_bedrooms']
            for p in results:
                if p.num_bedrooms >= min_bedrooms:
                    filtered.append(p)
            results = filtered

        # Filter by property_type
        if 'property_type' in criteria:
            filtered = []
            prop_type = criteria['property_type']
            for p in results:
                if p.property_type == prop_type:
                    filtered.append(p)
            results = filtered

        # Filter by status
        if 'status' in criteria:
            filtered = []
            status = criteria['status']
            for p in results:
                if p.status == status:
                    filtered.append(p)
            results = filtered

        return results
    
    def search_by_name(self, owner_name):
        
        owner_name_lower = owner_name.lower()
        
        # Check if exact match exists
        if owner_name in self.__owners:
            return self.__owners[owner_name].properties
        
        # Otherwise search for partial match
        matching_properties = []
        for prop in self.__properties:
            if owner_name_lower in prop.owner.full_name.lower():
                matching_properties.append(prop)
        
        return matching_properties
    
    def get_all_sorted(self):
        
        
        owners_list = list(self.__owners.values())
        n = len(owners_list)
       
        i = 0
        while i < n - 1:
            j = 0
            while j < n - i - 1:
                
                try:
                    name_left = owners_list[j].full_name
                except Exception:
                    name_left = str(owners_list[j])

               
                try:
                    name_right = owners_list[j + 1].full_name
                except Exception:
                    name_right = str(owners_list[j + 1])
                if str(name_left) > str(name_right):
                    temp = owners_list[j]
                    owners_list[j] = owners_list[j + 1]
                    owners_list[j + 1] = temp
                j += 1
            i += 1
        return owners_list
    
    def save_all_data(self):
        
        if not self.__property_persistence or not self.__owner_persistence or not self.__buyer_persistence:
            print("Warning: Persistence objects not set. Data not saved.")
            return False
        
        try:
            property_dicts = []
            i = 0
            while i < len(self.__properties):
                prop = self.__properties[i]
                property_dicts.append(prop.to_dict())
                i += 1

            owner_dicts = []
            owners_iter = self.__owners.values().__iter__()
            while True:
                try:
                    owner = owners_iter.__next__()
                except StopIteration:
                    break
                owner_dicts.append(owner.to_dict())

            buyer_dicts = []
            j = 0
            while j < len(self.__buyers):
                buyer = self.__buyers[j]
                buyer_dicts.append(buyer.to_dict())
                j += 1
            
          
            self.__property_persistence.save(property_dicts)
            self.__owner_persistence.save(owner_dicts)
            self.__buyer_persistence.save(buyer_dicts)
            
            return True
        except Exception as e:
            print(f"Error saving data: {e}")
            return False
    
    def load_all_data(self):
        
        if not self.__property_persistence or not self.__owner_persistence or not self.__buyer_persistence:
            print("Warning: Persistence objects not set. Data not loaded.")
            return False
        
        try:
            # Clear existing data
            self.__properties.clear()
            self.__owners.clear()
            self.__buyers.clear()
            
            # Load data (in actual implementation, would reconstruct objects from dictionaries)
            # For now, just load the raw data
            property_dicts = self.__property_persistence.load()
            owner_dicts = self.__owner_persistence.load()
            buyer_dicts = self.__buyer_persistence.load()
            
            print(f"Loaded {len(property_dicts)} properties, {len(owner_dicts)} owners, {len(buyer_dicts)} buyers")
            
            return True
        except Exception as e:
            print(f"Error loading data: {e}")
            return False
    
    def __get_or_create_owner(self, first_name, last_name, phone=None, email=None, address=None):
        
        full_name = f"{first_name} {last_name}"
        
        if full_name not in self.__owners:
            if not phone:
                phone = "000-000-0000"
            if not email:
                email = f"{first_name.lower()}.{last_name.lower()}@email.com"
            if not address:
                address = "No address provided"
            contact_info = ContactInfo(phone, email, address)
            owner = Owner(first_name, last_name , contact_info)
            self.__owners[full_name ] = owner
        
        return self.__owners[full_name]
    
    def __find_buyer(self, name):
        
        name_lower = name.lower()
        
        for buyer in self.__buyers:
            if buyer.full_name.lower() == name_lower:
                return buyer
        
        return None
    
    
    def get_all_properties(self):
        
        return self.__properties.copy()
    
    def get_all_buyers(self):
        
        return self.__buyers.copy()
    
    def get_all_owners(self):
        
        return list(self.__owners.values())
    
    def get_statistics(self):
        
        # Manual counts for property statuses (no list comprehensions)
        available_count = 0
        sold_count = 0
        i = 0
        while i < len(self.__properties):
            prop = self.__properties[i]
            if prop.status == PropertyStatus.AVAILABLE:
                available_count += 1
            if prop.status == PropertyStatus.SOLD:
                sold_count += 1
            i += 1

        return {
            'total_properties': len(self.__properties),
            'total_owners': len(self.__owners),
            'total_buyers': len(self.__buyers),
            'available_properties': available_count,
            'sold_properties': sold_count
        }


