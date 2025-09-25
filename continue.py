#continue condition 

#question
for number in range(1,6):
    if number == 3:
        print("skipping number 3")
        continue
    print("number:",number)
    
#skip negative numbers 
for number in range(-3,6):
    if number <0:
        print("skpping negative numbers")
        continue
    print("number:",number)
    

#skip multiple of 3
for number in range(1,38):
    if number %3==0:
        print("skipping multiple of 3")
        continue
    print("number:",number)
    
