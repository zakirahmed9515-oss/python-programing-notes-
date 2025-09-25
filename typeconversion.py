#1.LIST-TUPLE:
my_list = [1,2,3,4]
my_tuple = tuple(my_list)
print(my_tuple)
print(type(my_tuple))

#2.TUPLE-LIST
my_tuple = (5,6,7)
my_list = list(my_tuple)
print(my_list)
print(type(my_list))

#3.LIST-SET (REMOVE DUPLICATE)
my_list = [1,2,2,3,3,4]
my_set = set(my_list)
print(my_set)
print(type(my_set))

#4.SET-LIST
my_set = {10,20,30}
my_list = list(my_set)
print(my_list)

#5.DICTIONARY-LIST OF KEYS 
student = {'name':'john', 'age':'20','grade':'A'}
keys_list = list(student.keys())
print(keys_list)

#6. DICTIONARY-LIST OF VALUES
student = {'name':'john', 'age':'20','grade':'A'}
value_list = list(student.values())
print(value_list)

#7.DICTIONARY-LIST OF ITEMS (TUPLE OF KEY-VALUE PAIRS)
student = {'name':'john', 'age':'20','grade':'A'}
item_list = list(student.items())
print(item_list)

