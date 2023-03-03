# Build an automatic pizza order program.
# Based on a user's order, work out their final bill.

# Small Pizza: $15
# Medium Pizza: $20
# Large Pizza: $25
# Pepperoni for Small Pizza: +$2
# Pepperoni for Medium or Large Pizza: +$3
# Extra cheese for any size pizza: + $1

print("Welcome to Python Pizza. How can i help you ?")

size = input("What size of Pizza you want ? S = Small , M = Medium , L = Large ")
pepperoni = input( " Do you want Pepperoni on your Pizza ? Y = Yes , N = No")
cheese = input( " Do you want Cheese on your Pizza")

bill = 0


if size == "S":
    bill += 15
elif size == "M":
    bill += 20
elif size == "L":
    bill += 25

if pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3

if cheese == "Y":
    bill += 1

print(f"Your final bill is: ${bill}.")
