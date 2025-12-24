
from __future__ import annotations
from state_machine import (State, Event, acts_as_state_machine,
after, before, InvalidStateTransition)

@acts_as_state_machine
class LightProcess:
    # define 3 states
    OFF = State(initial=True)
    ON = State()
    DIM = State()
    
    
    # define 3 events
    turn_on = Event(from_states=(OFF, DIM), to_state=ON)
    turn_off = Event(from_states=(ON, DIM), to_state=OFF)
    dim = Event(from_states=(ON), to_state=DIM)
    
    def __init__(self, switch: LightSwitch) -> None:
        self.__switch = switch
        
    @before("turn_on")
    def before_turn_on(self):
        confirm = input("Are you sure to turn on the light (y/n)")
        return True if confirm == "y" else False
    @after("turn_on")
    def after_turn_on(self):
        print("Light is ON now.")
        
    @after("turn_off")
    def after_turn_off(self):
        print("Light is OFF now.")
    
    @after("dim")
    def after_dim(self):
        print("Light is DIM now.")
        
class LightSwitch:
    
    def __init__(self) -> None:
        self.__process = LightProcess(self)
        
    def turn_on(self):
        self.__process.turn_on()
    def turn_off(self):
        self.__process.turn_off()
    def dim(self):
        self.__process.dim()
    def get_current_state(self):
        return self.__process.current_state
    
    
def show_menu():
    print()
    print("====== MENU ======")
    print("1. Turn On")
    print("2. Turn Off")
    print("3. Dim")
    print("4. Exit")
def main():
    switch = LightSwitch()
    while True:
        show_menu()
        choice = int(input("Enter your choice: "))
        try:
            if choice == 1:
                switch.turn_on()
            elif choice == 2:
                switch.turn_off()
            elif choice == 3:
                switch.dim()
            elif choice == 4:
                break
        except InvalidStateTransition as err:
            print(f"Could not perform {choice} in {switch.get_current_state()} state")
if __name__ == "__main__":
  main()
  