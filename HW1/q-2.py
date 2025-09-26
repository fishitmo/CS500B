'''
Question 2:
Write a Python program that checks whether a given five-character string is a palindrome? If the string is not a
palindrome, the program should identify the one character that needs to be replaced to make it one. For
example, if the input string is ‘ABBAA’, the program should output ‘AABAA’ as the corrected palindrome. Not
the slicing syntax and reversed() cannot be used in your program.
Here are some samples of program execution:
Enter a five-character string: abbaaa
Error: Invalid input: Please enter a five-character string.
Enter a five-character string: abbaa
abbaa is not a palindrome. Replace character 2 with 'a' to make it become a palindrome.
Revised string with uppercase: AABAA
Enter a five-character string: abcda
abcda is not a palindrome. Replace character 2 with 'd' to make it become a palindrome.
Revised string with uppercase: ADCDA
Enter a five-character string: abcde
abcde is not a palindrome. No single character replacement can make it one.
'''

# Prompt the user to enter a five-character string
str_input = input("Enter a five-character string: ")

def main():
    # check if the string is a five characters
    if len(str_input) != 5:
        print("Error : Invalid input : Please enter a five-character string.")
    else: 
        # check if the string is a palindrome
        if str_input[0] == str_input[4] and str_input[1] == str_input[3]:
            print(f"{str_input} is a palindrome.")
        else:
            # check if the string is a one mismatch (fixable)
            mismatches = []
            
            # chack postion 0 and 4
            if str_input[0] != str_input[4]:
                mismatches.append((0,4))
            
            # check postion 1 and 3
            if str_input[1] != str_input[3]:
                mismatches.append((1,3))
            # analyze mismatch count
            if len(mismatches) == 1:
                print(f"{str_input} is not a palindrome. Replace character {mismatches[0][0]+1} with '{str_input[mismatches[0][1]]}' to make it become a palindrome.")
                # replace char at position 0 with char at position 4 or replace char at position 1 with char at position 3
                revised_str = ""
                # revised_str = str_input[:mismatches[0][0]] + str_input[mismatches[0][1]] + str_input[mismatches[0][0]+1:]
                for i in range(len(str_input)):
                    if i == mismatches[0][0]:
                        revised_str += str_input[mismatches[0][1]]
                    else:
                        revised_str += str_input[i]
                print(f"Revised string with uppercase: {revised_str.upper()}")
            elif len(mismatches) == 2:
                print(f"{str_input} is not a palindrome. No single character replacement can make it one.")
     
    
    
    
    

if __name__ == "__main__":
    main()