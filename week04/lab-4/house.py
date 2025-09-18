

class Room:
    def __init__(self, room_type: str, size: int) -> None:
        self.__type = room_type
        self.__size = size
    
    @property
    def type(self)-> str:
        return self.__type
    
    @type.setter
    def type(self, type: str)-> None:
        self.__type = type
        
    @property
    def size(self) -> int:
        return self.__size
    @size.setter
    def size(self, size: int)-> None:
        self.__size = size
        
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
    
    @type.setter
    def type(self, type: str)-> None:
        self.__type = type
        
    @property
    def size(self) -> int:
        return self.__size
    @size.setter
    def size(self, size: int)-> None:
        self.__size = size
    
    @property
    def door_type(self)-> str:
        return self.__door_type
    
    @door_type.setter
    def door_type(self, door_type: str)-> None:
        self.__door_type = door_type
        
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
    
    @screen_type.setter
    def screen_type(self, screen_type: str) -> None:
        self.__screen_type = screen_type
    
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
    
    @price.setter
    def price(self, price: float) -> None:
        self.__price = price
        
    def __str__(self) -> str:
        return f"Television: Screen Type: {self.__screen_type}, Screen Size: {self.__screen_size}, Resolution: {self.__resolution}, Price: {self.__price}"
    def __repr__(self) -> str:
        return str(self)


class House:
    def __init__(self, address: str, square_feet: int, garage: Garage, rooms: list[Room], televisions: list[Television]) -> None:
         self.__address = address
         self.__square_feet = square_feet
         self.__garage = garage
         self.__rooms = rooms
         self.__televisions = televisions
         
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
        
    @property
    def garage(self)-> Garage:
        return self.__garage
    
    @garage.setter
    def garage(self, garage: Garage)-> None:
        self.__garage = garage
        
    @property
    def rooms(self)-> list:
        return self.__rooms
    
    @rooms.setter
    def rooms(self, rooms: list[Room])-> None:
        self.__rooms = rooms
    
    @property
    def televisions(self)-> list:
        return self.__televisions
    
    @televisions.setter
    def televisions(self, televisions: list[Television])-> None:
        self.__televisions = televisions
        
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
    
    g1 = Garage("double", 400, "auto")
    r1 = Room("Bedroom", 200)
    r2 = Room("Kitchen", 150)
    r3 = Room("Living Room", 300)
    tv1 = Television("OLED", 65, "4K", 1200.0)
    tv2 = Television("LCD", 55, "1080p", 600.0)
    
    house1 = House("123 Main St", 2000, g1, [r1, r2, r3], [tv1, tv2])
    
    
    # biggest room
    print("Biggest room:", house1.get_biggest_room())
    
    # get OLED televisions
    print("OLED Televisions:", house1.get_oled_televisions())
    

if __name__ == "__main__":
    main()
    
    