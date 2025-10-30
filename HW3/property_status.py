from enum import Enum

class PropertyStatus(Enum):
    AVAILABLE = 'AVAILABLE'
    PENDING = 'PENDING'
    SOLD = 'SOLD'
    WITHDRAWN = 'WITHDRAWN'
    
    def __str__(self):
        return self.value
    
    @classmethod
    def from_string(cls, status_str: str) -> "PropertyStatus":
        
        for prop_status in cls:
            if prop_status.value == status_str.upper():
                return prop_status    
        raise ValueError(f"Unknown property status: {status_str}")
    
    
    @classmethod
    def get_all_statuses(cls) -> list[str]:
        statuses_list = []
        for prop_status in cls:
            statuses_list.append(prop_status.value)
        return statuses_list
    
    
    def __eq__(self, other: object) -> bool:
        if isinstance(other, PropertyStatus):
            return self is other
        if isinstance(other, str):
            try:
                return self is PropertyStatus.from_string(other)
            except ValueError:
                return False
        return False
    
    