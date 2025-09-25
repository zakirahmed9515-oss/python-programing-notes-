num = int(input("enter num : "))

if num % 4 == 0 and num % 5 == 0:
    print("the number is divisble by both 4 and 5 ")
    
elif num % 4 == 0:
    print("the number is divisible by 4 ")

elif num % 5 == 0: 
    print("the number is divisible by 5 ")
    
else:
    print("the number is not divisible by both ")