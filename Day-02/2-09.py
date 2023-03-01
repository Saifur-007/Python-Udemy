# Create a program using maths and f-Strings that tells us how many days, weeks, months we have left if we live until 90 years old.


age = int(input("Enter your current age - "))

age_left = 90 - age

week = int(age_left * 52)
month = int(age_left * 12)
day = int(age_left * 365)

print (f"You have {day} days, {week} weeks, and {month} months left.")