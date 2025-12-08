# what is variable in python 
# variable is a container for a value 
# how does variable are managed in memory ?
# variable are stored in memory location and the memory location is stored in the variable name
# example of variable declaration and memory allocation ?
a = 10
print(id(a))
print(id(10)) # both will give same memory location
# what is the difference between id() and memory address ?
# id() returns the memory address of the object in hexadecimal format   
# memory address is the location of the object in memory  
# memory address is the physical location of the object in memory 
# 
# Example , how to access value of a variable  ?
a = 10
print(a)
#    
# how does variable store string ?
a = "Hello"
print(id(a))
print(id("Hello")) # both will give same memory location

# what is index in string and how to find memory location of each character in a string  ?
a = "Hello"
print(id(a[0]))
print(id(a[1]))
print(id(a[2]))
print(id(a[3]))
print(id(a[4]))

# does this mean each charater occupy a memory location in a string ?   
# yes each character occupy a memory location in a string 

# what about list ? how is memory is managed in list ?  
# list is a collection of items and each item occupy a memory location
# example of list declaration and memory allocation ?
a = [1,2,3,4,5]
print(id(a))
print(id(1))
print(id(2))
print(id(3))
print(id(4))
print(id(5))
# does this mean each item occupy a memory location in a list ?
# yes each item occupy a memory location in a list
# what is difference between index and memory location ?
# index is the position of the item in the list and memory location is the physical location of the item in memory
# does index point to memroy location also ?
# yes index point to memory location also
# example of index and memory location in list ?
a = [1,2,3,4,5]
print(id(a[0]))
print(id(a[1]))
print(id(a[2]))
print(id(a[3]))
print(id(a[4]))

# does this mean when i print an index , i am printing value from a memory location ?
# yes when i print an index , i am printing value from a memory location   

# How does the value stored in a variable , i mean in which format ?    
# value stored in a variable is stored in a memory location and the memory location is stored in the variable name

# # print(10), how is memory is manaaged ?    
# when i print(10) , it will create a memory location for 10 and store it in memory and print the value from that memory location    
# but when i assign a = 10 , it will create a memory location for 10 and store it in memory and assign the memory location to variable a    
# so in first case memory location is not stored in variable name but in second case memory location is stored in variable name 
# 
# is any othername for storing value in memory itself ?
# yes , it is called as memory address

#     

