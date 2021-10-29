#Program to convert pounds to kilograms

#Prompt user to enter the first value in pounds
print("Enter the first value in pounds you wish to convert into kilograms")
pound1= float(input())

#prompt user to enter the second value in pounds
print("Enter the second value in pounds you wish to convert into kilograms")
pound2 = float(input())

#converting pounds to kgs
kgs1 = pound1/2.20462
kgs2 = pound2/2.20462

#display the results
print("Results")
print(" ")

print("The weight in kgs  of" ,pound1,  " pounds is",round(kgs1,3))
print("The weight in kgs of" ,pound2,  " pounds is",round(kgs2,3))

