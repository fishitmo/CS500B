from enum import Enum
from abc import ABC , abstractmethod
import csv

class PeriodicalType(Enum):
    JOURNAL = "JOURNAL"
    MAGAZINE = "MAGAZINE"
    NEWSPAPER = "NEWSPAPER"
    

class CoverType(Enum):
    HARDCOVER = "HARDCOVER"
    PAPERBACK = "PAPERBACK"
    CLOTHCOVER = "CLOTHCOVER"
    
class FormatType(Enum):  
    DVD = "DVD"
    BLU_RAY = "BLU_RAY"
    VCD = "VCD"
    

class Catalog(ABC):
    
    def __init__(self, catalog_num: int , title: str, published_date: str) -> None:
        
        self.__catalog_num = catalog_num
        self.__title = title
        self.__published_date = published_date
        
    @property
    def catalog_num(self) -> int:
        return self.__catalog_num
    
    @property
    def published_date(self)-> str:
        return self.__published_date
    
    @property
    def title(self) -> str:
        return self.__title
           
    def __eq__(self, other) -> bool:
        if isinstance(other, Catalog):
            return self.__catalog_num == other.catalog_num
        return False
    
    @abstractmethod
    def __str__(self):
        pass

class Article:
    
    def __init__(self,title: str, author: str, issue_date: str, periodical_title: str) -> None:
        
        self.__title = title
        self.__author = author
        self.__issue_date = issue_date        
        self.__periodical_title = periodical_title
    @property
    def title(self) -> str:
        return self.__title
    
    @property
    def author(self)->str:
        return self.__author
    
    @property
    def issue_date(self)-> str:
        return self.__issue_date
    
    @property
    def periodical_title(self) -> str:
        return self.__periodical_title
    
    def __str__(self)-> str:
        
        return (f"Article: '{self.__title}', by {self.__author}\n"
                f"        Published: {self.__issue_date} in {self.__periodical_title}")
        
class Periodical(Catalog):
    
    def __init__(self, catalog_num: int, title: str, published_date: str, periodical_type: PeriodicalType):
        
        super().__init__(catalog_num, title, published_date)
        self.__periodical_type = periodical_type
        self.__articles: list[Article] = []
        
    @property
    def periodical_type(self) -> PeriodicalType:
        return self.__periodical_type 
    
     
    @property
    def articles(self) -> list[Article]:
        return self.__articles.copy()
    def add_article(self,article_title: str, author: str, issue_date: str) -> Article:
        article = Article(article_title, author, issue_date, self.title)
        self.__articles.append(article)
        return article
    
    def __str__(self) -> str:
        
        output: str = f"[PERIODICAL] Catalog #: {self.catalog_num}\n"
        output += f"Title: {self.title}\n"
        output += f"Published: {self.published_date}\n"
        output += f"Type: {self.__periodical_type.value}\n"
        output += f"Number of Articles: {len(self.__articles)}"
        if not self.__articles:
            output += "No items in the order.\n"
        else:
            output += "\nArticles:\n"
            for article in self.__articles:
                output += f"  - {article.title} by {article.author} ({article.issue_date})\n"
        
        return output
                
class Book(Catalog):
    
    def __init__(self, catalog_num: int, title: str, published_date: str, cover_type: CoverType, subject: str, author: str) -> None:
        super().__init__(catalog_num, title, published_date)    
        self.__cover_type = cover_type
        self.__subject = subject
        self.__author = author
    
    @property
    def cover_type(self) -> CoverType:
        return self.__cover_type
    
    @property
    def subject(self)-> str:
        return self.__subject
    
    @property
    def author(self) -> str:
        return self.__author
    
    def __str__(self) -> str:
        
        output = f"[Book] Catalog #: {self.catalog_num}\n"
        output +=f"Title: {self.title}\n"
        output +=f"Author: {self.__author}\n"
        output += f"Published: {self.published_date}\n"
        output += f"Cover Type: {self.__cover_type.value}\n"
        output += f"Subject: {self.__subject}\n"
        
        return output
   
class Movie(Catalog):
    
    
    def __init__(self, catalog_num: int, title: str, published_date: str, subject: str, format_type: FormatType, director: str, actors: str, year: int, length: int) -> None:
          super().__init__(catalog_num, title, published_date)
          
          self.__subject = subject
          self.__format_type = format_type
          self.__director = director
          self.__actors = actors
          self.__year = year
          self.__length = length 
          
    @property
    def subject(self) -> str:
        return self.__subject
    
    @property
    def format_type(self) -> FormatType:
        return self.__format_type
    
    @property
    def director(self) -> str:
        return self.__director
    
    @property
    def actors(self) -> str:
        return self.__actors
    
    @property
    def year(self) -> int:
        return self.__year
    
    @property
    def length(self)-> int:
        self.__length
     
    def __str__(self) -> str:
    
        output: str = f"[MOVIE] Catalog #: {self.catalog_num}\n"
        output += f"Title: {self.title}\n"
        output += f"Director: {self.__director}\n"
        output += f"Actors: {self.__actors}\n"
        output += f"Year: {self.__year}\n"
        output += f"Length: {self.__length} minutes\n"
        output += f"Published: {self.published_date}\n"
        output += f"Format: {self.__format_type.value}\n"
        output += f"Subject: {self.__subject}\n"
        
        return output

