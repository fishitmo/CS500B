class Book:
    def __init__(self, title, author = "", price = 0.0):
        self.__title = title
        self.__author = author
        self.price = price
        
    @property
    def title(self):
        return self.__title
    
    @title.setter
    def title(self, title):
        self.__title = title
        
    @property
    def author(self):
        return self.__author
    
    @author.setter
    def author(self, author):
        self.__author = author
        
    def __str__(self):
        return f"{self.__title} by {self.__author} costs {self.price}"
    
    