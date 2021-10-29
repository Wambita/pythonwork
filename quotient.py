#Program to convert pounds to kilograms

#Prompt user to enter the first value in pounds
print("Enter the first value ")
pound1= float(input())

#prompt user to enter the second value in pounds
print("Enter the second value ")
pound2 = float(input())

#Quotient
quo1= pound1//pound2
quo2=pound2//pound1
 
 #display results
print ("quotient results")
print("The quotient when " ,pound1, "is divided by " , pound2, "is ")
print(quo1)
print("The quotient when " ,pound2, "is divided by " , pound1, "is ")
print(quo2)