class CatalogRepository:
    def __init__(self, filename: str) ->None:
        self.__filename = filename
        
    @property
    def filename(self) -> str:
        return self.__filename
    
    def get_items(self) -> list[Catalog]:
        
        items = []
        periodicals_dict = {}  # Dictionary to store periodicals by catalog_num for article linking
        
        try:
            with open(self.__filename, 'r', newline='') as file:
                reader = csv.reader(file)
                line_num = 0
                
                while True:
                    try:
                        row = next(reader)
                        line_num += 1
                    except StopIteration:
                        break
                    except csv.Error as e:
                        print(f"Warning: Skipping malformed CSV line {line_num}: {e}")
                        continue
                    
                    # Skip empty rows
                    if not row or len(row) == 0:
                        continue
                    
                    item_type = row[0]
                    
                    try:
                        if item_type == 'BOOK':
                            # BOOK: TYPE,catalog_num,title,published_date,cover_type,subject,author
                            if len(row) != 7:
                                print(f"Warning: Skipping invalid BOOK row at line {line_num}: expected 7 fields, got {len(row)}")
                                continue
                            
                            book = Book(
                                catalog_num=int(row[1]),
                                title=row[2],
                                published_date=row[3],
                                cover_type=CoverType[row[4]],  # Convert string to enum
                                subject=row[5],
                                author=row[6]
                            )
                            items.append(book)
                        
                        elif item_type == 'MOVIE':
                            # MOVIE: TYPE,catalog_num,title,published_date,subject,format_type,director,actors,year,length
                            if len(row) != 10:
                                print(f"Warning: Skipping invalid MOVIE row at line {line_num}: expected 10 fields, got {len(row)}")
                                continue
                            
                            movie = Movie(
                                catalog_num=int(row[1]),
                                title=row[2],
                                published_date=row[3],
                                subject=row[4],
                                format_type=FormatType[row[5]],  # Convert string to enum
                                director=row[6],
                                actors=row[7],
                                year=int(row[8]),
                                length=int(row[9])
                            )
                            items.append(movie)
                        
                        elif item_type == 'PERIODICAL':
                            # PERIODICAL: TYPE,catalog_num,title,published_date,periodical_type
                            if len(row) != 5:
                                print(f"Warning: Skipping invalid PERIODICAL row at line {line_num}: expected 5 fields, got {len(row)}")
                                continue
                            
                            periodical = Periodical(
                                catalog_num=int(row[1]),
                                title=row[2],
                                published_date=row[3],
                                periodical_type=PeriodicalType[row[4]]  # Convert string to enum
                            )
                            items.append(periodical)
                            # Store in dictionary for article linking
                            periodicals_dict[periodical.catalog_num] = periodical
                        
                        elif item_type == 'ARTICLE':
                            # ARTICLE: TYPE,title,author,issue_date,periodical_catalog_num
                            if len(row) != 5:
                                print(f"Warning: Skipping invalid ARTICLE row at line {line_num}: expected 5 fields, got {len(row)}")
                                continue
                            
                            periodical_catalog_num = int(row[4])
                            
                            # Find the parent periodical
                            if periodical_catalog_num in periodicals_dict:
                                parent_periodical = periodicals_dict[periodical_catalog_num]
                                # Add article to the periodical using composition
                                parent_periodical.add_article(
                                    article_title=row[1],
                                    author=row[2],
                                    issue_date=row[3]
                                )
                            else:
                                print(f"Warning: Article at line {line_num} references non-existent periodical catalog #{periodical_catalog_num}")
                        
                        else:
                            print(f"Warning: Unknown item type '{item_type}' at line {line_num}")
                    
                    except (ValueError, KeyError, IndexError) as e:
                        print(f"Warning: Error parsing line {line_num}: {e}")
                        continue
        
        except FileNotFoundError:
            print(f"Warning: File '{self.__filename}' not found. Starting with empty catalog.")
            return []
        except IOError as e:
            print(f"Warning: Error reading file '{self.__filename}': {e}")
            return []
        
        return items
    
    def save_items(self, items: list[Catalog]) -> None:
        with open(self.__filename, 'w', newline='') as file:
            writer = csv.writer(file)
            
            i = 0
            
            while i < len(items):
                item = items[i]
                
                if isinstance(item, Book):
                   writer.writerow([
                        'BOOK',
                        item.catalog_num,
                        item.title,
                        item.published_date,
                        item.cover_type.value,
                        item.subject,
                        item.author
                    ])
                   
                elif isinstance(item, Movie):
                     writer.writerow([
                        'MOVIE',
                        item.catalog_num,
                        item.title,
                        item.published_date,
                        item.subject,
                        item.format_type.value,
                        item.director,
                        item.actors,
                        item.year,
                        item.length
                    ])
                     
                elif isinstance(item, Periodical):
                    writer.writerow([
                        'PERIODICAL',
                        item.catalog_num,
                        item.title,
                        item.published_date,
                        item.periodical_type.value
                    ])
                    
                    # writes all articels for this periodical
                    j = 0
                    while j < len(item.articles):
                        article = item.articles[j]
                        writer.writerow([
                            'ARTICLE',
                            article.title,
                            article.author,
                            article.issue_date,
                            item.catalog_num        # Reference to parent periodical
                        ])
                        j += 1
                
                i += 1
                
    
                                          

        
        