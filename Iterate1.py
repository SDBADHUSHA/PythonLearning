# what is iteration in Python ?
# iteration is the process of repeating a set of instructions
# example of iteration ?
for i in range(5):
    print(i)
# what is the difference between iteration and loop ?
# iteration is the process of repeating a set of instructions
# loop is the control structure that is used to repeat a set of instructions

# what are the iteration functions or operators avaiable in python ?
# iteration functions or operators avaiable in python are range() and enumerate()

# The in keyword used in for loop  indicating the iterable from which elements are drawn sequentially
todo_list = ['start project', 'review proposal', 'present proposal']

for todo in todo_list:
    print("Things to do today:", todo)
    #In this context, 
    # in keyword tells Python to iterate over each item in todo_list and assign the current item to the loop variable todo during each pass

# what it is membership operator in python ?
# membership operator in python is used to check if a value is present in a sequence
# example of membership operator ?
print("a" in "apple") # True
print("b" in "apple") # False 

student = {'name': 'Alice', 'age': 24}
print('name' in student)    # Output: True (key check)
print('Alice' in student)   # Output: False (value check)
print('Alice' in student.values()) # Output: True (explicit value check)

# what is the difference between membership operator and identity operator ?
# membership operator is used to check if a value is present in a sequence
# identity operator is used to check if two variables point to the same object
# example of identity operator ?
a = [1,2,3]
b = a
print(a is b) # True
print(a == b) # True    
print(a is not b) # False
print(a != b) # False

#   what is enumerate in python ?
# enumerate in python is used to get the index of an item in a sequence
# example of enumerate ?
for i, letter in enumerate("apple"):
    print(i, letter)

#In this context, 
# enumerate() function is used to get the index of each letter in the string "apple" and assign it to the variable i during each pass

todo_list1 = ['start project', 'review proposal', 'present proposal']

for index1,todo1 in enumerate(todo_list1):
    print("Things to do today:", index1,todo1)
    #In this context, 
    # enumerate() function is used to get the index of each item in the list todo_list1 and assign it to the variable index1 during each pass
# todo1 variable is used to store the current item in the list todo_list1 during each pass
# for loop uses both IN and ENUMERATE operator to iterate over each item in the list todo_list1 and assign the current item to the loop variable todo1 during each pass


# what is the difference between enumerate and range ?
# enumerate is used to get the index of an item in a sequence
# range is used to generate a sequence of numbers
#Example of range ?
value1 = range(5)
print(value1) # range(0, 5)
print(list(value1)) # [0, 1, 2, 3, 4]   

#list() function used to convert range object to list

value1 = range(5)
for i in value1:
    print(i)


# what is iter() function in python ?
# iter() function in python is used to get an iterator object from an iterable
# example of iter() ?
value1 = range(5)
print(iter(value1)) # <range_iterator object at 0x0000021C1C1C1C1C>

# iterator object is used to iterate over an iterable
# example of iterator object ?
value1 = range(5)
for i in iter(value1):
    print(i)

# what is next() function in python ?
# next() function in python is used to get the next item from an iterator
# example of next() ?
# 1. Start with an iterable object (e.g., a list)
my_list = ['A', 'B', 'C', 'D']

# 2. Convert the list into an iterator object
my_iterator = iter(my_list)

# 3. Manually get the next element using next()
print(next(my_iterator)) # Output: A
print(next(my_iterator)) # Output: B
print(next(my_iterator)) # Output: C
print(next(my_iterator)) # Output: D

# 4. Calling next() again after the iterator is exhausted raises an error
# print(next(my_iterator)) # This would raise: StopIteration

value2 = iter(["apple","banana","cherry"])
for i in value2:
    print(i)
   # print(next(i))
    
#reversed(),sorted(),map(),filter():zip()

#reversed() function in python is used to reverse an iterable
#example of reversed() ?
value1 = [1,2,3,4,5]
for i in reversed(value1):
    print(i) # output is 5 4 3 2 1


#sorted() function in python is used to sort an iterable
#example of sorted() ?
value1 = [1,2,3,4,5,1,2,3,4,5]
for i in sorted(value1):
    print(i) # output is 1 1 2 2 3 3 4 4 5 5    

#map() function in python is used to apply a function to all items in an iterable
#example of map() ?
value1 = [1,2,3,4,5]
for i in map(lambda x: x*2, value1):
    print(i) # output is 2 4 6 8 10


#filter() function in python is used to filter an iterable
#example of filter() ?
value1 = [1,2,3,4,5]
for i in filter(lambda x: x%2==0, value1):
    print(i) # output is 2 4

#zip() function in python is used to combine two iterables
#example of zip() ?
value1 = [1,2,3,4,5]
value2 = ["a","b","c","d","e"]
for i in zip(value1,value2):
    print(i) # output is (1, 'a') (2, 'b') (3, 'c') (4, 'd') (5, 'e')

#lambda function in python is used to create anonymous functions
#example of lambda function ?
value1 = [1,2,3,4,5]
value2 = [6,7,8,9,10]
print(lambda x,y: x+y, value1,value2 )

