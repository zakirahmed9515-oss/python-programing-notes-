#arrays

#create integer array
import array 
numbers = array.array('i',[1,2,3,4,5])
print(numbers)

#create float array
import array 
floats = array.array('f',[1.1,2.2,3.3])
print(floats)


#OPERATIONS ON ARRAYS 
#1.ACCESSING ELEMENTS (INDEXING)
import array
nums = array.array('i',[10,20,30,40])
print(nums[0])
print(nums[2])

#2.SLICING ARRAY
import array 
nums = array.array('i',[10,20,30,40,50])
print(nums[1:4])
print(nums[::-1])

#3.import array 
nums = array.array('i',[1,2,3])
nums.append(4)
print(nums)

#insert at specific index - .insert  (index,value)
nums = array.array('i',[1,2,3])
nums.insert(1,10)
print(nums)

#4.removing elements
nums = array.array('i',[1,10,2,3])
nums.remove(10)
print(nums)

#remove element by index 
nums = array.array('i',[1,2,3,4,5])
del nums[0]
print(nums)


#Questins 
#Q1. 
import array
nums = array.array('i',[10,20,30,40])
print(nums[0])
print(nums[-1])

#Q2. 
import array 
nums = array.array('i',[1,2,3,4,5,6,7])
print(nums[2:5])

#Q3.
import array 
nums = array.array('i',[1,2,3,4,5,6,7])
print(nums[-1])
print(nums[-2])
print(nums[-3])
print(nums[-4])

#Q4.
import array 

nums = array.array('i',[1,2,3,4,5,6,7,8,9,10])
print(nums[::2])

#Q5.
import array 
nums = array.array('i',[5,10,15,20,25,30])
sliced_array = array[0:4]

#Q6.
import array 
nums = ([1,2,3,4,5,6])
print(nums[::-1])

