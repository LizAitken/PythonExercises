#Sum of all the numbers divisible by 3 or 5 up to the inputted number
user_input = int(input("What is your number? "))

def sum_odd_by_three_five(num):
    total = 0
    start = 1
    while start <= num:
        if(start % 3 == 0) or (start % 5 == 0):
            total+= start
        start += 1
    return total

print(sum_odd_by_three_five(user_input))