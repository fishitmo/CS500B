def main():
    
    user_int = int(input("Enter a decimal value: "))
    hex_str = ""
    if user_int == 0:
        hex_str = '0'
    while user_int > 0:
        remainder = user_int % 16
        if remainder < 10:
            hex_digit = str(remainder)
            
        else:
             hex_digit = chr(remainder + 55)
            
        hex_str = hex_digit + hex_str
        user_int //= 16
          
    print(f"The hex value is {hex_str}")



if __name__ == "__main__":
    main()
    
