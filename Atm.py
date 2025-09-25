amt1 = int(input("enter amount"))

amt2 = int(input("enter amount"))

if amt1>amt2:
     
     if amt2%100==0:
         print("transaction succesful")
         print("balance amount")  
         
     else:
         print("invalid amount")

else:
    print("insufficient amount")

