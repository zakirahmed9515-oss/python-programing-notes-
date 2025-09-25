num = int(input("enter num : "))
if num % 5 == 0 and num % 3 == 0:
    print(f"num is divisible by both 3 and 5")
elif num % 5 == 0 or num % 3 == 0:
    print (f"num is divisble by either 3 or 5 ")
else:
    print(f"num is not divisible by both 3 and 5 ")