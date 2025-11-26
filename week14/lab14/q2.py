from abc import ABC, abstractmethod

# Receiver

class Database:
    def insert(self) -> None:
        print("Inserting a record into the database.")
        
    def update(self) -> None:
        print("Updating a record into the database.")
        
    def deletr(self) ->None:
        print("Deleting a record into the database.")
        
class Command(ABC):
     @abstractmethod
     def execute(self) -> None:
         pass
     
