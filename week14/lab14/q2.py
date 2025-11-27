from abc import ABC, abstractmethod

# Receiver

class Database:
    def insert(self) -> None:
        print("Inserting a record into the database.")
        
    def update(self) -> None:
        print("Updating a record into the database.")
        
    def delete(self) ->None:
        print("Deleting a record into the database.")
        
class Command(ABC):
     @abstractmethod
     def execute(self) -> None:
         pass
     
class InsertCommand(Command):
    def __init__(self, obj: Database) -> None:
        self.__obj = obj
        
    def execute(self) -> None:
        self.__obj.insert()
        
class UpdateCommand(Command):
    def __init__(self, obj: Database) -> None:
        self.__obj = obj
    
    def execute(self) -> None:
        self.__obj.update()
        
class DeleteCommand(Command):
    def __init__(self, obj: Database) -> None:
        self.__obj = obj
    
    def execute(self) -> None:
        self.__obj.delete()
        
    
# Invoker


class Client:
    
    def __inti__(self) -> None:
        self.__command = None
        
        
    def setCommand(self, command: Command) -> None:
        
        self.__command = command
        print("Command Set")
       
    def executeCommand(self) -> None:
        
        if self.__command:
            print("Executing Command")
            self.__command.execute()
            
            
        else:
            print("No Command Set to  execute")
            
  
  
def main():
    
    
    db = Database()
    client = Client()
    
    print("\nTesting Insert Operation\n")
    insert_cmd1 = InsertCommand(db)
    client.setCommand(insert_cmd1)
    client.executeCommand()
   
    
    print("\nTesting Update operations\n")
    
    update_cmd = UpdateCommand(db)
    client.setCommand(update_cmd)
    client.executeCommand()
    
    print("\nTesting Delete Operations\n")
    
    delete_cmd = DeleteCommand(db)
    client.setCommand(delete_cmd)
    client.executeCommand()
    


if __name__ =="__main__":
    main()
    


        
    
     
