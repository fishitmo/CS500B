from abc import ABC, abstractmethod, abstractproperty

class Movable(ABC):
    @abstractmethod
    def move(self) -> None:
        pass

class Displayable(ABC):
    @abstractmethod
    def display(self) -> None:
        pass

class Flyable(ABC):
    @abstractmethod
    def fly(self) -> None:
        pass

class Part(Displayable):
    def __init__(self, partno: int, price: float) -> None:
        self.__partno = partno
        self.__price = price

    def __str__(self) -> str:
        return f"partno = {self.__partno}\nprice = {self.__price}"
    
    def display(self) -> None:
        print(self)

    def __eq__(self, __value: object) -> bool:
        if isinstance(__value, Part):
            return self.__partno == __value.__partno
        else:
            return False
    @property
    def partno(self) -> int:
        return self.__partno
    @property
    def price(self) -> float:
        return self.__price
        
class Machine(Displayable):
    def __init__(self, machine_name: str) -> None:
        self.__machine_name = machine_name
        self.__parts: list[Part] = []     # the list may have duplicates

    @property
    def machine_name(self) -> str:       # comment out by @fishitmo
        return self.__machine_name

    def add_part(self, part: Part) -> None:
        self.__parts.append(part)

    def __str__(self) -> str:
        output = f"machine_name = {self.__machine_name}\n"
        output += "The machine has these parts:\n"
        for part in self.__parts:
            output += str(part) + "\n\n"
        return output

    def display(self) -> None:
        print(self)

    @abstractmethod
    def dowork(self) -> None:
        pass
    
    def get_duplicated_parts(self) -> dict[int, int]:
        part_freq: dict[int, int] = {}
        
        for part in self.__parts:
            if part.partno not in part_freq:
                part_freq[part.partno] = 1  # the first time
            else:
                part_freq[part.partno] += 1 # increment occurences
        
        duplicated_parts: dict[int, int] = {}
        for partno, occurences in part_freq.items():
            if occurences > 1:
                duplicated_parts[partno] = occurences
                        
        return duplicated_parts
    
    def remove_part_by_partno(self, partno: int) -> None:
        i= 0 
        while i < len(self.__parts):
            if self.__parts[i].partno == partno:
                self.__parts[i] = self.__parts[-1]
                self.__parts.pop()
            else:
                i += 1
    def __iter__(self):
        self.__index = 0 # initialize index for each iteration
        return self

    def __next__(self):
        
        if self.__index < len(self.__parts):
            part = self.__parts[self.__index]
            self.__index += 1
            return part
        else:
            raise StopIteration   

class JetFighter(Displayable, Flyable):
    def __init__(self, model: str, speed: int) -> None:
        self.__model = model
        self.__speed = speed

    def __str__(self) -> str:
        return f"model = {self.__model}\nspeed = {self.__speed}"
    
    def display(self) -> None:
        print(self)

    def fly(self) -> None:
        print(f"The JetFigher {self.__model} is flying in the sky!")
        
    

class Robot(Machine, JetFighter):
    def __init__(self, machine_name: str, cpu: str, model: str, speed: int) -> None:
        Machine.__init__(self, machine_name)
        JetFighter.__init__(self, model, speed)
        self.__processor = cpu

    def dowork(self) -> None:
        print(f"The Robot {self.machine_name} is assembling a big truck.")
    
    def __str__(self) -> str:
        return f"processor = {self.__processor}\n" + Machine.__str__(self) + JetFighter.__str__(self)
    
        
    def fly(self) -> None:
        super().fly()
        print(f"The Robot {self.machine_name} is flying over the ocean!")
    
    
        
    def get_expensive_parts(self, price_limit: float) -> list[Part]:
        
        
        expensive_parts: list[Part] = []
        for part in self:
            if part.price >= price_limit:
                expensive_parts.append(part)
        return expensive_parts
    def get_movable_parts_bytype(self) -> dict[str,list[Part]]:
        movable_by_type: dict[str, list[Part]] = {}
        for part in self:
            if isinstance(part, MovablePart):
                if part.type not in movable_by_type:
                    movable_by_type[part.type] = []
                movable_by_type[part.type].append(part)    
        return movable_by_type
    def get_movable_parts(self) -> list['MovablePart']:
        movable_parts: list[MovablePart] = []
        for part in self:
            if isinstance(part, MovablePart):
                movable_parts.append(part)
        return movable_parts
class MovablePart(Movable, Part):
    def __init__(self, partno: int, price: float, type: str) -> None:
        Part.__init__(self, partno, price)
        self.__type = type
    
    @property
    def type(self) -> str:
        return self.__type
    
    def __str__(self) -> str:
        return  super().__str__() + "\n" + f"type = {self.__type}"
        
    def display(self) -> None:
        print(self)
        
    def move(self) -> None:
        print(f"partno: {self.partno} is moving fast!")
        
        

def main():
    robo = Robot('MTX', 'M1X', 'F-16', 10000)
    robo.add_part(Part(111, 100))
    robo.add_part(Part(222, 200))
    robo.add_part(Part(333, 300))
    robo.add_part(Part(222, 300))
    robo.add_part(MovablePart(555, 300, "TypeA"))
    robo.add_part(Part(111, 100))
    robo.add_part(Part(111, 100))
    robo.add_part(MovablePart(777, 300, "TypeB"))
    robo.add_part(MovablePart(655, 300, "TypeA"))
    robo.add_part(MovablePart(755, 300, "TypeA"))
    robo.add_part(MovablePart(977, 300, "TypeB"))
    robo.display()
    print()
    
   
    
    print("\nRobot test flight----")
    robo.fly()
    
    print("\nRobot dowork() test ----")
    robo.dowork()

    print("\nDuplicated part list----")
    
    partfreq = robo.get_duplicated_parts()
    for partno in partfreq.keys():
        print(partno,'=>', partfreq[partno], 'times')
        
    print("\nExpensive part list----")
    expensive_parts = robo.get_expensive_parts(200)
    for part in expensive_parts:
            part.display()
    print("\nMovable part list----")
    movable_parts = robo.get_movable_parts_bytype()
    for type, parts in movable_parts.items():
            print("type =", type)
            for part in parts:
                part.display()
            print()
    print("\nAsk movable to move----")
    movable_parts = robo.get_movable_parts()
    for part in movable_parts:
            part.move()
            
    print("\nTest remove_part() ----")
    robo.remove_part_by_partno(333)
    for part in robo:
        if part.partno == 333:
            print('Found 333')
            break


if __name__ == "__main__":
    main()