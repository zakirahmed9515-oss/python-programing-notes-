#example for int data type 
val1 = int(input("enter val1: "))
val2 = int(input("enter val2: "))
print("val1 + val2 = ", val1 + val2 ) #addition
print("val1 - val2 = ", val1 - val2 ) #substraction
print("val1 * val2 = ", val1 * val2 ) #multiplication
print("val1 / val2 = ", val1 / val2 ) #division


value1 = float(input("enter value1: "))
value2 = float(input("enter value2: "))


#concatenation of two strings   
first_name = input("Enter First name: ")
last_name = input("Enter last name: ")
print("full name: ", first_name + " " + last_name)

#string slicing 
print("sliced name (first 2 chars):", first_name[:2])

#string length 
print("length of string: ", len(first_name))

#string conversion 
print("string to upper case: ", first_name.upper())
print("string to lower case: ", first_name.lower()) 

#swap case 
print("string swap case: ", last_name.swapcase())

