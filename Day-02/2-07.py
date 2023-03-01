# Write a program that calculates the Body Mass Index (BMI) from a user's weight and height.

height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")


bim = int(weight) / float(height) ** 2
cov_bim = int(bim)

print (cov_bim)