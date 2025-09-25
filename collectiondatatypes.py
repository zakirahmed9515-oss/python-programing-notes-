#COLLECTION DATA TYPES 
#1.LIST

fruits = ['apple', 'banana', 'mango']
print(fruits)

#ADDING AN ELEMENt
fruits.append('orange')
print(fruits)

#REMOVEING AN ELEMENT 
fruits.remove('banana')
print(fruits)

#CHANGING AN ELEMENT 
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


#2.tuple
dimensions = (10,20,30)
print(dimensions)

#create a tuple of 5 colour and print it (example)
colours = ('black', 'white', 'red', 'green', 'blue')
print(colours)

#access elements
colours = ('black', 'white', 'red', 'green', 'blue')
print(colours[0])      #first colour 
print(colours[-1])     #last colour 

#tuple indexing
fruits = ('apple', 'banana', 'mango', 'grapes', 'orange')
print(fruits[0])
print(fruits[2])
print(print[-1])

#tuple slicing
fruits = ('apple', 'banana', 'mango', 'grapes', 'orange')
print(fruits[1:3])

#tuple slice from index1 to 3(does not include index)
fruits = ('apple', 'banana', 'mango', 'grapes', 'orange')
print(fruits[1:3])

#tuple slice from beginning up to index
fruits = ('apple', 'banana', 'mango', 'grapes', 'orange')
print(fruits[:3])

#tuple slice from 2 to end 
fruits = ('apple', 'banana', 'mango', 'grapes', 'orange')
print(fruits[2:])

#tuple step slicing : every second element 
fruits = ('apple', 'banana', 'mango', 'grapes', 'orange')
print(fruits[::2])

#reverse tuple 
fruits = ('apple', 'banana', 'mango', 'grapes', 'orange')
print(fruits[::-1])


# count method
numbers = (1,2,3,2,1,2)
count_2 = numbers.count(2)
print(count_2)


#index method
fruits = ('apple', 'banana', 'mango', 'apple')
index_apple = fruits.index('apple')
print(index_apple)


#3.SET
unique_numbers = {1,2,3,4,2,1}
print(unique_numbers)

#adding elements
unique_numbers = {1,2,3,4,2,1}
unique_numbers.add(5)
print(unique_numbers)

#removing elements
unique_numbers = {1,2,3,4,2,1}
unique_numbers.remove(2)
print(unique_numbers)

#4.DICTIONARY
student={
    'name':'zakir',
    'age':'18',
    'grade':'A',
}

#access value by key 
student={
    'name':'zakir',
    'age':'18',
    'grade':'A',
}
print(student['name'])

#add new key value 
student={
    'name':'zakir',
    'age':'18',
    'grade':'A',
}
student['course']='cs'
print(student)

