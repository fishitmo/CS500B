def add(x:  int,y: int):
    
    """
    This function adds two numbers

    """
    return x + y

def sub(x,y):
    return x - y


def main():
    
    sum = add(10,20)
    print("sum =", sum)
    
    diff = sub(30, 15)
    print("diff =", diff)

if __name__ == "__main__":
    main()
