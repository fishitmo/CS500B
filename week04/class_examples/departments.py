class Professor:
    
    def __init__(self, professor_name: str, full_time: bool, salary: float) -> None:
        self.__professor_name = professor_name
        self.__full_time = full_time
        self.__salary = salary
        
    @property
    def full_time(self) -> bool:
        return self._full_time
    
    
class Building:
    
    def __init__(self, building_name: str, stories: int) -> None:
        self.__building_name = building_name
        self.__stories = stories
        
    @property
    def stories(self) -> int:
        return self.__stories
        
class Department:
    
    def __init__(self, deptname: str) -> None:
        self.__deptname = deptname
        self.__professors: list[Professor] = []
        self.__buildings: list[Building] = []
        
    def add_professor(self, professor: Professor) -> None:
        self.__professors.append(professor)   # aggregation
        
    def add_building(self, building_name: str, stories: int) -> None:
        self.__buildings.append(Building(building_name, stories)) # composition
    def add_building2(self, building: Building) -> None:
        building2 = Building(building.building_name , building.stories)
        self.__buildings.append(building2)      # Composition
        
    def get_fulltime_proffesors(self) -> list[Professor]:
        
        professors: list[Professor] = []
        
        for prof in self.__professors:
            if prof.full_time:
                professors.append(prof)
        
        return professors
    
def main():
    p1 = Professor("Fsehaye Medhanie", True, 2000000)
    p2 = Professor("Jane Doe", False, 1000000)
    
    dept1 = Department("CS")
    dept2 = Department("EE")
    
    dept1.add_building("Science Lab", 2)   # Composition
    dept2.add_building("Hardware Lab", 2)  # Composition
    
    
    dept1.add_professor(p1)       # aggreagation    
    
    dept1.add_professor(p2)       # aggreagation
    
    a: int = 10
    
    print("a =", a)
    
if __name__ == "__main__":
    main()
        
     
        
        
        