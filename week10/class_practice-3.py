from __future__ import annotations

from abc import ABC, ABCMeta, abstractmethod
import enum

class Subject(ABC):
    
     @abstractmethod
     def registerObserver(self, o):
         pass
     
     @abstractmethod
     def removeObserver(self, o):
         pass
     
     @abstractmethod
     def notifyObserver(self):
         pass
     
     
class Observer(ABC):
    @abstractmethod
    def  update(self, temp, rpm, speed):
        pass
    
    
class DisplayElement(ABC):
    
    @abstractmethod
    def display(self):
        pass
    
class EngineData(Subject):
    
    def __init__(self):
        
        self.__observers = []
        self.__tempreture = 0.0
        self.__rpm = 0.0
        self.__speed = 0.0
        
    def registerObserver(self, o):
        self.__observers.append(o)
        
    def removeObserver(self, o):
        i = self.__observers.index(o)
        if i>=0:
            self.__observers.pop(i)
            
            
    def notifyObserver(self):
        for o in self.__observers:
            o.update(self.__tempreture, self.__rpm, self.__speed)
            print()
            
    def measurementsChanged(self):
        self.notifyObserver()
        
    def setMeasurements(self, temp, rpm, speed):
        self.__tempreture = temp
        self.__rpm = rpm 
        self.__speed = speed
        self.measurementsChanged()
        
class AnalogDisplay(Observer, DisplayElement):
    
    def __init__(self, engineData):
        self.__engineData = engineData
        self.__temperature =0
        self.__rpm = 0.0
        self.__speed = 0.0
        engineData.registerObserver(self)
        
        
    def display(self):
        
        print("Analog Display:")
        print("Temperature =", self.__rpm)
        print("RPM =", self.__rpm)
        print("Speed =", self.__speed)
        
    def update(self, temp, rpm, speed):
        self.__temperature = temp
        self.__rpm = rpm
        self.__speed = speed
        self.display()
        
class DigitalDisplay(Observer, DisplayElement):
    
    def __init__(self, engineData):
        self.__engineData = engineData
        self.__temperature = 0
        self.__rpm = 0.0
        self.__speed = 0.0
        engineData.registerObserver(self)
        
    def display(self):
        print("Digital Display:")
        print("Temperature =", self.__temperature)
        print("RPM =", self.__rpm)
        print("Speed =", self.__speed)
        
        
    def update(self, temp, rpm, speed):
              
       self.__temperature = rpm
       self.__rpm = rpm
       self.__speed = speed
       self.display()
       
def main():
    engineData = EngineData()
    analog = AnalogDisplay(engineData)
    digital = DigitalDisplay(engineData)
    
    print("The first setMeasurments called.")
    engineData.setMeasurements(80, 7000, 80)
    
    engineData.removeObserver(digital)
    
    print("The second setMeasurments called.")
    engineData.setMeasurements(60, 4000, 60)
    
if __name__ == "__main__":
    main()
    
    
    
    
    
     
    
    
    
    
    
    