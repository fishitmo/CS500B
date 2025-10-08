class Book:
    def __init__(self, title, author, price) -> None:
        self.__title = title
        self.__author = author
        self.__price = price
        
    def display(self):
        print('Title:', self.__title)
        print('Author:', self.__author)
        print('Price:', self.__price)

class Bookstore:
    def __init__(self, store_name):
        self.__list = []
        self.__store_name = store_name
        
    def add_book(self, book):
        self.__list.append(book)
        
    # def displayall(self):
    #     for book in self.__list:
    #         book.display()
    # define the Book object as the iterator
    def __iter__(self):
        self.__index = -1
        return self
    
    # define the method that gets the next object
    def __next__(self):
        if self.__index >= len(self.__list) -1:
            raise StopIteration
        self.__index += 1
        book = self.__list[self.__index]
        return book

            
            
def main():
    b1 = Book('The Alchemist', 'Paulo Coelho', 300)
    b2 = Book('The Great Gatsby', 'F. Scott Fitzgerald', 400)
    b3 = Book('The Lord of the Rings', 'J. R. R. Tolkien', 500)
    b4 = Book('To Kill a Mockingbird', 'Harper Lee', 300)
    
    bookstore = Bookstore('Fish-Bookstore')
    bookstore.add_book(b1)
    bookstore.add_book(b2)
    bookstore.add_book(b3)
    bookstore.add_book(b4)
    
    # bookstore.displayall()
    
    for book in bookstore:
        book.display()
        print()
    
if __name__ == '__main__':
    main()