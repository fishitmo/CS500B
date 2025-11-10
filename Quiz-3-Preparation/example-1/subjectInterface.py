from abc import ABC , abstractmethod

class Subject(ABC):
    
    @abstractmethod
    def registerObserver(self, observer) -> None:
        pass
    
    @abstractmethod
    def removeObserver(self, observer) -> None:
        pass
    
    @abstractmethod
    def notifyObserver(self) -> None:
        pass

    