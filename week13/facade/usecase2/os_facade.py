from enum import Enum 
from abc import ABC, abstractmethod, abstractproperty

class State(Enum):
    new = 1
    running = 2
    sleeping = 3
    restart = 4
    zombie = 5

class Server(ABC):
    @abstractmethod
    def __init__(self):
        pass

    def __str__(self):
        return self.name

    @abstractmethod
    def boot(self):
        pass

    @abstractmethod  
    def kill(self, restart=True):
        pass
        
class FileServer(Server): 
    def __init__(self): 
        # actions required for initializing the file server
        self.name = 'FileServer' 
        self.state = State.new 

    def boot(self): 
        print(f'booting the {self}') 
        # actions required for booting the file server
        self.state = State.running 

    def kill(self, restart=True): 
        print(f'Killing {self}') 
        # actions required for killing the file server
        self.state = State.restart if restart else State.zombie 

    def createFile(self, user, name, permissions): 
        # check validity of permissions, user rights, etc.
        print(f"trying to create the file '{name}' for user '{user}' with permissions {permissions}") 
        
class ProcessServer(Server): 
    def __init__(self): 
        # actions required for initializing the process server
        self.name = 'ProcessServer' 
        self.state = State.new 

    def boot(self): 
        print(f'booting the {self}') 
        # actions required for booting the process server
        self.state = State.running 

    def kill(self, restart=True): 
        print(f'Killing {self}') 
        # actions required for killing the process server
        self.state = State.restart if restart else State.zombie 

    def createProcess(self, user, name): 
        # check user rights, generate PID, etc.
        print(f"trying to create the process '{name}' for user '{user}'")        
        
class OperatingSystem: 
    def __init__(self): 
        self.fs = FileServer() 
        self.ps = ProcessServer() 

    def start(self): 
        [i.boot() for i in (self.fs, self.ps)] 
        
    def shutdown(self): 
        [i.kill() for i in (self.fs, self.ps)] 

    def createFile(self, user, name, permissions): 
        return self.fs.createFile(user, name, permissions) 

    def createProcess(self, user, name): 
        return self.ps.createProcess(user, name)       
        
def main():
    os = OperatingSystem() 
    os.start()  
    os.createFile('peter', 'parts.txt', '-rw-r-r') 
    os.createProcess('lily', 'ls /var')
    os.shutdown()
    
if __name__ == "__main__":
    main()