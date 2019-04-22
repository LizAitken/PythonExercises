#2
#Identifies how many characters from J string are in S string

J = 'aA'
S = 'aAAbbb'

def num_jewels_in_stones(J, S):
    count = 0
    for stone in S:
        if stone in J:
            count += 1
    return count

print(num_jewels_in_stones(J, S))