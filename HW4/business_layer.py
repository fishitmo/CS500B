from data_layer import ( Catalog, Book, Movie, Periodical, 
                        Article, CoverType, FormatType, 
                        PeriodicalType, CatalogRepository)


class Library:
    
    
    def __init__(self, library_name: str) -> None:
        
        self.__library_name = library_name
        self.__items: list[Catalog] = []
    
    @property
    def library_name(self) -> str:
        return self.__library_name
    
    # made this to use a copy of it in the presenttation layer 
    @property
    def items(self) -> list[Catalog]:
        return self.__items.copy()
    
    def __eq__(self, other) -> bool:
        if isinstance(other, Library):
            return self.__library_name == other.library_name
        return False
    def __str__(self) -> str:
        
        output: str = f"Library: {self.__library_name}\n"
        output += f"Total Items: {len(self.__items)}\n"
        
        return output
    
    def add_item(self, item: Catalog) -> None:
        self.__items.append(item)
        
    def remove_item(self, catalog_num: int) -> None:
        i = 0
        while i < len(self.__items):
            if self.__items[i].catalog_num == catalog_num:
                self.__items[i] = self.__items[-1]
                self.__items.pop()
            else:
                i +=1
                
    def update_item(self, item: Catalog) -> None:
        
        i = 0
        while i < len(self.__items):
            if self.__items[i].catalog_num == item.catalog_num:
                self.__items[i] = item
                return 
            i +=1
                
    def search_by_catalog_num(self, catalog_num: int) -> Catalog| None:
        i =0 
        
        while i < len(self.__items):
            if self.__items[i].catalog_num == catalog_num:
                return self.__items[i]
            i +=1
            
        return None 
    
    def search_by_title(self, title: str) -> list[Catalog]:
        
        results: list[Catalog] = []
        title_lower = title.lower()
        
        i =0 
        while i< len(self.__items):
            if title_lower in self.__items[i].title.lower():
                results.append(self.__items[i])
                
            i +=1
            
        return results
    
    def search_by_subject(self, subject: str) -> list[Catalog]:
        
        results: list[Catalog] = []
        subject_lower = subject.lower()
        
        i= 0
        
        while i < len(self.__items):
            item  = self.__items[i]
            # check it item is Book or Movie because both have subject attribute
            if isinstance(item, (Book,  Movie)):
                if subject_lower in item.subject.lower():
                    results.append(item)
                    
            i +=1
            
        return results
    
    def search_by_article_title(self, title: str) -> list[Article]:
        
        results: list[Article] = []
        title_lower = title.lower()
        
        i =0 
        while  i < len(self.__items):
            
            item = self.__items[i]
            
            if isinstance(item, Periodical):
                j=0
                while j < len(item.articles):
                    article = item.articles[j]
                    if title_lower in article.title.lower():
                        results.append(article)
                    j += 1
            i +=1
        return results
    
    
    def get_books_by_covertype(self, cover_type: CoverType)-> list[Book]:
        
        results: list[Book] = []
        
        i = 0
        while i < len(self.__items):
            item = self.__items[i]
            if isinstance(item, Book):
                if item.cover_type == cover_type:
                    results.append(item)
            i +=1
        return results
    

    def get_movies_by_movie_format(self, format_type: FormatType) -> list[Movie]:
        results: list[Movie] = []
        
        i = 0
        while i < len(self.__items):
            item = self.__items[i]
            if isinstance(item, Movie):
                if item.format_type == format_type:
                    results.append(item)
            i +=1
        return results
    
    def save_to_db(self, filename: str = "D:/SFBU/CS500B/HW4/catalog_data.csv") -> None:
        
        
        repository = CatalogRepository(filename)
        repository.save_items(self.__items)
        print(f" Library data saved to {filename}")
    
    def read_from_db(self, filename: str = "D:/SFBU/CS500B/HW4/catalog_data.csv")-> None:
        
        repository = CatalogRepository(filename)
        items = repository.get_items()
        
        self.__items = []
        
        # Add loaded items
        i = 0
        while i < len(items):
            self.__items.append(items[i])
            i += 1
        
        print(f"  Library data loaded from {filename}")
        print(f"  Loaded {len(self.__items)} items")
    
    
        
    

    
    
    
            