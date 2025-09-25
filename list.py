#COLLECTION DATA TYPES 
#1.LIST

fruits = ['apple', 'banana', 'mango']
print(fruits)

#ADDING AN ELEMENt
fruits = ['apple', 'banana', 'mango']
fruits.append('orange')
print(fruits)

#REMOVEING AN ELEMENT 
fruits = ['apple', 'banana', 'mango']
fruits.remove('banana')
print(fruits)

#CHANGING AN ELEMENT 
fruits = ['apple', 'banana', 'mango']
fruits[1] = 'grapes'
print(fruits)

#ACCESS ELEMENTFROM LIST 
fruits = ['apple', 'banana', 'mango', 'grapes', 'orange']
print(fruits[0])      # first fruit 
print(fruits[-1])     # last fruit 

#SORT THE LIST
numbers = [5,2,9,1,7]
numbers.sort()
print(numbers)


list = ['apple', 'mango', 'banana', 'grapes', 'orange'] 
a = input("enter a fruit :")
if a in list:
    print("a is in the list")
else:
    print("a is not in the list")



