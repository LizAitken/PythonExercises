#Checks the frequency of an item in a list
object_list = ["Banana", "Tuna", "Basket", "Tuna"]
print(object_list)
word = input("What word do you want to check? ")  

def frequency(list, word):
    count = 0
    for item in object_list:
        if item == word:
            count += 1
    return count

print(frequency(object_list, word))