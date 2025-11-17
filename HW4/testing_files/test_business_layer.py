from data_layer import(
    Book, Movie, Periodical, Article,
    CoverType, FormatType, PeriodicalType
)

from business_layer import Library

print("=" * 70)
print("CRITICAL TEST: Business Layer - Data Layer Integration")
print("=" * 70)

# step 1 Create Library 
print("\n--- Step 1: Create Library ---")
library = Library("City Library")
print(f"Library created: {library.library_name}")
print(library)

# step 2: Create and add test items

print("-- Step-2: Create and Add Test Items--")

# Add Book

book = Book(
    catalog_num= 111,
    title= "Programming in C++",
    published_date="Feb 2, 2023",
    cover_type=CoverType.HARDCOVER,
    subject="Programming",
    author="Peter"
)
library.add_item(book)
print(f"Added Book: {book.title}")

# Add Movie 

movie = Movie(
    catalog_num=221,
    title="Star Wars",
    published_date="May 25, 1977",
    subject="Adventure",
    format_type=FormatType.DVD,
    director="George Lucas",
    actors="Mark Hamill, Harrison Ford, Carrie Fisher",
    year=1977,
    length=121
)

library.add_item(movie)
print(f"Added Movie: {movie.title}")

# Add Periodical

periodical = Periodical(
    catalog_num=331,
    title="Wall Street Journal 167(15)",
    published_date="Oct 23, 2023",
    periodical_type=PeriodicalType.JOURNAL
)

library.add_item(periodical)

print(f"Added Periodical: {periodical.title}")

print(f"\n{library}")

# Step-3: Test search by Catalog number
print("---Step-3: Test search by Catalog Number(111)--")

result = library.search_by_catalog_num(111)
if result:
    print("Found Item with Catalog #111")
    print(f"Title: {result.title}")
    print(f"  Type: {type(result).__name__}")
    if isinstance(result, Book):
        print(f"  Author: {result.author}")
        print(f"  Subject: {result.subject}")
        print(f"  Cover Type: {result.cover_type.value}")
else:
    print("Item not found")
    
# Step 4: Test search by title
print("\n--- Step 4: Test Search by Title ('Star Wars') ---")
results = library.search_by_title("Star Wars")
print(f"Found {len(results)} item(s) with title 'Star Wars':")
for item in results:
    print(f"  - Catalog #{item.catalog_num}: {item.title}")
    if isinstance(item, Movie):
        print(f"    Director: {item.director}")
        print(f"    Year: {item.year}")
        print(f"    Length: {item.length} minutes")

# Step 5: Test search by subject
print("\n--- Step 5: Test Search by Subject ('Programming') ---")
results = library.search_by_subject("Programming")
print(f" Found {len(results)} item(s) with subject 'Programming':")
for item in results:
    print(f"  - Catalog #{item.catalog_num}: {item.title}")
    if isinstance(item, Book):
        print(f"    Author: {item.author}")
        print(f"    Cover Type: {item.cover_type.value}")
        
# Step 6: Test get books by cover type
print("\n--- Step 6: Test Get Books by Cover Type (HARDCOVER) ---")
hardcover_books = library.get_books_by_covertype(CoverType.HARDCOVER)
print(f"Found {len(hardcover_books)} HARDCOVER book(s):")
for book_item in hardcover_books:
    print(f"  - Catalog #{book_item.catalog_num}: {book_item.title}")
    print(f"    Author: {book_item.author}")
    print(f"    Subject: {book_item.subject}")
    
# Additional Test 7: Display all items
print("\n--- Additional Test 7: Display All Items ---")
print("Book Details:")
print(book)
print("\nMovie Details:")
print(movie)
print("\nPeriodical Details:")
print(periodical)

# Additional Test 8: Test equality
print("--- Additional Test 8: Test Catalog Item Equality ---")
book_copy = Book(111, "Different Title", "Different Date", CoverType.PAPERBACK, "Different Subject", "Different Author")
print(f"Original book catalog #: {book.catalog_num}")
print(f"Copy book catalog #: {book_copy.catalog_num}")
print(f"book == book_copy: {book == book_copy}")
print(f"Equality based on catalog number works")

# Additional Test 9: Test Library equality
print("\n--- Additional Test 9: Test Library Equality ---")
library2 = Library("City Library")
library3 = Library("Different Library")
print(f"library == library2: {library == library2}")
print(f"library == library3: {library == library3}")
print(f"Library equality based on name works")


# Additional Test 10: Test update_item
print("\n--- Additional Test 10: Test Update Item ---")
updated_book = Book(
    catalog_num=111,
    title="Advanced Programming in C++",
    published_date="Feb 2, 2023",
    cover_type=CoverType.PAPERBACK,
    subject="Programming",
    author="Peter Smith"
)
library.update_item(updated_book)
result = library.search_by_catalog_num(111)

if isinstance(result, Book):
    print(f"Item updated successfully:")
    print(f"  New Title: {result.title}")
    print(f"  New Author: {result.author}")
    print(f"  New Cover Type: {result.cover_type.value}")


# Additional Test 11: Test remove_item
print("\n--- Additional Test 11: Test Remove Item ---")
print(f"Before removal: {library}")
library.remove_item(331)  # Remove the periodical
print(f"After removing catalog #331:")
print(library)
result = library.search_by_catalog_num(331)
if result is None:
    print("Item successfully removed (search returns None)")
    

# Additional Test 12: Test search by article title (add articles first)
print("\n--- Additional Test 12: Test Search by Article Title ---")
# Add a new periodical with articles
periodical2 = Periodical(332, "Time Magazine 168(18)", "Oct 26, 2023", PeriodicalType.MAGAZINE)
periodical2.add_article("AI Revolution", "John Doe", "Oct 26, 2023")
periodical2.add_article("Climate Change Update", "Jane Smith", "Oct 26, 2023")
library.add_item(periodical2)
print(f"Added periodical with {len(periodical2.articles)} articles")

article_results = library.search_by_article_title("AI")
print(f"Found {len(article_results)} article(s) with 'AI' in title:")
for article in article_results:
    print(f"  - {article.title} by {article.author}")
    print(f"    In: {article.periodical_title}")


# Additional Test 13: Test get movies by format
print("\n--- Additional Test 13: Test Get Movies by Format (DVD) ---")
dvd_movies = library.get_movies_by_movie_format(FormatType.DVD)
print(f"Found {len(dvd_movies)} DVD movie(s):")
for movie_item in dvd_movies:
    print(f"  - {movie_item.title} ({movie_item.year})")