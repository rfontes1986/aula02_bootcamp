# input word 
word = input("Enter a word or sentence: ")

try:
    format = word.replace(" ", "").lower()
    if not format.isalpha():
        raise ValueError("Input contains non-letter characters.")
    
    if format == format[::-1]:
        print(f"{format} is a palindrome.")
    else:
        print(f"{format} is not a palindrome.")
except ValueError:
    print("Invalid entry. Please type a word or sentence.")