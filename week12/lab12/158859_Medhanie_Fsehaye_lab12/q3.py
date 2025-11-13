
from __future__ import annotations
from abc import ABC, abstractmethod

class Node(ABC):
    def __init__(self, content: str, attributes: dict[str, str]= None) -> None:
        self.__content = content 
        if attributes is not None:    
            self.__attributes = attributes 
        else:
             self.__attributes = {}
        self.__children: list[Node] = []
        
    def appendChild(self, child: Node):
        self.__children.append(child)
    
    def html(self) -> str:
        output = '<' + self.createTag()   # Factory Method
        
        for k, v in self.attributes.items():
            
            output += ' ' + k + '="' + v + '"'
        output += '>'
        
        for child in self.children:
            output += child.html()
            
        output += self.content
        output += '</' + self.createTag() + '>'
        return output
    @abstractmethod
    def createTag(self) -> str:
        pass
        
    @property
    def attributes(self) -> dict[str, str]:
        return self.__attributes
    @property
    def content(self) -> str:
        return self.__content  
    @property
    def children(self) -> list[Node]:
        return self.__children.copy()
    
    
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
        return '<!DOCTYPE html><' + super().html()
 
class AbstractNodeFactory(ABC):
    
    @abstractmethod
    def makeNode(self, node_type: str, content: str , attributes: dict[str, str]):
        pass
    
class StandardNodeFactory(AbstractNodeFactory):
    
    def makeNode(self, node_type: str, content: str = '', attributes: dict[str, str]=None):
        
        node_type = node_type.lower()
        if node_type == 'div':
            return Div(content, attributes)
        elif node_type == 'b':
            return B(content, attributes)
        elif node_type == 'body':
            return Body(content, attributes)
        elif node_type == 'title':
            return Title(content, attributes)
        elif node_type == 'head':
            return Head(content, attributes)
        elif node_type == 'html':
            return Html(content, attributes)
        else:
            raise ValueError(f"Unknown node type: {node_type}. "
                           f"Supported types: div, b, body, title, head, html")
            
class DebugNodeFactory(AbstractNodeFactory):

    def __init__(self):
        self.__standard_factory = StandardNodeFactory()
    

        
    def makeNode(self, node_type: str, content: str= '', attributes: dict[str, str]= None)-> Node:
        node = self.__standard_factory.makeNode(node_type, content, attributes)
        
        print(f"{node_type.capitalize()} node is created.")
        
        return node 
def main():
    
    
    # factory = StandardNodeFactory()
    factory = DebugNodeFactory()
    
    divAtts = {}
    divAtts['id'] = 'first'
    divAtts['class'] = 'foo'
    divA = factory.makeNode('div','This is a test A', divAtts)
    
    divAtts = {}
    divAtts['id'] = 'second'
    divAtts['class'] = 'bar'
    divB = factory.makeNode('div','This is a test B', divAtts)
    divAtts = {}
    divAtts['id'] = 'third'
    divAtts['class'] = 'dump'
    divC = factory.makeNode('div','This is a test C', divAtts)
    
    b = factory.makeNode('b','This is a simple HTML file')
    divC.appendChild(b)
    
    body = factory.makeNode('body')
    body.appendChild(divA)
    body.appendChild(divB)
    body.appendChild(divC)
    
    title = factory.makeNode('title','Example')
    
    
    head = factory.makeNode('head')
    head.appendChild(title)
    
    htmlAtts = {}
    htmlAtts['lang'] = 'en'
    html = factory.makeNode('html', '',htmlAtts)
    html.appendChild(head)
    html.appendChild(body)
    print(html.html())
    
if __name__ == "__main__":
       main()




        

    
