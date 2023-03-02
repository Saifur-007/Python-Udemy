# Write a program that interprets the Body Mass Index (BMI) based on a user's weight and height.

# It should tell them the interpretation of their BMI based on the BMI value.

# Under 18.5 they are underweight
# Over 18.5 but below 25 they have a normal weight
# Over 25 but below 30 they are slightly overweight
# Over 30 but below 35 they are obese
# Above 35 they are clinically obese.


height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

bmi = weight / (height ** 2)
cov_bim = int(bmi)

if cov_bim > 18.5:
    print("Your BMI is" , cov_bim ,", you are underweight.")
elif cov_bim >= 18.5 and cov_bim < 25:
    print("Your BMI is" , cov_bim ,", you have a normal weight.")
elif cov_bim > 25 and 30 < cov_bim:
    print("Your BMI is " , cov_bim ,", you are slightly overweight.")
elif cov_bim > 30 and cov_bim < 35:
    print("Your BMI is ", cov_bim ,", you are obese.")
else:
    print("Your BMI is ",cov_bim,", your are clinically obese.")