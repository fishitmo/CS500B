
from __future__ import annotations
from abc import ABC, abstractmethod

class Node(ABC):
    def __init__(self, content: str, attributes: dict[str, str]) -> None:
        self.__content = content 
        self.__attributes = attributes
        self.__children = list[Node] = []
        
    def appendChild(self, child: Node):
        self.__children.append(child)
    
    def html(self) -> str:
        output = '<' + self.createTag() # Factory Method
        
        for k, v in self.attributes.items():
            pass
    @abstractmethod
    def html(self) -> str:
        pass
        
    @property
    def attributes(self) -> dict[str, str]:
        return self.__attributes
    @property
    def content(self) -> str:
        return self.__content  
    @property
    def children(self) -> list[Node]:
        return self.__children
    
    
class Div(Node):
    def createTag(self) -> str:
        return "div"
    
class B(Node):
    def createTag(self) -> str:
        return "b"
    
class Body(Node):
    def createTag(self) -> str:
        return "body"
    
class Title(Node):
    def createTag(self) -> str:
        return "title"
    
class Head(Node):
    def createTag(self) -> str:
        return "head"

class Html(Node):
    def createTag(self) -> str:
        return "html"
    
    def html(self) -> str:
        return '<!DOCTYPE html>' + super().html()




        

    
