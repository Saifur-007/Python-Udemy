print("//Welcome to the Tip calculator//")

bill = float(input("What is the total bill? £ "))
tip = int(input("How much tip would you want to give ? "))
person = int(input("How many people want to split the bill? "))


each_person_without_tip = (bill / person)
total_tip = ( bill /100 ) * tip
each_person_tip = total_tip / person

each_person_with_tip = each_person_without_tip + each_person_tip
final_amount = "{:.2f}".format(each_person_with_tip)
print (f"Each person need to pay £ {final_amount}")