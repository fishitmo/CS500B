class Book:
    def __init__(self, title, author):
        self.__title = title
        self.__author = author
        self.__pages: list[Page] = []
        
    def __str__(self):
        
        # return self.__title  , self.__author in a separate lines
        return f'Book:\nTitle: {self.__title}\nAuthor: {self.__author}'
               
    
    def add_page(self, text):
        page = Page(text, book=self)
        self.__pages.append(page)
        return page
    
    
class Page:
    def __init__(self, text, book):
        self.__text = text
        self.__book = book
        
    def __str__(self):
        return self.__text
        
book = Book("Title", "Author")
page = book.add_page("Text")

print(book)
print(page)
               
            
        
        
    