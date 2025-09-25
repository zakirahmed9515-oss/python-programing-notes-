# Electricity Bill Calculator 

#ask the user for number of electricity units consumed
units = int(input("Enter the number of units consumed: "))

#calculate bill based on given conditions 
if units <= 100:
    bill = units * 5 
elif units <=200:
    bill = (100 * 5) + (units - 100) * 7 
else: 
    bill = (100 * 5) + (100 * 7) + (units - 100) * 10 
    
#print the result 
print("Total electricity Bill: $", bill)