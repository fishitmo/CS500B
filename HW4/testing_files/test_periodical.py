"""
Quick Test for Article and Periodical Classes
Tests the composition relationship and basic functionality
"""

from data_layer import Article, Periodical, PeriodicalType




print("=" * 60)
print("QUICK TEST: Article and Periodical Classes")
print("=" * 60)

# Test 1: Create a Periodical
print("\n--- Test 1: Creating a Periodical ---")
periodical1 = Periodical(
    catalog_num=331,
    title="Wall Street Journal 167(15)",
    published_date="Oct 23, 2023",
    periodical_type=PeriodicalType.JOURNAL
)
print("[OK] Periodical created successfully")
print(f"  Catalog Number: {periodical1.catalog_num}")
print(f"  Title: {periodical1.title}")
print(f"  Type: {periodical1.periodical_type.value}")

# Test 2: Add articles using composition
print("\n--- Test 2: Adding Articles (Composition) ---")
article1 = periodical1.add_article(
        article_title= "Market Trends in 2023",
    author="John Doe",
    issue_date ="Oct 23, 2023"
)
print("[OK] Article 1 added")
print(f"  Article title: {article1.title}")
print(f"  Periodical title (auto-set): {article1.periodical_title}")

article2 = periodical1.add_article(
    article_title="Tech Industry Analysis",
    author="Jane Smith",
    issue_date ="Oct 23, 2023"
)
print("[OK] Article 2 added")
print(f"  Article title: {article2.title}")

# Test 3: Display full periodical with articles
print("\n--- Test 3: Display Periodical with Articles ---")
print(periodical1)

# Test 4: Create another periodical (Magazine)
print("\n--- Test 4: Creating a Magazine Periodical ---")
periodical2 = Periodical(
    catalog_num=332,
    title="Time 168(18)",
    published_date="Oct 26, 2023",
    periodical_type=PeriodicalType.MAGAZINE
)
periodical2.add_article(
    article_title="Elon Musk's Struggle for the Future of AI",
    author="Walter Isaacson",
    issue_date="Oct 26, 2023"
)
print(periodical2)

# Test 5: Test equality based on catalog number
print("\n--- Test 5: Testing Equality (__eq__ method) ---")
periodical3 = Periodical(331, "Different Title", "Different Date", PeriodicalType.NEWSPAPER)
print(f"periodical1 catalog_num: {periodical1.catalog_num}")
print(f"periodical3 catalog_num: {periodical3.catalog_num}")
print(f"periodical1 == periodical3: {periodical1 == periodical3}")
print(f"periodical1 == periodical2: {periodical1 == periodical2}")
print(f"periodical1 != periodical2: {periodical1 != periodical2}")

# Test 6: Create standalone Article
print("\n--- Test 6: Creating Standalone Article ---")
standalone_article = Article(
    title="Standalone Article Title",
    author="Bob Wilson",
    issue_date="Nov 1, 2023",
    periodical_title="Some Magazine"
)
print(standalone_article)

print("\n" + "=" * 60)
print("ALL TESTS COMPLETED SUCCESSFULLY! [OK]")
print("=" * 60)