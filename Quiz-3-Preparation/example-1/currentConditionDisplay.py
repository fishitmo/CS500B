from observerInterface import Observer
from displayInterface import Display
from subjectInterface import Subject
class CurrentConditionDisplay(Observer, Display):
    
    def __init__(self, weather_data: Subject):
         self.__tempreature: float =0
         self.__humidity: float = 0.0
         self.__weather_data: Subject = weather_data
         
         # register this observer with the subject 
         weather_data.registerObserver(self)
         
    def update(self, tempreture: float, humidity: float, pressure: float) -> None:
         self.__tempreature= tempreture
         self.__humidity = humidity
         self.display()
         
    def display(self) -> None:
         print("Current condition display")
         print(f"Tempreture: {self.__tempreature}")
         print(f"Humidity: {self.__humidity}")
         
 
         
