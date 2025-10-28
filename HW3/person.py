from abc import ABC, abstractmethod


class Person(ABC):
    
    
    def __init__(self, first_name: str, last_name: str) -> None:
        self._first_name = first_name
        self._last_name = last_name

    @property
    def first_name(self) -> str:
        return self._first_name
    
    @property
    def last_name(self) -> str:
        return self._last_name
    
    @property
    def full_name(self) -> str:
        return f"{self._first_name} {self._last_name}"
    

    @first_name.setter
    def first_name(self, first_name: str) -> None:
        if not first_name:
            raise ValueError("First name cannot be empty.")
        self._first_name = first_name

    @last_name.setter
    def last_name(self, last_name: str) -> None:
        if not last_name:
            raise ValueError("Last name cannot be empty.")
        self._last_name = last_name
    
    @abstractmethod
    def to_dict(self) -> dict:
        pass
    
    
    @abstractmethod
    def validate(self) -> bool:
        pass
    
    def __eq__(self, value: object) -> bool:
        
        if isinstance(value, Person):
            return (self.first_name == value.first_name and
                    self.last_name == value.last_name)
        return False
    
    def __str__(self) -> str:
        return self.full_name
    

    
    
