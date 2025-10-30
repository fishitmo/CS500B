from abc import ABC, abstractmethod

class IDataPersistence(ABC):
  
    
    @abstractmethod
    def save(self, data: list) -> bool:
        
        pass
    
    @abstractmethod
    def load(self) -> list:
      
        pass
    
    @abstractmethod
    def delete(self, identifier: str) -> bool:
     
        pass
    
    @abstractmethod
    def update(self, identifier: str, data: dict) -> bool:
     
        pass
    
    @abstractmethod
    def exists(self, identifier: str) -> bool:
      
        pass