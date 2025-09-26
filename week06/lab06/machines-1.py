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

    # @property
    # def machine_name(self) -> str:       # comment out by @fishitmo
    #     return self.__machine_name

    def add_part(self, part: Part) -> None:
        self.__parts.append(part)

    def __str__(self) -> str:
        output = "machine_name = {self.__machine_name}"
        output += "The machine has these parts:\n"
        for part in self.__parts:
            output += str(part) + "\n\n"
        return output

    def display(self) -> None:
        print(self)

    @abstractmethod
    def dowork(self) -> None:
        pass
    
    def get_duplicate_parts(self) -> dict[int, int]:
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
        return f"processor = {self.__processor}\n" + super().__str__()
    
    def fly(self) -> None:
        super().fly()
        print(f"The Robot {self.machine_name} is flying in the ocean!")
        
    def get_expensive_parts(self, price_limit: float) -> list[Part]:
        
        # we need to define an itterators using __iter__ and __next__

def main():
    robo = Robot('MTX', 'M1X', 'F-16', 10000)
    robo.add_part(Part(111, 100))
    robo.add_part(Part(222, 200))
    robo.add_part(Part(333, 300))
    robo.add_part(Part(222, 300))
    robo.add_part(Part(111, 100))
    robo.add_part(Part(111, 100))
    robo.display()
    print()
    
   
    
    print("\nRobot test flight----")
    robo.fly()
    
    print("\nRobot dowork() test ----")
    robo.dowork()

    
    


if __name__ == "__main__":
    main()