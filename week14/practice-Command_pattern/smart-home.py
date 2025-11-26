from abc import ABC , abstractmethod

# Recivers (the actual devices) 

class Light:
    
    def __init__(self, location):
        self.location = location
        self.is_on = False
        
    def turn_on(self):
        self.is_on = True
        print(f"{self.location} light is ON")
        
    def turn_off(self):
        self.is_on = False
        print(f"{self.location} light is OFF")
        
class TV:
    def __init__(self):
        self.is_on = False
        self.channel = 1
        
    def turn_on(self):
        self.is_on= True
        print("Tv is ON")
    
    def turn_off(self):
        self.is_on = False
        print("Tv is OFF")
    def set_channel(self, channel):
        self.channel = channel
        print(f"Tv channel set to {channel}")
        
    
    
# Command Interface

class Command(ABC):
    
    @abstractmethod
    def execute(self):
        pass
    
    @abstractmethod
    def undo(self):
       pass
   


# Concreate Commands

class LightOnCommand(Command):
     def __init__(self, light: Light):
         self.light = light
     def execute(self):
         self.light.turn_on()
         
     def undo(self):
         self.light.turn_off()  
         
class LightOffCommand(Command):
     def __init__(self, light: Light):
         self.light = light
     def execute(self):
         self.light.turn_off()
         
     def undo(self):
         self.light.turn_on()  
    
class TVOnCommand(Command):
    def __init__(self, tv: TV):
        self.tv = tv
        
    def execute(self):
        self.tv.turn_on()
        self.tv.set_channel(1)
        
    def undo(self):
        self.tv.turn_off()
        
        
# Invoker (Remote Control)


class RemoteControl:
    
    def __init__(self):
        self.commands = {} # button_name: command
        self.history = []
        
    def set_command(self, button_name, command: Command):
        self.commands[button_name] = command
        
    def press_button(self, button_name):
        
        if button_name in self.commands:
            command = self.commands[button_name]
            command.execute() 
            self.history.append(command)
        else: 
            print(f"No command assigned to {button_name}")
            
    def press_undo(self):
        if self.history:
            command = self.history.pop()
            command.undo()
            print("Undo executed")
        else: 
            print("Nothing to undo")
    

# Client (Using the system)

def main():
    
    # create devices (recivers)
    living_room_light = Light("Living Room")
    bed_room_light = Light("Bedroom")
    tv = TV()
    
    # create commands 
    living_light_on = LightOnCommand(living_room_light)
    living_light_off = LightOffCommand(living_room_light)
    bed_light_on = LightOnCommand(bed_room_light)
    tv_on = TVOnCommand(tv)
    
    # create remote control(invoker)
    remote = RemoteControl()
    
    # Program the remote buttons
    remote.set_command("button1", living_light_on)
    remote.set_command("button2", living_light_off)
    remote.set_command("button3", bed_light_on)
    remote.set_command("button4", tv_on)
    
    # use the remote 
    print("====Using Remote Control====")
    remote.press_button("button1")  # turn on living room light
    remote.press_button("button4")  # turn on tv
    remote.press_button("button3") # turn on bedroom light
    
    print("\n=== Undo Operations ===")
    remote.press_undo()  # Undo bedroom light
    remote.press_undo() # Undo TV
    remote.press_undo() # Undo living room light
    
if __name__ == "__main__":
    main()
     
    
    
            
        