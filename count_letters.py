#1
#Identifies how many of the inputted letter in the inputted string

string = input("Enter a sentence: ")
letter = input("What letter would you like to identify? ")

def single_letter_count(string, letter):
    new_string = string.lower()
    new_letter = letter.lower()
    counter = 0
    for char in new_string:
        if (char == new_letter):
            counter += 1
    return counter

print(single_letter_count(string, letter))