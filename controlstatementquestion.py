# CONTROL STATEMENTS : control statements allow your program to execute different code blocks 
# based on conditions is true or false . 

#1. the IF statemnt : it executes a block of code only if the condition is true
#example:
score = 95
if score > 90: 
    print("the IF statement")
    print("Excellent You've earned a A. \n")
    
#2. the IF-ELSE Statement : it is a classic " THIS OR THAT"
#EXAMPLE :
num = 17
if num %2 == 0: 
    print("the IF_ELSE Statement")
    print(f"{num}is a even number.\n")
    
else:
    print("the IF-ELSE STATEMENT")
    print(f"{num}is an odd number.\n")
    
#3. IF ELIF-ELSE STATEMENT(chained conditionals): it is used when we have more than
#  two possible outcomes 
score = 85 
if score >=90:
    print("grade A")
elif score >80:
    print("grade B")
elif score >55:
    print("grade C")
else:
    print("fail")
    


age = 25 
if age >=18:
    print("")
else :
    print("")