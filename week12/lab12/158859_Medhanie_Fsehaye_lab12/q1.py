
from __future__ import annotations
from abc import ABC, abstractmethod

class Node(ABC):
    def __init__(self, content: str, attributes: dict[str, str]) -> None:
        self.__content = content 
        self.__attributes = attributes
        self.__children: list[Node] = []
        
    def appendChild(self, child: Node):
        self.__children.append(child)
    
    
   
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
        return self.__children.copy()
    
    
class Div(Node):
    def html(self) -> str:
        output = '<div' 
        
        for k, v in self.attributes.items():
            
            output += ' ' + k + '="' + v + '"'
        output += '>'
        
        for child in self.children:
            output += child.html()
            
        output += self.content
        output += '</div>'
        return output
class B(Node):
    def html(self) -> str:
        output = '<b' 
        
        for k, v in self.attributes.items():
            
            output += ' ' + k + '="' + v + '"'
        output += '>'
        
        for child in self.children:
            output += child.html()
            
        output += self.content
        output += '</b>'
        return output
    
class Body(Node):
    def html(self) -> str:
        output = '<body' 
        
        for k, v in self.attributes.items():
            
            output += ' ' + k + '="' + v + '"'
        output += '>'
        
        for child in self.children:
            output += child.html()
            
        output += self.content
        output += '</body>'
        return output
class Title(Node):
    def html(self) -> str:
        output = '<title' 
        
        for k, v in self.attributes.items():
            
            output += ' ' + k + '="' + v + '"'
        output += '>'
        
        for child in self.children:
            output += child.html()
            
        output += self.content
        output += '</title>'
        return output
    
class Head(Node):
    def html(self) -> str:
        output = '<head' 
        
        for k, v in self.attributes.items():
            
            output += ' ' + k + '="' + v + '"'
        output += '>'
        
        for child in self.children:
            output += child.html()
            
        output += self.content
        output += '</head>'
        return output

class Html(Node):
    
    def html(self) -> str:
        output = '<!DOCTYPE html><html' 
        
        for k, v in self.attributes.items():
            
            output += ' ' + k + '="' + v + '"'
        output += '>'
        
        for child in self.children:
            output += child.html()
            
        output += self.content
        output += '</html>'
        return output
    

def main():
    divAtts = {}
    divAtts['id'] = 'first'
    divAtts['class'] = 'foo'
    divA = Div('This is a test A', divAtts)
    
    divAtts = {}
    divAtts['id'] = 'second'
    divAtts['class'] = 'bar'
    divB = Div('This is a test B', divAtts)
    
    divAtts = {}
    divAtts['id'] = 'third'
    divAtts['class'] = 'dump'
    divC = Div('This is a test C', divAtts)
    
    b = B('This is a simple HTML file',{})
    divC.appendChild(b)
    
    body = Body('',{})
    body.appendChild(divA)
    body.appendChild(divB)
    body.appendChild(divC)
    
    
    title = Title('Example', {})
    head = Head('', {})
    head.appendChild(title)
    
    htmlAtts = {}
    htmlAtts['lang'] = 'en'
    html = Html('', htmlAtts)
    html.appendChild(head)
    html.appendChild(body)
    print(html.html())
    
if __name__ == "__main__":
    main()




        

    
