

class Room:
    def __init__(self, room_type: str, size: int) -> None:
        self.__type = room_type
        self.__size = size
    
    @property
    def type(self)-> str:
        return self.__type
    
    
        
    @property
    def size(self) -> int:
        return self.__size
    
        
    def __str__(self) -> str:
        return f"Room: Type: {self.__type}, Size: {self.__size} sq.ft"
    
    def __repr__(self) -> str:
        return str(self)

class Garage:
    def __init__(self, garage_type: str, size: int, door_type: str) -> None:
        self.__type = garage_type
        self.__size = size
        self.__door_type = door_type
        
    @property
    def type(self)-> str:
        return self.__type
    
    
        
    @property
    def size(self) -> int:
        return self.__size
   
    
    @property
    def door_type(self)-> str:
        return self.__door_type
    
    
        
    def __str__(self) -> str:
        return f"Garage: Type: {self.__type}, Size: {self.__size} sq.ft, Door Type: {self.__door_type}"
    
    def __repr__(self) -> str:
        return str(self)

class Television:
    def __init__(self, screem_type: str, screen_size: int, resolution: str, price: float ) -> None:
        self.__screen_type = screem_type
        self.__screen_size = screen_size
        self.__resolution = resolution
        self.__price = price
     
    @property
    def screen_type(self)-> str:
        return self.__screen_type
    
    
    
    @property
    def screen_size(self) -> int:
        return self.__screen_size
    
    @screen_size.setter
    def sceen_size(self, screen_size: int) -> None:
        self.__screen_size = screen_size
        
    @property
    def resolution(self) -> str:
        return self.__resolution
    
    @resolution.setter
    def resolution(self, resolution: str) -> None:
        self.__resolution = resolution
        
    @property
    def price(self) -> float:
        return self.__price
    
    
        
    def __str__(self) -> str:
        return f"Television: Screen Type: {self.__screen_type}, Screen Size: {self.__screen_size}, Resolution: {self.__resolution}, Price: {self.__price}"
    def __repr__(self) -> str:
        return str(self)


class House:
    def __init__(self, address: str, square_feet: int, garage_type: str, size: int, door_type: str, room_data: list[tuple[str, int]]) -> None:
         self.__address = address
         self.__square_feet = square_feet
         self.__garage = Garage(garage_type, size, door_type)
         self.__rooms = []
         for room_type, size in room_data:
             self.__rooms.append(Room(room_type, size))
         self.__televisions = []
         
    @property
    def address(self)-> str:
        return self.__address
    
    @address.setter
    def address(self, address: str)-> None:
        self.__address = address
        
    @property
    def square_feet(self) -> int:
        return self.__square_feet
    @square_feet.setter
    def square_feet(self, square_feet: int)-> None:
        self.__square_feet = square_feet
        
   
        
    # Tv management
    def add_television(self, television: Television)-> None:
        self.__televisions.append(television)
        
    def remove_television(self, television: Television)-> None:
        self.__televisions.remove(television)
    
    # garage management
    def change_garage_size(self, size: int)-> None:
        self.__garage.size = size
    
    def get_biggest_room(self)-> Room:
        if not self.__rooms:
            return None
        
        biggest = self.__rooms[0]
        for room in self.__rooms:
            if room.size > biggest.size:
                biggest = room
        return biggest
    
    def get_oled_televisions(self)-> list[Television]:
        oled_list = []
        for tv in self.__televisions:
            if tv.screen_type.upper() == 'OLED':
                oled_list.append(tv)
        return oled_list
    
    def is_similar_house(self, other)-> bool:
        
        return self == other
    
    def __eq__(self, other) -> bool:
        # two houses are similar if they have the same square feet and the same number of rooms
        
        if not isinstance(other, House):
            return False
        
        # count rooms
        count_self = 0
        for _ in self.__rooms:
            count_self += 1
        count_other = 0
        for _ in other.__rooms:
            count_other += 1
        
        return self.__square_feet == other.__square_feet and count_self == count_other
    
    def __str__(self) -> str:
        rooms_str = "["
        first = True
        for room in self.__rooms:
            if not first:
                rooms_str += ", "
            rooms_str += str(room)
            first = False
        rooms_str += "]"

        # Build television strings manually
        tvs_str = "["
        first = True
        for tv in self.__televisions:
            if not first:
                tvs_str += ", "
            tvs_str += str(tv)
            first = False
        tvs_str += "]"
        
        return f"House: Address: {self.__address}, Square Feet: {self.__square_feet}, Garage: {self.__garage}, Rooms: {rooms_str}, Televisions: {tvs_str}"
    
    def __repr__(self) -> str:
        return str(self)
    
    
    
def main():
    
    room_info = [
        ("Living Room", 300),
        ("Bedroom", 200),
        ("Kitchen", 150),
        ("Bathroom", 120)
            ]
    house1 = House("123 Main St", 2000, 
              garage_type="double", size=400, door_type="automatic",
              room_data=room_info)
    house1.add_television(Television("OLED", 65, "4K", 1200))
    house1.add_television(Television("LCD", 55, "1080p", 600))
    house1.add_television(Television("OLED", 65, "4K", 1200))
    house1.add_television(Television("OLED", 65, "4K", 1200))
    
    print(house1)
    
    house2 = House("456 Elm St", 3000, 
              garage_type="double", size=400, door_type="automatic",
              room_data=room_info)
    house2.add_television(Television("OLED", 65, "4K", 1200))
    house2.add_television(Television("OLED", 65, "4K", 1200))
    house2.add_television(Television("OLED", 65, "4K", 1200))
    house2.add_television(Television("OLED", 65, "4K", 1200))
    # remove a television
    # house2.remove_television(Television("OLED", 65, "4K", 1200))
    
    print(house2)
    
    print("Similar Houses:", house1.is_similar_house(house2))
    
    
    # biggest room
    print("Biggest room:", house1.get_biggest_room())
    
    # get OLED televisions
    print("OLED Televisions:", house1.get_oled_televisions())
    
    print("Similar Houses:", house1.is_similar_house(house2))

if __name__ == "__main__":
    main()
    
    