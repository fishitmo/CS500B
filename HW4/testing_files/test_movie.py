"""
Quick Test for Movie Class
Tests the Movie class functionality
"""

from data_layer import Movie, FormatType

print("=" * 60)
print("QUICK TEST: Movie Class")
print("=" * 60)

# Test 1: Create a DVD movie
print("\n--- Test 1: Creating a DVD Movie ---")
movie1 = Movie(
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
print("[OK] Movie created successfully")
print(f"  Catalog Number: {movie1.catalog_num}")
print(f"  Title: {movie1.title}")
print(f"  Director: {movie1.director}")
print(f"  Year: {movie1.year}")
print(f"  Format: {movie1.format_type.value}")

# Test 2: Display movie using __str__
print("\n--- Test 2: Display Movie Information ---")
print(movie1)

# Test 3: Create a Blu-ray movie
print("--- Test 3: Creating a Blu-ray Movie ---")
movie2 = Movie(
    catalog_num=222,
    title="The Matrix",
    published_date="March 31, 1999",
    subject="Science Fiction",
    format_type=FormatType.BLU_RAY,
    director="The Wachowskis",
    actors="Keanu Reeves, Laurence Fishburne, Carrie-Anne Moss",
    year=1999,
    length=136
)
print(movie2)

# Test 4: Create a VCD movie
print("--- Test 4: Creating a VCD Movie ---")
movie3 = Movie(
    catalog_num=223,
    title="Inception",
    published_date="July 16, 2010",
    subject="Science Fiction",
    format_type=FormatType.VCD,
    director="Christopher Nolan",
    actors="Leonardo DiCaprio, Joseph Gordon-Levitt, Ellen Page",
    year=2010,
    length=148
)
print(movie3)

# Test 5: Test equality
print("--- Test 5: Testing Equality ---")
movie4 = Movie(221, "Different Title", "Different Date", "Different Subject", 
               FormatType.BLU_RAY, "Different Director", "Different Actors", 2020, 90)
print(f"movie1 catalog_num: {movie1.catalog_num}")
print(f"movie4 catalog_num: {movie4.catalog_num}")
print(f"movie1 == movie4: {movie1 == movie4}")
print(f"movie1 == movie2: {movie1 == movie2}")
print(f"movie1 != movie2: {movie1 != movie2}")

# Test 6: Access all properties
print("\n--- Test 6: Testing All Properties ---")
print(f"Subject: {movie1.subject}")
print(f"Format Type: {movie1.format_type.value}")
print(f"Director: {movie1.director}")
print(f"Actors: {movie1.actors}")
print(f"Year: {movie1.year}")
print(f"Length: {movie1.length} minutes")

print("\n" + "=" * 60)
print("ALL MOVIE TESTS COMPLETED SUCCESSFULLY!")
print("=" * 60)



