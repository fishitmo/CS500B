from __future__ import annotations
from abc import ABC, abstractmethod

class InvalidStateError(Exception):
    def __init__(self, message: str) -> None:
        self.__message = message
        
    def __str__(self) -> str:
        return f"InvalidStateError: {self.__message}"
    
class State(ABC):
    def __init__(self, name: str) -> None:
        self._state = State
        
    # @property
    # def state(self):
    #     return self.__state
        
    def turn_on(self, light_switch: LightSwitch):
        raise InvalidStateError("Not in OFF or DIM state")
        
    def turn_off(self, light_switch: LightSwitch):
        raise InvalidStateError("Not in ON or DIM state")
        
    def dim(self, light_switch):
        raise InvalidStateError("Not in ON state")
    
class OffState(State):
    def __init__(self) -> None:
        super().__init__("OFF")
        
    def turn_on(self, light_switch: LightSwitch):
        light_switch.state = OnState()
        print("Light is now on.")
        
class OnState(State):
    def __init__(self) -> None:
        super().__init__("ON")
        
    def turn_off(self, light_switch: LightSwitch):
        light_switch.state = OffState()
        print("Light is now off.")
        
    def dim(self, light_switch: LightSwitch):
        light_switch.state = DimState()
        print("Light is now dimmed.")
        
class DimState(State):
    def __init__(self) -> None:
        super().__init__("DIM")
        
    def turn_on(self, light_switch: LightSwitch):
        light_switch.state = OnState()
        print("Light is now on.")
        
    def turn_off(self, light_switch):
        light_switch.state = OffState()
        print("Light is now off.")
        
class LightSwitch:
    def __init__(self) -> None:
        self.__state: State = OffState()
        
    @property
    def state(self) -> State:
        return self.__state
        
    @state.setter
    def state(self, state: State) -> None:
        self.__state = state
        
    def turn_on(self):
        self.__state.turn_on(self)
        
    def turn_off(self):
        self.__state.turn_off(self)
        
    def dim(self):
        self.__state.dim(self)
        
def show_menu():
    print()
    print("====== MENU ======")
    print("1. Turn on")
    print("2. Turn off")
    print("3. Dim")
    print("4. Exit")
    
def main():
    light_switch = LightSwitch()
    while True:
        show_menu()
        choice = input("Enter your choice: ")
        try: 
            if choice == "1":
                light_switch.turn_on()
            elif choice == "2":
                light_switch.turn_off()
            elif choice == "3":
                light_switch.dim()
            elif choice == "4":
                break
            
        except InvalidStateError as err:
            print(f"Could not perform {choice} because {err}")
        
        
