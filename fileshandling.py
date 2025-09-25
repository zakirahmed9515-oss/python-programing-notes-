#FILE HANDLING
f = open("data.txt","w")

#WRITING DATA TO A FILE
#write()
f = open("data.txt","w")
print(f.write())
f.close()
    
#writelines()
f = open("data.txt","w")
print(f.writelines())
f.close()

#READING DATA FROM A FILE
#read()
f = open("data.txt","r")
print(f.read())
print(f.read(5))
f.close()

#readline()
f = open("data.txt","r")
print(f.readline())
print(f.readline())
f.close()

#readlines
f = open("data.txt","r")
lines = f.readlines()
print(lines)
f.close()

#RANDOM ACCESS FILE OPERATION
#tell()
f = open("data.txt","r")
print(f.read(5))
print("pointer at:",f.tell())
f.seek(0)
print(f.read(5))
f.close()

