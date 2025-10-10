class Room:
    def __init__(self, room_type: str, size: int) -> None:
        self.__type = room_type
        self.__size = size
    @property
    def size(self) -> int:
        return self.__size
        
    def __str__(self) -> str:
        return f"Room: Type: {self.__type}, Size: {self.__size} sq.ft"
    

class Garage:
    def __init__(self, garage_type: str, size: int, door_type: str) -> None:
        self.__type = garage_type
        self.__size = size
        self.__door_type = door_type
    @property
    def size(self) -> int:
        return self.__size
    
    @size.setter
    def size(self, size: int) -> None:
        self.__size = size
    def __str__(self) -> str:
        return f"Garage: Type: {self.__type}, Size: {self.__size} sq.ft, Door Type: {self.__door_type}"
    
    
class Television:
    def __init__(self, screen_type: str, screen_size: int, resolution: str, price: float) -> None:
        self.__screen_type = screen_type
        self.__screen_size = screen_size
        self.__resolution = resolution
        self.__price = price
        
        
    @property
    def screen_type(self) -> str:
        return self.__screen_type
        
    def __str__(self) -> str:
        return f"Television: Screen Type: {self.__screen_type}, Screen Size: {self.__screen_size}, Resolution: {self.__resolution}, Price: {self.__price}"
    
    
class House:
    def __init__(self, address: str, square_feet: int, garage_type: str, size: int, door_type: str) -> None:
        self.__address = address
        self.__square_feet = square_feet
        self.__garage = Garage(garage_type, size, door_type)
        self.__rooms: list[Room] = []
        self.__televisions: list[Television] = []
        
    def add_room(self, type: str, size: int) -> None:
        if len(self.__rooms) == 4:
            print("No more rooms can be added")
            return
        self.__rooms.append(Room(type, size))
        
    def add_television(self, television: Television) -> None:
        self.__televisions.append(television)
        
    @property
    def rooms(self) -> list[Room]:
        return self.__rooms
        
    def __str__(self) -> str:
        output: str = f"Adress: {self.__address}\n"
        output += f"Square Feet: {self.__square_feet}\n"
        output += f'Garage: {self.__garage}\n'
        output += "Rooms:\n"
        for room in self.__rooms:
            output += f"{room}\n"
        output += "Televisions:\n"
        for television in self.__televisions:
            output += f"{television}\n"
        return output
    
    def __eq__(self, other):
        if not isinstance(other, House):
            return False
        return self.__address == other.__address
    def remove_television(self, television: Television)-> None:
        self.__televisions.remove(television)
        
    def change_garage_size(self, size: int) -> None:
        self.__garage.size = size
        
    def get_biggest_room(self) -> Room:
    
        biggest = self.__rooms[0]
        for room in self.__rooms:
            if room.size > biggest.size:
                biggest = room
        return biggest
    
    def get_oled_televisions(self) -> list[Television]:
        oled_televisions = []
        for television in self.__televisions:
            if television.screen_type == "OLED":
                oled_televisions.append(television)
        return oled_televisions
    
    def is_similar_house(self, other) -> bool:
        
        if not isinstance(other, House):
            return False
        
        if len(self.__rooms) == len(other.__rooms):
            total_room_size = 0
            for room in self.__rooms:
                total_room_size += room.size
            total_room_size_other = 0
            for room in other.__rooms:
                total_room_size_other += room.size
            if total_room_size == total_room_size_other:    
                return True
            else:
                return False
        else:
            return False
        



def main():
    h1 = House("123 Main St", 2000, "Attached", 2, "Wood")
   
    
    h1.add_room("Bedroom", 100)
    h1.add_room("Kitchen", 50)
    h1.add_room("Living Room", 150)
    h1.add_room("Bathroom", 50)
    
  
    
    h1.add_television(Television("OLED", 65, "4K", 1200))
    h1.add_television(Television("LCD", 45, "1080p", 800))
    h1.add_television(Television("OLED", 55, "8K", 1600))
    
    print(h1)
    
    
    
            
if __name__ == "__main__": 
    
    main()
        