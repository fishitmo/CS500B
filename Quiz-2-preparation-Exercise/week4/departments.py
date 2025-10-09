class Professor:
    def __init__(self, professor_name: str, full_time: bool, salary: float) -> None:
        self.__professor_name = professor_name
        self.__full_time = full_time
        self.__salary = salary
    
    
    
    @property
    def full_time(self) -> bool:
        return self.__full_time
    
    def __str__(self):
        return f"Professor: {self.__professor_name}, Full Time: {self.__full_time}, Salary: {self.__salary}"
    
    
class Building:
    def __init__(self, building_name: str, stories: int) -> None:
        self.__building_name = building_name
        self.__stories = stories
        
    @property
    def building_name(self) -> str:
        return self.__building_name
    
    @property
    def stories(self) -> int:
        return self.__stories
    
    def __str__(self):
        return f"Building: {self.__building_name}, Stories: {self.__stories}"
    
class Department:
    def __init__(self, deptname: str) -> None:
        self.__deptname = deptname
        self.__professors: list[Professor] = []
        self.__buildings: list[Building] = []
        
        
    @property
    def professors(self) -> list[Professor]:
        return self.__professors
    
    @property
    def buildings(self) -> list[Building]:
        return self.__buildings
    
   
    def add_professor(self, professor: Professor) -> None:
        self.__professors.append(professor)      # aggregation
        
    def add_building(self, building_name: str, stories: int) -> None:
        self.__buildings.append(str(Building(building_name, stories))) # compostion
        
    def add_building2(self, building: Building) -> None:
        building2 = Building(building.building_name, building.stories)
        self.__buildings.append(building2) # compostion
        
    def get_fulltime_proffesors(self) -> list[Professor]:
        
        professors: list[Professor] = []
        
        for prof in self.__professors:
            if prof.full_time:
                professors.append(str(prof))
        
        return professors
    
    
    
def main():
    p1 = Professor("John", True, 1000)
    p2 = Professor("Jane", False, 2000)
    p3 = Professor("Jack", True, 3000)
    
    p4 = Professor("Lily", True, 1000)
    p5 = Professor("Kevin", False, 2000)
    p6 = Professor("Fsehaye", True, 3000)
    
    d1 = Department("CSE")
    d2 = Department("EEE")
    
    d1.add_building("Science Lab", 2)   # Composition
    d2.add_building("Hardware Lab", 2)  # Composition
    
    
    d1.add_professor(p1)
    d1.add_professor(p2)
    d1.add_professor(p3)
    
    d2.add_professor(p4)
    d2.add_professor(p5)
    d2.add_professor(p6)
    
    
    
    
    print(d1.get_fulltime_proffesors())
    print(d2.get_fulltime_proffesors())
    
    print(d1.buildings)
    print(d2.buildings)

if __name__ == "__main__":
    
    main()
    
    
    
    
    