from observerInterface import Observer
from displayInterface import Display
from subjectInterface import Subject

class StatisticlaDisplay(Observer, Display):
    def __init__(self, weather_data: Subject):
        self._temperatures: list[float] = []
        self._weather_data: Subject = weather_data
        
        weather_data.registerObserver(self)
    
    def update(self, temperature: float, humidity: float, pressure: float) -> None:
        """Receive update from subject"""
        self._temperatures.append(temperature)
        self.display()
    
    def display(self) -> None:
        """Display statistics"""
        if self._temperatures:
            avg_temp = sum(self._temperatures) / len(self._temperatures)
            max_temp = max(self._temperatures)
            min_temp = min(self._temperatures)
            
            print(f"\n📊 Statistics Display:")
            print(f"   Avg Temperature: {avg_temp:.1f}°C")
            print(f"   Max Temperature: {max_temp:.1f}°C")
            print(f"   Min Temperature: {min_temp:.1f}°C")