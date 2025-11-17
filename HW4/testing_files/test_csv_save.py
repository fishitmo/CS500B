from data_layer import (
    Book, Movie, Periodical, Article,
    CoverType, FormatType, PeriodicalType,
    CatalogRepository
)

print("=" * 70)
print("TEST: CSV Save Functionality")
print("=" * 70)

# Create test items
print("\n--- Step 1: Create Test Items ---")
items = []

# Add books
book1 = Book(111, "Programming in C++", "Feb 2, 2023", CoverType.HARDCOVER, "Programming", "Peter")
items.append(book1)
print(f"Created: {book1.title}")

book2 = Book(121, "Advanced Programming in C++", "Jun 6, 2022", CoverType.HARDCOVER, "Programming", "Lily")
items.append(book2)
print(f"Created: {book2.title}")

# Add movie
movie1 = Movie(221, "Star Wars", "May 25, 1977", "Adventure", FormatType.DVD,
               "George Lucas", "Mark Hamill,Harrison Ford,Carrie Fisher", 1977, 121)
items.append(movie1)
print(f"Created: {movie1.title}")

# Add periodicals with articles
periodical1 = Periodical(331, "Wall Street Journal 167(15)", "Oct 23, 2023", PeriodicalType.JOURNAL)
periodical1.add_article("Market Trends 2023", "John Doe", "Oct 23, 2023")
periodical1.add_article("Tech Industry Analysis", "Jane Smith", "Oct 23, 2023")
items.append(periodical1)
print(f"Created: {periodical1.title} with {len(periodical1._Periodical__articles)} articles")

periodical2 = Periodical(332, "Time 168(18)", "Oct 26, 2023", PeriodicalType.MAGAZINE)
periodical2.add_article("Elon Musk's Struggle for AI", "Walter Isaacson", "Oct 26, 2023")
items.append(periodical2)
print(f"Created: {periodical2.title} with {len(periodical2._Periodical__articles)} article")

print(f"\nTotal items created: {len(items)}")

# Save to CSV
print("\n--- Step 2: Save Items to CSV ---")
repo = CatalogRepository("test_catalog.csv")
repo.save_items(items)
print(f"Items saved to {repo.filename}")

# Read and display the CSV file
print("\n--- Step 3: Display CSV File Contents ---")
with open("test_catalog.csv", 'r') as file:
    lines = file.readlines()
    print(f"Total lines in CSV: {len(lines)}")
    print("\nCSV Contents:")
    print("-" * 70)
    for i, line in enumerate(lines, 1):
        print(f"{i:2}. {line.strip()}")
    print("-" * 70)

# Verify CSV format
print("\n--- Step 4: Verify CSV Format ---")
with open("test_catalog.csv", 'r') as file:
    import csv
    reader = csv.reader(file)
    rows = list(reader)
    
    print(f"Total rows: {len(rows)}")
    
    # Count each type
    book_count = sum(1 for row in rows if row[0] == 'BOOK')
    movie_count = sum(1 for row in rows if row[0] == 'MOVIE')
    periodical_count = sum(1 for row in rows if row[0] == 'PERIODICAL')
    article_count = sum(1 for row in rows if row[0] == 'ARTICLE')
    
    print(f"Books: {book_count} (expected 2)")
    print(f"Movies: {movie_count} (expected 1)")
    print(f"Periodicals: {periodical_count} (expected 2)")
    print(f"Articles: {article_count} (expected 3)")
    
    # Verify structure
    print("\n--- Step 5: Verify Row Structure ---")
    for row in rows:
        if row[0] == 'BOOK':
            assert len(row) == 7, f"Book row should have 7 fields, got {len(row)}"
            print(f"BOOK row: catalog_num={row[1]}, title={row[2]}")
        elif row[0] == 'MOVIE':
            assert len(row) == 10, f"Movie row should have 10 fields, got {len(row)}"
            print(f"MOVIE row: catalog_num={row[1]}, title={row[2]}")
        elif row[0] == 'PERIODICAL':
            assert len(row) == 5, f"Periodical row should have 5 fields, got {len(row)}"
            print(f"PERIODICAL row: catalog_num={row[1]}, title={row[2]}")
        elif row[0] == 'ARTICLE':
            assert len(row) == 5, f"Article row should have 5 fields, got {len(row)}"
            print(f"ARTICLE row: title={row[1]}, periodical_catalog_num={row[4]}")

# Test with special characters
print("\n--- Step 6: Test with Special Characters ---")
special_items = []
book_special = Book(999, "Test Book: \"Quotes\" & Commas, Here", "Jan 1, 2023",
                   CoverType.PAPERBACK, "Testing,Commas", "Author, Name")
special_items.append(book_special)

repo.save_items(special_items)
print("Saved item with special characters (quotes, commas)")

with open("test_catalog.csv", 'r', encoding='utf-8') as file:
    content = file.read()
    print("\nCSV Content with special characters:")
    print(content)