from abc import ABC , abstractmethod

class Light:
    def on(self) -> None:
        print("Turning on the light.")
        
    def off(self) -> None:
        print("Turning off the light.")
class Fan:
    def start(self) ->None:
        print("starting the fan.")
        
    def stop(self) -> None:
        print("Stoping the fan")
        
# Commands

class Command(ABC):
    @abstractmethod
    def execute(self) -> None:
        pass
    
class LightOnCommand(Command):
    def __init__(self, obj: Light) -> None:
        self.__obj = obj
        
    def execute(self) -> None:
        self.__obj.on()
        
class LightOffCommand(Command):
    def __init__(self, obj: Light) -> None:
        self.__obj = obj
        
    def execute(self) -> None:
        self.__obj.off()
        
class FanStartCommand(Command):
    def __init__(self, obj: Fan) -> None:
        self.__obj = obj
        
    def execute(self) -> None:
        self.__obj.start()
        
class FanStopCommand(Command):
    def __init__(self, obj: Fan) -> None:
        self.__obj = obj
        
    def execute(self) -> None:
        self.__obj.stop()
        
    
# Invoker

class RemoteControl:
    
    def __init__(self) -> None:
        self.__lightOnCommand = None
        self.__lightOffCommand = None
        self.__fanStartCommand = None
        self.__fanStopCommand = None
        
    def setCommand(self, command: Command) -> None:
        if isinstance(command, LightOnCommand):
            self.__lightOnCommand = command
        elif isinstance(command, LightOffCommand):
            self.__lightOffCommand = command
        elif isinstance(command, FanStartCommand):
            self.__fanStartCommand = command
        elif isinstance(command, FanStopCommand):
            self.__fanStopCommand = command
            
    def lightOnButtonPressed(self) -> None:
        if self.__lightOnCommand:
            print("Light ON button pressed")
            self.__lightOnCommand.execute()
        else:
            print("Light ON command not set!")
    
    def lightOffButtonPressed(self) -> None:
        if self.__lightOffCommand:
            print("Light OFF button pressed")
            self.__lightOffCommand.execute()
        else:
            print("Light OFF command not set!")
        
    def fanStartButtonPressed(self) -> None:
        if self.__fanStartCommand:
            print("Fan START button pressed")
            self.__fanStartCommand.execute()
        else:
            print("Fan START command not set!")
    
    def fanStopButtonPressed(self) -> None:
        if self.__fanStopCommand:
            print("Fan STOP button pressed")
            self.__fanStopCommand.execute()
        else:
            print("Fan STOP command not set!")
            
    def display_status(self) -> None:
        
        if self.__lightOnCommand:
            print("Ligh ON Command Set")
        else:
            print("Ligh ON Command Not Set")
            
        if self.__lightOffCommand:
            print("Ligh OFF Command Set")
        else:
            print("Ligh OFF Command Not Set")
            
        if self.__fanStartCommand:
            print("Fan START Command Set")
        else:
            print("Fan START Command Not Set")
        
        if self.__fanStopCommand:
            print("Fan STOP Command Set")
        else:
            print("Fan STOP Command Not Set")
    
def main():
    
    light = Light()
    fan = Fan()
    control = RemoteControl()
    control.setCommand(LightOnCommand(light))
    control.setCommand(LightOffCommand(light))
    control.setCommand(FanStartCommand(fan))
    control.setCommand(FanStopCommand(fan))
    control.display_status()
    
    # testing light command
    control.lightOnButtonPressed()
    control.lightOffButtonPressed()
    control.lightOnButtonPressed()
    
    # test fan commands
    control.fanStartButtonPressed()
    control.fanStopButtonPressed()
    
    
    
if __name__ == "__main__":
    main()
    
        
    