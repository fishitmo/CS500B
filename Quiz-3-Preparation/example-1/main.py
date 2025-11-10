from observerInterface import Observer
from subjectInterface import Subject
from displayInterface import Display
from weatherData import WeatherData
from currentConditionDisplay import CurrentConditionDisplay
from statisticalDisplay import StatisticlaDisplay

def main():
    
    print("=" * 60)
    print("WEATHER MONITORING SYSTEM - OBSERVER PATTERN DEMO")
    print("=" * 60)
    
    # Create the Subject (WeatherData)
    weather_data = WeatherData()
    
    print("\n--- PHASE 1: Creating Observers ---")
    # Create Observers - they auto-register in their constructors
    current_display = CurrentConditionDisplay(weather_data)
    statistics_display = StatisticlaDisplay(weather_data)
    
    print("\n--- PHASE 2: First Weather Update ---")
    # Simulate new weather measurements
    weather_data.setMeasurement(25.0, 65.0, 1013.1)
if __name__ == "__main__":
    main()



