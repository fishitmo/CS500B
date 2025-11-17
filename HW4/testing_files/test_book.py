"""
Quick Test for Book Class
Tests the Book class functionality
"""

from data_layer import Book, CoverType

print("=" * 60)
print("QUICK TEST: Book Class")
print("=" * 60)

# Test 1: Create a hardcover book
print("\n--- Test 1: Creating a Hardcover Book ---")
book1 = Book(
    catalog_num=111,
    title="Programming in C++",
    published_date="Feb 2, 2023",
    cover_type=CoverType.HARDCOVER,
    subject="Programming",
    author="Peter"
)
print("[OK] Book created successfully")
print(f"  Catalog Number: {book1.catalog_num}")
print(f"  Title: {book1.title}")
print(f"  Author: {book1.author}")
print(f"  Cover Type: {book1.cover_type.value}")
print(f"  Subject: {book1.subject}")

# Test 2: Display book using __str__
print("\n--- Test 2: Display Book Information ---")
print(book1)

# Test 3: Create a paperback book
print("--- Test 3: Creating a Paperback Book ---")
book2 = Book(
    catalog_num=121,
    title="Advanced Programming in C++",
    published_date="Jun 6, 2022",
    cover_type=CoverType.PAPERBACK,
    subject="Programming",
    author="Lily"
)
print(book2)

# Test 4: Test equality
print("--- Test 4: Testing Equality ---")
book3 = Book(111, "Different Title", "Different Date", CoverType.CLOTHCOVER, "Different Subject", "Different Author")
print(f"book1 catalog_num: {book1.catalog_num}")
print(f"book3 catalog_num: {book3.catalog_num}")
print(f"book1 == book3: {book1 == book3}")
print(f"book1 == book2: {book1 == book2}")
print(f"book1 != book2: {book1 != book2}")

print("\n" + "=" * 60)
print("ALL BOOK TESTS COMPLETED SUCCESSFULLY!")
print("=" * 60)



