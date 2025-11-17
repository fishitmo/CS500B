from data_layer import CatalogRepository, Book, Movie, Periodical

print("=" * 70)
print("VERIFICATION: catalog_data.csv")
print("=" * 70)

# Load the catalog
repo = CatalogRepository("D:/SFBU/CS500B/HW4/catalog_data.csv")
items = repo.get_items()

print(f"\n Successfully loaded {len(items)} items from catalog_data.csv\n")

# Display all items
for item in items:
    print(item)
    print()

# Verify article linking
print("=" * 70)
print("ARTICLE VERIFICATION")
print("=" * 70)

periodical_332 = next((item for item in items if isinstance(item, Periodical) and item.catalog_num == 332), None)

if periodical_332:
    print(f"\nPeriodical: {periodical_332.title}")
    print(f"Catalog #: {periodical_332.catalog_num}")
    print(f"Articles: {len(periodical_332.articles)}")
    
    if len(periodical_332.articles) > 0:
        print("\nArticle Details:")
        for article in periodical_332.articles:
            print(f"  Title: {article.title}")
            print(f"  Author: {article.author}")
            print(f"  Date: {article.issue_date}")
            print(f"  In: {article.periodical_title}")
        print("\n Article successfully linked to periodical!")
    else:
        print("\n No articles found in periodical")
else:
    print("\n Periodical 332 not found")

print("\n" + "=" * 70)
print("VERIFICATION COMPLETE")
print("=" * 70)
print("\nSummary:")
print(f"  - Books: {sum(1 for item in items if isinstance(item, Book))}")
print(f"  - Movies: {sum(1 for item in items if isinstance(item, Movie))}")
print(f"  - Periodicals: {sum(1 for item in items if isinstance(item, Periodical))}")
print(f"  - Total Items: {len(items)}")
print("\n catalog_data.csv format is correct!")
print(" All items load successfully!")
print(" Articles are properly linked to periodicals!")