#datatypes : A  data type is an attribute that specifies the kind of data
# a particular value can hold within a computer system or programming 
# language.

# types of datatypes: 
# ("Integers") : a number without decimal points.
# syntax: datatype variablename = value;
#example
a = int(input("enter a value "))
b = int(input("enter b value "))
print(a+b)
print(type(a))
print(type(b))

#float : a number with decimal points 
#syntax datatype variable = value 
#example : 
a = float(input("enter a value "))
b = float(input("enter b value "))
print(a+b)
print(type(a)) 
print(type(b)) 

#complex : anumbe which represents the complex values 
#syntax datatype variable = value 
#example : 
a = 20+2j
print(a)
print(type("a"))

#string : it is nothing but collection of characters which is used to storinf of data types 
#syntax : string variable = "characters"
#example :
a = str(input("hello"))
b = str(input("guys"))        
print(a+b)
print(type("a+b"))
#boolean : for checking the conditions 
#syntax : 
bool(e) = True 
bool(f) = False 
