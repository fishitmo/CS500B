
'''
Question 1:
Write a Python program that acts as a code-breaking device, translating letters into their corresponding digits
using this cryptic key:
1 = ADGJM 3 = BEKLO 5 = CFNPQ 7 = HIRST
2 = EFTUV 4 = HSWXY 6 = IYZ 8 = Z
● Input: Prompt the user to enter a single letter, ready for decoding.
● Echo-printing: Repeat the entered letter to confirm its reception.
● Code Translation:
○ For valid letters (A-Z), reveal the corresponding digit according to the code. If the letter is found in multiple
sets, choose the biggest digit. E..g the letter H can be decoded as 4 and 7, then choose 7.
○ If the user enters an invalid character or lowercase letter, indicate that no matching digit exists.
● Constraints: you cannot dictionaries but you can use lists in your program.
Sample program executions:
Prompt: Enter a letter to decipher:
User input: H
Program output: You entered: H
The corresponding digit is 7.
Prompt: Enter a letter to decipher:
User input: Z
Program output: You entered: Z
The corresponding digit is 8.
Prompt: Enter a letter to decipher:
User input: 5
Program output: You entered: 5
No matching digit exists for this character.
'''




def main():
    user_input = input("Enter a letter to decipher:")
    print(f'User input:\t{user_input}')
    
    # check for valid input 
    if len(user_input) != 1 or not user_input.isupper() or not user_input.isalpha():
        print("No matching digit exists for this character.")
        return
    cryptic_key = ["ADGJM", "EFTUV","BEKLO",  "HSWXY" , "CFNPQ", "IYZ" , "HIRST", "Z"]
    cores_digit = []
    for i in range(len(cryptic_key)):
        for j in range(len(cryptic_key[i])):
            if user_input == cryptic_key[i][j]:
               cores_digit.append(i+1)  
    bigest_digit = cores_digit[0]
    for i in cores_digit:
        if i > bigest_digit:
            bigest_digit = i
            
    print(f"The corresponding digit is {bigest_digit}")
            
    
 
    


if __name__ == "__main__":
    main()