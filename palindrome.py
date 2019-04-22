#4 Palindrome

word = input("Enter a word: ")
palindrome_check = word[::-1]

if palindrome_check == word:
   print(str(word) + " is a palindrome!")
else:
   print(str(word) + " is NOT a palindrome.")