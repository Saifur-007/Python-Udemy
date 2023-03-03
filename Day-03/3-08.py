print("Welcome to the Rollercoaster!")

hight = int(input("What is your hight in cm ? - "))
bill = 0

if hight >= 120:
    print("You can ride the Rollercoaster!")
    age = int(input("What is your age ? "))
    if age < 12:
        bill = 5
        print("Child tickets are £5.")
    elif age <= 18:
        bill = 7
        print("Youth tickets are £7")
    else:
        bill = 12
        print("Adult tickets are £12.")
    wants_phot = input("Do you want a photo taken ? Y = Yes & N = No ")
    if wants_phot == "Y":
        bill += 3
    
    print(f"Your final bill is {bill}")
else:
    print("Sorry,you have to grow taller before you can ride.")