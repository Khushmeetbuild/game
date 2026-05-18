rent= int(input("Enter the amount of rent you pay: "))
orders= int(input("Enter the total amount of the food ordered: "))
electricity= int(input("Enter the total of electricity spent: "))
charge= int(input("Enter the charge of per unit: "))
members= int(input("Enter the total number of people living in the house: "))

bill= electricity*charge

total= (rent+orders+bill) // members
individual_pay= rent+orders+bill

print ("The total amount each member have to pay: ", total)
print ("The total amount you have to pay is: ", individual_pay)