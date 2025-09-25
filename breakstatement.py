#find first even number 

numbers = [1, 3,  7, 10, 5, 8]

for num in numbers:
    if num % 2 == 0:
       print("first even number found:",num)
       break
    print(num)
else:
    print("no even number found")
    
#user input s


while True:
    user_input = input("enter 'exit' to stop: ")
    if user_input == 'exit':
        print("exiting loop...")
        break 
    print("you entered:", user_input)
 
 