from subjectInterface import Subject
from observerInterface import Observer
from displayInterface import Display

class WeatherData(Subject):
    
    def __init__(self):
        
        self.__observers: list[Observer] = []
        self.__temperature: float = 0.0
        self.__humidity: float = 0.0
        self.__pressure: float = 0.0
    def registerObserver(self, observer: Observer) -> None:
        if observer not in self.__observers:
            self.__observers.append(observer)
            print("observer registered")
            
    def removeObserver(self, observer) -> None:
        if observer in self.__observers:
            self.__observers.remove(observer)
            print("observer removed")
    def notifyObserver(self) -> None:
        print("\nnotify all observers")
        for obsever in self.__observers:
            obsever.update(self.__temperature, self.__humidity, self.__pressure)
    
    def measurementsChnaged(self) -> None:
        self.notifyObserver()
        
    def setMeasurement(self, temperature: float,  humidity: float, presure: float) -> None:
        print("New measurement recived:")
        print(f"Temperature: {temperature}")
        print(f"Humidity: {humidity}")
        print(f"Presure: {presure}")
        
        self.__temperature = temperature
        self.__humidity = humidity
        self.__pressure = presure
        self.measurementsChnaged()
        
    @property
    def temperature(self) -> float:
        return self.__temperature
    
    @property
    def humidity(self) -> float:
        return self.__humidity
    @property
    def pressure(self) -> float:
        return self.__pressure
    