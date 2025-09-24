
class Book:
    def __init__(self, title, author):
        self.__title = title
        self.__author = author
    @property
    def title(self):
        return self.__title
        
    def display(self):
        print(f"{self.__title} by {self.__author}")

class Bookstore:
    def __init__(self, store_name):
        self.__list = []
        self.__store_name = store_name
        
    def add_book(self, book):
        self.__list.append(book)
    
    def displayall(self):
        for book in self.__list:
            book.display()
            
    
    # define the book object as the itterator
    def __iter__(self):
        self.__index = -1 # initialize index for eaach iteration
        return self
    
    # define the metthod that gets the next object
    def __next__(self):
        print(f"__next__ called, index= {self.__index}")
        self.__index += 1
        
        # check if we have reached the end after incrementing
        if self.__index >= len(self.__list):
            print("StopIteration raised - no more items")
            raise StopIteration
        # Get return the book
        book= self.__list[self.__index]
        print(f"Returning book at index {self.__index}: {book.title}")
        return book
    
    
def main():
    print("== Creating Bookstore and Adding Books ==")
    bookstore = Bookstore("My Bookstore")
    bookstore.add_book(Book("1984", "George Orwell"))
    bookstore.add_book(Book("To Kill a Mockingbird", "Harper Lee"))
    bookstore.add_book(Book("The Great Gatsby", "F. Scott Fitzgerald"))
    
    
    # print("\n== using for loop (calls __iter__ and __next__ automatically) ==")
    # for book in bookstore:
    #     book.display()
    #     print("---")
        
    print("== Manual iteration using iter() and next() ==")
    iteration = iter(bookstore) # calls __iter__()
    print("Geting first book:")
    book1 = next(iteration) # calls __next__()
    book1.display()
     
    print("\nGetting second book:")
    book2 = next(iteration) # calls __next__()
    book2.display()
    
    print("\nGeting third book:")
    book3 = next(iteration) # calls __next__()
    book3.display()
    
    print("\nTrying to get fourth book (shoul raise StopIteration):")
    try:
        book4 = next(iteration) 
        
    except StopIteration:
        print("No more books - StopIteration caught")
        
if __name__ == "__main__":
    main()


