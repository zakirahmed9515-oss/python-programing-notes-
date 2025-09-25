#COLLECTION DATA TYPES 
#TUPLE

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
print(fruits[-1])

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

