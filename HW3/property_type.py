



from enum import Enum

class PropertyType(Enum):
    
    HOUSE = "HOUSE"
    APARTMENT = "APARTMENT"
    CONDO = "CONDO"
    TOWNHOUSE = "TOWNHOUSE"
    
    def __str__(self):
        return self.value
    
    
    @classmethod
    def from_string(cls, type_str: str) -> "PropertyType":
        
        type_upper = type_str.upper()
        for prop_type in cls:
            if prop_type.value == type_upper:
                return prop_type
        raise ValueError(f"Unknown property type: {type_str}")
    
    @classmethod
    def get_all_types(cls) -> list[str]:
        types_list = []
        for prop_type in cls:
            types_list.append(prop_type.value)
        return types_list
    
    # define __eq__ method
    def __eq__(self, other: object) -> bool:
        # Compare to another PropertyType by identity
        if isinstance(other, PropertyType):
            return self is other
        # Allow comparing to a string like "house" or "HOUSE"
        if isinstance(other, str):
            try:
                return self is PropertyType.from_string(other)
            except ValueError:
                return False
        return False
    



