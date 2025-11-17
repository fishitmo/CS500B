from business_layer import Library
from data_layer import (
    CatalogRepository, Catalog, Book, Movie, Periodical, Article,
    CoverType, FormatType, PeriodicalType
)


class LibraryApp:
    
    def __init__(self) -> None:
        
        self.__repository = CatalogRepository("D:/SFBU/CS500B/HW4/catalog_data.csv")
        items = self.__repository.get_items()
        
        self.__library = Library("City Library")
        
        i = 0
        while i < len(items):
            self.__library.add_item(items[i])
            i += 1
            
    def show_program_title(self) -> None:
        
        print()
        print("=" * 70)
        print("           LIBRARY CATALOG MANAGEMENT SYSTEM")
        print("=" * 70)
        print(f"           Welcome to {self.__library.library_name}")
        print("=" * 70)
        print()
        
    def show_menu(self) -> None:
       
        print("===== LIBRARY CATALOG SYSTEM =====")
        print("1. Add Book")
        print("2. Add Movie")
        print("3. Add Periodical")
        print("4. Add Article to Periodical")
        print("5. Remove Item")
        print("6. Search by Catalog Number")
        print("7. Search by Title")
        print("8. Search by Subject")
        print("9. List Books by Cover Type")
        print("10. List All Books")
        print("11. List All Movies")
        print("12. List All Periodicals")
        print("13. Display All Items")
        print("14. Save Data to File")
        print("0. Exit")
        print("Enter your choice: ", end="")
        
    def process_command(self) -> None:
      
        while True:
            self.show_menu()
            choice = input().strip()
            print() 
            
            if choice == "0":
                # Exit
                print("Thank you for using the Library Catalog System!")
                print("Goodbye!")
                break
            
            elif choice == "1":
                # Add Book
                self.__add_book()
            
            elif choice == "2":
                # Add Movie
                self.__add_movie()
            
            elif choice == "3":
                # Add Periodical
                self.__add_periodical()
            
            elif choice == "4":
                # Add Article to Periodical
                self.__add_article()
            
            elif choice == "5":
                # Remove Item
                self.__remove_item()
            
            elif choice == "6":
                # Search by Catalog Number
                self.__search_by_catalog_num()
            
            elif choice == "7":
                # Search by Title
                self.__search_by_title()
            
            elif choice == "8":
                # Search by Subject
                self.__search_by_subject()
            
            elif choice == "9":
                # List Books by Cover Type
                self.__list_books_by_cover_type()
            
            elif choice == "10":
                # List All Books
                self.__list_all_books()
            
            elif choice == "11":
                # List All Movies
                self.__list_all_movies()
            
            elif choice == "12":
                # List All Periodicals
                self.__list_all_periodicals()
            
            elif choice == "13":
                # Display All Items
                self.__display_all_items()
                
            elif choice == "14":
                # Save Data to File
                self.__save_data()
            
            else:
                print(f"Invalid choice: '{choice}'. Please try again.")
            
            print()  
            
    def __add_book(self) -> None:
        
        print("=== Add Book ===")
        try:
            catalog_num = int(input("Enter catalog number: "))
            title = input("Enter title: ")
            published_date = input("Enter published date: ")
            
            # Show cover type options
            print("\nCover Types:")
            print("1. HARDCOVER")
            print("2. PAPERBACK")
            print("3. CLOTHCOVER")
            cover_choice = input("Select cover type (1-3): ")
            
            if cover_choice == "1":
                cover_type = CoverType.HARDCOVER
            elif cover_choice == "2":
                cover_type = CoverType.PAPERBACK
            elif cover_choice == "3":
                cover_type = CoverType.CLOTHCOVER
            else:
                print("Invalid cover type selection.")
                return
            
            subject = input("Enter subject: ")
            author = input("Enter author: ")
            
            # Create and add book
            book = Book(catalog_num, title, published_date, cover_type, subject, author)
            self.__library.add_item(book)
            print(f"\n Book '{title}' added successfully!")
            
        except ValueError as e:
            print(f"Error: Invalid input - {e}")
        except Exception as e:
            print(f"Error adding book: {e}")
    
    def __add_movie(self) -> None:
       
        print("=== Add Movie ===")
        try:
            catalog_num = int(input("Enter catalog number: "))
            title = input("Enter title: ")
            published_date = input("Enter published date: ")
            subject = input("Enter subject/genre: ")
            
            # Show format type options
            print("\nFormat Types:")
            print("1. DVD")
            print("2. BLU_RAY")
            print("3. VCD")
            format_choice = input("Select format type (1-3): ")
            
            if format_choice == "1":
                format_type = FormatType.DVD
            elif format_choice == "2":
                format_type = FormatType.BLU_RAY
            elif format_choice == "3":
                format_type = FormatType.VCD
            else:
                print("Invalid format type selection.")
                return
            
            director = input("Enter director: ")
            actors = input("Enter actors (comma-separated): ")
            year = int(input("Enter year: "))
            length = int(input("Enter length (minutes): "))
            
            # Create and add movie
            movie = Movie(catalog_num, title, published_date, subject, format_type, 
                         director, actors, year, length)
            self.__library.add_item(movie)
            print(f"\n Movie '{title}' added successfully!")
            
        except ValueError as e:
            print(f"Error: Invalid input - {e}")
        except Exception as e:
            print(f"Error adding movie: {e}")
    
    def __add_periodical(self) -> None:
        
        print("=== Add Periodical ===")
        try:
            catalog_num = int(input("Enter catalog number: "))
            title = input("Enter title: ")
            published_date = input("Enter published date: ")
            
            # Show periodical type options
            print("\nPeriodical Types:")
            print("1. JOURNAL")
            print("2. MAGAZINE")
            print("3. NEWSPAPER")
            type_choice = input("Select periodical type (1-3): ")
            
            if type_choice == "1":
                periodical_type = PeriodicalType.JOURNAL
            elif type_choice == "2":
                periodical_type = PeriodicalType.MAGAZINE
            elif type_choice == "3":
                periodical_type = PeriodicalType.NEWSPAPER
            else:
                print("Invalid periodical type selection.")
                return
            
            # Create and add periodical
            periodical = Periodical(catalog_num, title, published_date, periodical_type)
            self.__library.add_item(periodical)
            print(f"\n Periodical '{title}' added successfully!")
            
        except ValueError as e:
            print(f"Error: Invalid input - {e}")
        except Exception as e:
            print(f"Error adding periodical: {e}")
    
    def __add_article(self) -> None:
        
        print("=== Add Article to Periodical ===")
        try:
            catalog_num = int(input("Enter periodical catalog number: "))
            
            # Search for periodical
            periodical = self.__library.search_by_catalog_num(catalog_num)
            
            if periodical is None:
                print(f"Error: No item found with catalog number {catalog_num}")
                return
            
            if not isinstance(periodical, Periodical):
                print(f"Error: Item {catalog_num} is not a periodical")
                return
            
            print(f"Adding article to: {periodical.title}")
            
            article_title = input("Enter article title: ")
            author = input("Enter author: ")
            issue_date = input("Enter issue date: ")
            
            # Add article to periodical
            periodical.add_article(article_title, author, issue_date)
            print(f"\n Article '{article_title}' added to periodical successfully!")
            
        except ValueError as e:
            print(f"Error: Invalid input - {e}")
        except Exception as e:
            print(f"Error adding article: {e}")
    
    def __remove_item(self) -> None:
        
        print("=== Remove Item ===")
        try:
            catalog_num = int(input("Enter catalog number to remove: "))
            
            # Check if item exists first
            item = self.__library.search_by_catalog_num(catalog_num)
            if item is None:
                print(f"Error: No item found with catalog number {catalog_num}")
                return
            
            print(f"Found: {item.title}")
            confirm = input("Are you sure you want to remove this item? (yes/no): ")
            
            if confirm.lower() == "yes":
                self.__library.remove_item(catalog_num)
                print(f"\n Item removed successfully!")
            else:
                print("Removal cancelled.")
                
        except ValueError as e:
            print(f"Error: Invalid input - {e}")
        except Exception as e:
            print(f"Error removing item: {e}")
    
    def __search_by_catalog_num(self) -> None:
       
        print("=== Search by Catalog Number ===")
        try:
            catalog_num = int(input("Enter catalog number: "))
            
            item = self.__library.search_by_catalog_num(catalog_num)
            
            if item:
                print("\n" + "=" * 70)
                print(item)
            else:
                print(f"\nNo item found with catalog number {catalog_num}")
                
        except ValueError as e:
            print(f"Error: Invalid input - {e}")
    
    def __search_by_title(self) -> None:
        
        print("=== Search by Title ===")
        title = input("Enter title (partial match): ")
        
        results = self.__library.search_by_title(title)
        
        if results:
            print(f"\nFound {len(results)} item(s):")
            print("=" * 70)
            i = 0
            while i < len(results):
                print(results[i])
                print()
                i += 1
        else:
            print(f"\nNo items found with title containing '{title}'")
    
    def __search_by_subject(self) -> None:
       
        print("=== Search by Subject ===")
        subject = input("Enter subject (partial match): ")
        
        results = self.__library.search_by_subject(subject)
        
        if results:
            print(f"\nFound {len(results)} item(s):")
            print("=" * 70)
            i = 0
            while i < len(results):
                print(results[i])
                print()
                i += 1
        else:
            print(f"\nNo items found with subject containing '{subject}'")
    
    def __list_books_by_cover_type(self) -> None:
      
        print("=== List Books by Cover Type ===")
        print("\nCover Types:")
        print("1. HARDCOVER")
        print("2. PAPERBACK")
        print("3. CLOTHCOVER")
        choice = input("Select cover type (1-3): ")
        
        if choice == "1":
            cover_type = CoverType.HARDCOVER
        elif choice == "2":
            cover_type = CoverType.PAPERBACK
        elif choice == "3":
            cover_type = CoverType.CLOTHCOVER
        else:
            print("Invalid cover type selection.")
            return
        
        results = self.__library.get_books_by_covertype(cover_type)
        
        if results:
            print(f"\nFound {len(results)} {cover_type.value} book(s):")
            print("=" * 70)
            i = 0
            while i < len(results):
                print(results[i])
                print()
                i += 1
        else:
            print(f"\nNo {cover_type.value} books found")
    
    def __list_all_books(self) -> None:
       
        print("=== All Books ===")
        
        # Get all items and filter for books
        all_items = self.__library.items
        books = []
        i = 0
        while i < len(all_items):
            if isinstance(all_items[i], Book):
                books.append(all_items[i])
            i += 1
        
        if books:
            print(f"\nTotal books: {len(books)}")
            print("=" * 70)
            i = 0
            while i < len(books):
                print(books[i])
                print()
                i += 1
        else:
            print("\nNo books found in the library")
    
    def __list_all_movies(self) -> None:
        
        print("=== All Movies ===")
        
        # Get all items and filter for movies
        all_items = self.__library.items
        movies = []
        i = 0
        while i < len(all_items):
            if isinstance(all_items[i], Movie):
                movies.append(all_items[i])
            i += 1
        
        if movies:
            print(f"\nTotal movies: {len(movies)}")
            print("=" * 70)
            i = 0
            while i < len(movies):
                print(movies[i])
                print()
                i += 1
        else:
            print("\nNo movies found in the library")
    
    def __list_all_periodicals(self) -> None:
        
        print("=== All Periodicals ===")
        
        # Get all items and filter for periodicals
        all_items = self.__library.items
        periodicals = []
        i = 0
        while i < len(all_items):
            if isinstance(all_items[i], Periodical):
                periodicals.append(all_items[i])
            i += 1
        
        if periodicals:
            print(f"\nTotal periodicals: {len(periodicals)}")
            print("=" * 70)
            i = 0
            while i < len(periodicals):
                print(periodicals[i])
                print()
                i += 1
        else:
            print("\nNo periodicals found in the library")
    
    def __display_all_items(self) -> None:
      
        print("=== All Library Items ===")
        print(self.__library)
        
        all_items = self.__library.items
        
        if all_items:
            print("=" * 70)
            i = 0
            while i < len(all_items):
                print(all_items[i])
                print()
                i += 1
        else:
            print("\nLibrary is empty")
    
    def __save_data(self) -> None:
       
        print("=== Save Data to File ===")
        
        # Ask for filename or use default
        filename = input("Enter filename (press Enter for 'D:/SFBU/CS500B/HW4/catalog_data.csv'): ").strip()
        
        if not filename:
            filename = "catalog_data.csv"
        
        # Ensure .csv extension
        if not filename.endswith('.csv'):
            filename += '.csv'
        
        try:
            self.__library.save_to_db(filename)
        except Exception as e:
            print(f"Error saving data: {e}")     
            
            

