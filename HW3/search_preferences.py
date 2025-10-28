

from property_type import PropertyType
from property import Property

class SearchPreferences:
    
    def __init__(self, min_price: float, max_price: float, min_bedrooms: int, property_types: list[PropertyType]) -> None:
        
        
        # validate min_price and max_price
        if min_price < 0:
            raise ValueError("min_price must be non-negative")
        if max_price < 0:
            raise ValueError("max_price must be non-negative")
        if min_price > max_price:
            raise ValueError("min_price must be less than or equal to max_price")
        # validate min_bedrooms
        if min_bedrooms < 0:
            raise ValueError("min_bedrooms must be non-negative")
        
        if not isinstance(property_types, list):
            raise TypeError("property_types must be a list")
        for prop_type in property_types:
            if not isinstance(prop_type, PropertyType):
                raise TypeError("property_types must be a list of PropertyType objects")
        
        self._min_price = min_price
        self._max_price = max_price
        self._min_bedrooms = min_bedrooms
        # insert property types into list
        self.__property_types: list[PropertyType] = []
        for prop_type in property_types:
            self.__property_types.append(prop_type)

        @property
        def min_price(self) -> float:
            return self._min_price
        @property
        def max_price(self) -> float:
            return self._max_price
        @property
        def min_bedrooms(self) -> int:
            return self._min_bedrooms
        
        def __iter__(self):
            self.__index = 0
            return self
        def __next__(self):
            if self.__index < len(self.__property_types):
                prop_type = self.__property_types[self.__index]
                self.__index += 1
                return prop_type
            else:
                raise StopIteration
        
        def matches(self, property: Property) -> bool:
            
            
            if property.price < self._min_price or property.price > self._max_price:
                return False
            if property.num_bedrooms < self._min_bedrooms:
                return False
            
            # check property type
            if len(self.__property_types) > 0:
                if isinstance(property.property_type, str):
                    prop_type_enum = PropertyType.from_string(property.property_type)
                
                if prop_type_enum not in self.__property_types:
                    return False     
            
            return True

    def to_dict(self) -> dict:
        output = []
        for prop_type in self.__property_types:
            output.append(prop_type.value)
        return {
            "min_price": self._min_price,
            "max_price": self._max_price,
            "min_bedrooms": self._min_bedrooms,
            "property_types": output 
        }
    def validate(self) -> bool:
        
        if self._min_price < 0 or self._max_price < 0:
            return False
        if self._min_price > self._max_price:
            return False
        if self._min_bedrooms < 0:
            return False
        
        for prop_type in self.__property_types:
            if not isinstance(prop_type, PropertyType):
                return False
        
        return True
    
    def __str__(self) -> str:
        output = f"Search Preferences:\n"
        output += f"Min Price: {self._min_price}\n"
        output += f"Max Price: {self._max_price}\n"
        output += f"Min Bedrooms: {self._min_bedrooms}\n"
        output += "Property Types: "
        if len(self.__property_types) == 0:
            output += "Any\n"
        else:
            for prop_type in self.__property_types:
                output += str(prop_type) + "; "
                
            output = output[:-2] + "\n"

        return output

if __name__ == "__main__":
    print("Testing propertytype enumeration...")
    for prop_type in PropertyType:
        print(f"Property Type: {prop_type.name} = {prop_type.value}")
        
    print("\n Creating  PropertyType Instances:")
    house = PropertyType.HOUSE
    apartment = PropertyType.APARTMENT
    condo = PropertyType.CONDO
    townhouse = PropertyType.TOWNHOUSE
    
    print(f"House: {house} (type: {type(house)})")
    print(f"Apartment: {apartment} (type: {type(apartment)})")
    print(f"Condo: {condo} (type: {type(condo)})")
    print(f"Townhouse: {townhouse} (type: {type(townhouse)})")
     
     
    print("\nTesting Propertytype from_string method:")
    house_str = PropertyType.from_string("house")
    apartment_str = PropertyType.from_string("apartment")
    condo_str = PropertyType.from_string("condo")
    townhouse_str = PropertyType.from_string("townhouse")
    
    print(f"House: {house_str} (type: {type(house_str)})")
    print(f"Apartment: {apartment_str} (type: {type(apartment_str)})")
    print(f"Condo: {condo_str} (type: {type(condo_str)})")
    print(f"Townhouse: {townhouse_str} (type: {type(townhouse_str)})")
    
    # testing invalid string
    try:
        invalid_type = PropertyType.from_string("villa")
    except ValueError as e:
        print(f"Caught expected exception for invalid property type: {e}")
        
    print("Testing PropertyType.get_all_types method:")
    all_types = PropertyType.get_all_types()
    print(f"Property Types: {all_types}")
    
    
    print("\nTesting PropertyType equality:")
    house1 = PropertyType.HOUSE
    house2 = PropertyType.HOUSE
    apartment1 = PropertyType.APARTMENT
    condo1 = PropertyType.CONDO
    
    print(f"house1 == house2: {house1 == house2}")  
    print(f"house1 == apartment1: {house1 == apartment1}")  
    
    print(f"apartment1 == condo1: {apartment1 == condo1}")
    
    
    print("\nTesting SearchingPreferences with property type enum:")
    try:
        search_prefs = SearchPreferences(
            min_price=200000.0,
            max_price=500000.0,
            min_bedrooms=3,
            property_types=[PropertyType.HOUSE, PropertyType.CONDO]
        )
        print("search_prefs: creted successfully")
        print(search_prefs)
    except ValueError as e:
        print(f"Failed to create SearchPreferences: {e}")
    
    print("\nTesting invalid SearchingPreferences:")
    # print("\nTesting SearchingPreferences with property type string:")
    # try:
    #     search_prefs = SearchPreferences(
    #         min_price=200000.0,
    #         max_price=500000.0,
    #         min_bedrooms=3,
    #         property_types=["house", "condo"]
    #     )
    #     print("search_prefs: creted successfully")
    #     print(search_prefs)
    # except ValueError as e:
    #     print(f"Failed to create SearchPreferences: {e}")
    
   
    # try:
    #     search_prefs = SearchPreferences(
    #         min_price=200000.0,
    #         max_price=500000.0,
    #         min_bedrooms=3,
    #         property_types=['HOUSE', 'APARTMENT']
    #     )
    #     print("search_prefs: creted successfully")
    #     print(search_prefs)
    # except ValueError as e:
    #     print(f"Failed to create SearchPreferences: {e}")
    
    # mixed types string and enum
    # try:
    #     search_prefs = SearchPreferences(
    #         min_price=200000.0,
    #         max_price=500000.0,
    #         min_bedrooms=3,
    #         property_types=[PropertyType.HOUSE, "APARTMENT"]
    #     )
    #     print("search_prefs: creted successfully")
    #     print(search_prefs)
    # except ValueError as e:
    #     print(f"Failed to create SearchPreferences: {e}")
        
    # Testing invalid object type
    
    # try:
        
    #     invalid_type = SearchPreferences(
    #         min_price=200000.0,
    #         max_price=500000.0,
    #         min_bedrooms=3,
    #         property_types=[123, 456]
    #     )
    #     print("search_prefs: creted successfully")
    #     print(invalid_type)
    # except ValueError as e:
    #     print(f"Failed to create SearchPreferences: {e}")
