# Python program to check palindrome

word = input("Enter a word: ")

# Reverse the word
reverse_word = word[::-1]

# Check palindrome
if word == reverse_word:
    print("Palindrome")
else:
    print("Not Palindrome")