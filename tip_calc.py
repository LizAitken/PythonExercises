#Tip calculator

bill_amount = float(input("Total bill amount? "))
service = input("Level of service? ")

if (service == "good"):
    tip = float(.2 * bill_amount)
    print("Tip amount: $%.2f" % tip)
elif (service == "fair"):
    tip = float(.15 * bill_amount)
    print("Tip amount: $%.2f" % tip)
elif (service == "bad"):
    tip = float(.1 * bill_amount)
    print("Tip amount: $%.2f" % tip)
else:
    print("Please enter good, bad, or fair.")

print("Total amount: $%.2f" % (tip + bill_amount))