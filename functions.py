#FUNCTIONS
def greet():
    print("welcome to python funcions!")
greet()
    
#PASSING PARAMETER AND ARGMENTS 
def greet_user(name):
    print("hello,",name)
greet_user("hero")
    
#FUNCTION ARGUMENTS TYPES 
#a)positional arguments 
def add(a,b):
    print("sum is:",a+b)
add(5,10)

#KEYWORK ARGUMENT 
def introduce(name,age):
    print(f"my name is {name} and i am {age} years old")
introduce(age=29,name="hero")

#b)default arguments 
def greet(name="guest"):
    print("hello,",name)
greet()
greet("zakir")


#Q1.
num1 = int(input("enter num"))
num2 = int(input("enter num"))
def mul(num1,num2):
    return num1*num2
print(mul(num1,num2))

#Q2.
a = int(input("enter a value:"))
def check_even_odd(number):
    if number % 2 == 0:
        return "even"
    else:
        return "odd"
print(check_even_odd(a))
    
#Q3.
def factorial(n):
    if n == 0 or n == 1:
        return 1 
    else:
        return n  * factorial(n-1)
    print()
    
#Q4.
n1=int(input("enter first number"))
n2=int(input("enter second number"))
n3=int(input("enter third number"))
def largest_of_three(a,b,c):
    if a >= b and a>=c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c
print(largest_of_three(n1,n2,n3))
        
#Q5.
str = input("enter string")
def reverse_string(s):
    return s[::-1]
print(reverse_string(str))

#Q6.
word = input("enter your name")
def count_vowels(word):
    vowels = "aeiouAEIOU"
    count = 0
    for char in word:
        if char in vowels:
         count += 1
    return count
print(count_vowels(word))

