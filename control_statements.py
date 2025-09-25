#1. the IF statemnt 
score = 95
if score > 90: 
    print("the IF statement")
    print("Excellent You've earned a A. \n")
    
#2. the IF-ELSE Statement\
num = 17
if num %2 == 0: 
    print("the IF_ELSE Statement")
    print(f"{num}is a even number.\n")
    
else:
    print("the IF-ELSE STATEMENT")
    print(f"{num}is an odd number.\n")
    
#3. IF ELIF-ELSE STATEMENT(chained conditionalds)
score = 85 
if score >=90:
    print("grade A")
elif score >80:
    print("grade B")
elif score >55:
    print("grade C")
else:
    print("fail")
    
score = 85 
if score > 90:
    grade = "A"
elif score > 80:  #else-if 
      grade = "B"
elif score > 70:
      grade = "C"
elif score > 60:
      grade = "C"
else: 
    grade = "F"
print("The IF-ELSE-ELSE Statement")
print(f"A score of {score} gets a grade of {grade}.")
print(f"A score of "+str(score)+"gets a grade of "+grade+ "./n")

# # 4. Nested IF-ELSE Statement 
num =78 
if num > 0:
    if num > 25: 
        if num > 50:
            if num > 75:
                print("The Nested IF-ELSE Statement")
                print(f"{num} is greather than 75.\n")
else: 
    print("The Nested IF-ELSE Statements")
    print(f"{num} is not greater than 75.\n") 
  