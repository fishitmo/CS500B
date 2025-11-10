from abc import ABC, abstractmethod

class Observer(ABC):
    
    @abstractmethod
    def update(self, tempreture: float, humidity: float, pressure: float) -> None:
        pass
    