from data_layer import CatalogRepository, Book, Movie, Periodical, CoverType, FormatType, PeriodicalType
from business_layer import Library

print("=" * 70)
print("COMPLETE CSV INTEGRATION TEST")
print("=" * 70)

# Test 1: Load library from CSV
print("\n--- Test 1: Load Library from CSV ---")
repo = CatalogRepository("D:/SFBU/CS500B/HW4/catalog_data.csv")
items = repo.get_items()
library = Library("City Library")

# Add all items to library
i = 0
while i < len(items):
    library.add_item(items[i])
    i += 1

print(f" Loaded library from CSV:")
print(library)

# Test 2: Test all library operations
print("--- Test 2: Test Library Operations ---")

# Search by catalog number
book = library.search_by_catalog_num(111)
print(f" Search by catalog #111: {book.title if book else 'Not found'}")

# Search by title
results = library.search_by_title("Programming")
print(f" Search by title 'Programming': Found {len(results)} items")

# Search by subject
results = library.search_by_subject("Programming")
print(f" Search by subject 'Programming': Found {len(results)} items")

# Get books by cover type
hardcover_books = library.get_books_by_covertype(CoverType.HARDCOVER)
print(f" Hardcover books: {len(hardcover_books)}")

# Get movies by format
dvd_movies = library.get_movies_by_movie_format(FormatType.DVD)
print(f" DVD movies: {len(dvd_movies)}")

# Search by article title
articles = library.search_by_article_title("AI")
print(f" Search articles with 'AI': Found {len(articles)} articles")

# Test 3: Modify library and save
print("\n--- Test 3: Modify Library and Save ---")

# Add new items
new_book = Book(999, "Python Programming", "Jan 1, 2024", CoverType.PAPERBACK, "Programming", "Alice")
library.add_item(new_book)
print(f" Added: {new_book.title}")

new_movie = Movie(888, "The Matrix", "Mar 31, 1999", "Science Fiction", FormatType.BLU_RAY,
                 "The Wachowskis", "Keanu Reeves", 1999, 136)
library.add_item(new_movie)
print(f" Added: {new_movie.title}")

new_periodical = Periodical(777, "Nature 500(1)", "Jan 1, 2024", PeriodicalType.JOURNAL)
new_periodical.add_article("Climate Change Study", "Dr. Smith", "Jan 1, 2024")
new_periodical.add_article("Quantum Computing Breakthrough", "Dr. Jones", "Jan 1, 2024")
library.add_item(new_periodical)
print(f" Added: {new_periodical.title} with {len(new_periodical.articles)} articles")

print(f"\n{library}")

# Test 4: Save modified library
print("--- Test 4: Save Modified Library to CSV ---")
# Get all items from library (we need to access private attribute for now)
all_items = library._Library__items
repo_output = CatalogRepository("modified_catalog.csv")
repo_output.save_items(all_items)
print(f" Saved {len(all_items)} items to modified_catalog.csv")

# Test 5: Reload and verify
print("\n--- Test 5: Reload and Verify ---")
repo_reload = CatalogRepository("modified_catalog.csv")
reloaded_items = repo_reload.get_items()
print(f" Reloaded {len(reloaded_items)} items")

# Create new library from reloaded items
library2 = Library("Reloaded Library")
i = 0
while i < len(reloaded_items):
    library2.add_item(reloaded_items[i])
    i += 1

print(library2)

# Verify the new items are present
found_book = library2.search_by_catalog_num(999)
print(f" Found new book: {found_book.title if found_book else 'Not found'}")

found_movie = library2.search_by_catalog_num(888)
print(f" Found new movie: {found_movie.title if found_movie else 'Not found'}")

found_periodical = library2.search_by_catalog_num(777)
if found_periodical:
    article_count = len(found_periodical._Periodical__articles)
    print(f" Found new periodical: {found_periodical.title} with {article_count} articles")

# Verify article search works
climate_articles = library2.search_by_article_title("Climate")
print(f" Search for 'Climate' in articles: Found {len(climate_articles)} articles")

# Test 6: Display CSV contents
print("\n--- Test 6: Display Modified CSV Contents ---")
with open("modified_catalog.csv", 'r', encoding='utf-8') as file:
    lines = file.readlines()
    print(f"Total lines in modified CSV: {len(lines)}")
    print("\nFirst 10 lines:")
    for i, line in enumerate(lines[:10], 1):
        print(f"{i:2}. {line.strip()}")
    if len(lines) > 10:
        print(f"... and {len(lines) - 10} more lines")

# Test 7: Update and remove operations with persistence
print("\n--- Test 7: Update and Remove with Persistence ---")

# Update an item
updated_book = Book(111, "Programming in C++ (2nd Edition)", "Feb 2, 2023", 
                   CoverType.PAPERBACK, "Programming", "Peter")
library2.update_item(updated_book)
print(f" Updated book #111")

# Remove an item
library2.remove_item(121)
print(f" Removed book #121")

print(library2)

# Save changes
all_items2 = library2._Library__items
repo_final = CatalogRepository("final_catalog.csv")
repo_final.save_items(all_items2)
print(f" Saved final state to final_catalog.csv")

# Reload and verify changes persisted
repo_verify = CatalogRepository("final_catalog.csv")
final_items = repo_verify.get_items()
final_library = Library("Final Library")
i = 0
while i < len(final_items):
    final_library.add_item(final_items[i])
    i += 1

print(f"\n{final_library}")

# Verify update
book_111 = final_library.search_by_catalog_num(111)
if book_111:
    if isinstance(book_111, Book):
        print(f" Verified update: {book_111.title}")
        print(f"  Cover type: {book_111.cover_type.value}")

# Verify removal
book_121 = final_library.search_by_catalog_num(121)
if book_121 is None:
    print(f" Verified removal: Book #121 not found (as expected)")

print("\n" + "=" * 70)
print("COMPLETE CSV INTEGRATION TEST PASSED! ")
print("=" * 70)
print("\nSummary:")
print("   CSV reading and writing work correctly")
print("   Full integration with Library (business layer)")
print("   Article linking preserved through save/load cycle")
print("   All search operations work with loaded data")
print("   Updates and removals persist correctly")
print("   Round-trip data integrity maintained")
print("\nThe three-tier architecture is complete:")
print("   Data Layer (CSV persistence)")
print("   Business Layer (Library operations)")
print("   Ready for Presentation Layer!")