from bookstore import Book

def main():
    
    b1 = Book("How to code C++", "Petter", 36.99)
    b2 = Book("Python Programming", "Sandy", 46.99)

    print("b1 =", str(b1))
    print()
    b2.author = "Lily"
    print("After b2.author = 'Lily'")
    print("b2 =", str(b2))
    b2.price = 56.7
    print("After b2.price = 56.7")
    print("b2 =", str(b2))
    b2.title = "Advanced C"
    print("After b2.title = 'Advanced C'")
    print("b2 =", str(b2))
if __name__ == "__main__":
    main()