from data_layer import (
    Book, Movie, Periodical, Article,
    CoverType, FormatType, PeriodicalType,
    CatalogRepository
)

print("=" * 70)
print("TEST: CSV Read Functionality")
print("=" * 70)

# Test 1: Read from the sample catalog_data.csv file
print("\n--- Test 1: Read from catalog_data.csv ---")
repo = CatalogRepository("D:/SFBU/CS500B/HW4/catalog_data.csv")
items = repo.get_items()
print(f"Loaded {len(items)} items from catalog_data.csv")

# Count items by type
book_count = sum(1 for item in items if isinstance(item, Book))
movie_count = sum(1 for item in items if isinstance(item, Movie))
periodical_count = sum(1 for item in items if isinstance(item, Periodical))

print(f"\nItem breakdown:")
print(f"  Books: {book_count}")
print(f"  Movies: {movie_count}")
print(f"  Periodicals: {periodical_count}")
print(f"  Total: {len(items)}")

# Test 2: Verify book details
print("\n--- Test 2: Verify Book Details ---")
book = next((item for item in items if isinstance(item, Book) and item.catalog_num == 111), None)
if book:
    print(f"  Found book with catalog #111:")
    print(f"  Title: {book.title}")
    print(f"  Author: {book.author}")
    print(f"  Published: {book.published_date}")
    print(f"  Cover Type: {book.cover_type.value}")
    print(f"  Subject: {book.subject}")
else:
    print("  Book with catalog #111 not found")

# Test 3: Verify movie details
print("\n--- Test 3: Verify Movie Details ---")
movie = next((item for item in items if isinstance(item, Movie) and item.catalog_num == 221), None)
if movie:
    print(f"  Found movie with catalog #221:")
    print(f"  Title: {movie.title}")
    print(f"  Director: {movie.director}")
    print(f"  Actors: {movie.actors}")
    print(f"  Year: {movie.year}")
    print(f"  Length: {movie.length} minutes")
    print(f"  Format: {movie.format_type.value}")
    print(f"  Subject: {movie.subject}")
else:
    print("  Movie with catalog #221 not found")

# Test 4: Verify periodical with articles
print("\n--- Test 4: Verify Periodical with Articles ---")
periodical = next((item for item in items if isinstance(item, Periodical) and item.catalog_num == 332), None)
if periodical:
    print(f"  Found periodical with catalog #332:")
    print(f"  Title: {periodical.title}")
    print(f"  Type: {periodical.periodical_type.value}")
    print(f"  Articles: {len(periodical.articles)}")
    
    if len(periodical.articles) > 0:
        print("\n  Article details:")
        for i, article in enumerate(periodical.articles, 1):
            print(f"    {i}. {article.title}")
            print(f"       Author: {article.author}")
            print(f"       Date: {article.issue_date}")
            print(f"       In: {article.periodical_title}")
else:
    print("  Periodical with catalog #332 not found")

# Test 5: Display all items
print("\n--- Test 5: Display All Items ---")
for item in items:
    print(f"\n{item}")

# Test 6: Test round-trip (save and read back)
print("\n--- Test 6: Round-Trip Test (Save and Read) ---")
# Create new items
test_items = []
test_items.append(Book(999, "Test Book", "Jan 1, 2023", CoverType.PAPERBACK, "Testing", "Test Author"))
test_items.append(Movie(888, "Test Movie", "Jan 1, 2023", "Action", FormatType.BLU_RAY, 
                       "Test Director", "Actor One, Actor Two", 2023, 100))

test_periodical = Periodical(777, "Test Journal", "Jan 1, 2023", PeriodicalType.JOURNAL)
test_periodical.add_article("Test Article 1", "Author A", "Jan 1, 2023")
test_periodical.add_article("Test Article 2", "Author B", "Jan 2, 2023")
test_items.append(test_periodical)

# Save items
repo_test = CatalogRepository("test_roundtrip.csv")
repo_test.save_items(test_items)
print(f"Saved {len(test_items)} items to test_roundtrip.csv")

# Read items back
loaded_items = repo_test.get_items()
print(f"Loaded {len(loaded_items)} items from test_roundtrip.csv")

# Verify counts match
assert len(loaded_items) == len(test_items), "Item count mismatch!"
print("  Item count matches")

# Verify the periodical has articles
loaded_periodical = next((item for item in loaded_items if isinstance(item, Periodical)), None)
if loaded_periodical:
    article_count = len(loaded_periodical.articles)
    print(f"  Loaded periodical has {article_count} articles")
    assert article_count == 2, "Article count mismatch!"
    print("  Article count matches")

