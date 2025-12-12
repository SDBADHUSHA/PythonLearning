#In Python, virtually everything is an object—lists, dictionaries, strings, integers, and custom class instances are all objects.
#function in python is a block of code that performs a specific task
#A Python function is a self-contained, reusable block of code that performs a specific task. Functions are essential for organizing code,
#  making it modular, easier to read, test, and maintain, and for avoiding code repetition (the DRY principle). 
# Similar to passing lists and dictionaries (which are also objects), Python uses pass-by-object-reference (or call-by-reference for mutable objects).
# When you pass the list, dictionary, interger or custon class object to the function, the function receives a reference to that exact same object in memory

#Python has two main types of functions:
#Built-in functions: Pre-defined functions that are always available for use, such as print(), len(), and sum().
#User-defined functions: Functions that you create yourself to perform specific tasks tailored to your program's needs. 

#Defining and Calling a Function
#   You define a function using the def keyword, followed by a function name, parentheses (), and a colon :. 
# The code block within the function must be indented. The code inside the function body only runs when the function is explicitly called
 
 # Syntax - defining a function 
#def function_name(parameters):
    # function body must be indented to 4 spaces
    #return expression  # Optional: returns a value to the caller

#function_name(arguments) # calling a function


#arguments: The actual values provided to a function when it is called. 
# In Python, virtually everything is an object—lists, dictionaries, strings, integers, and custom class instances are all objects. hence any object can be passed as an argument to a function
# How Passing Objects Works
# Similar to passing lists and dictionaries (which are also objects), Python uses pass-by-object-reference (or call-by-reference for mutable objects).
# When you pass the list, dictionary, interger or custon class object to the function, the function receives a reference to that exact same object in memory
# Python supports various argument types, 
# including positional, keyword, default, and arbitrary arguments (*args and **kwargs).

# Example 1 , Defining a Function and Calling function 
def add(x, y): # function starf with def keyword, add is function name ,(x,y) are parameters, : is colon to indicate the start of the function body
    print(x + y) # function body must be indented to 4 spaces, here the print(x+y) is indented to 4 spaces with in function body

add(5, 3)  # 5 and 3 are positional arguments, add(5, 3) is function call with (5,3) as arguments, function call is outside of the function body


# Example 2 , function returning a single value

def add1(x, y): # function starf with def keyword, add is function name ,(x,y) are parameters, : is colon to indicate the start of the function body
    return x + y # function body must be indented to 4 spaces, here the return (x+y) , return the value 

sum1= add1(5, 3) # add1 is a function call with 5,3 as arguments passed and the return value is stored in variable sum1
print(sum1) # print the value of sum1,output is 8   



# Example 3 function returning mutiple Values
#In Python, returning multiple values from a function is straightforward because Python automatically packs the multiple return values into a single tuple
#The return statement in Python can return multiple values, and these values are packed into a tuple,
#A tuple is a fundamental, built-in data structure in Python used to store an ordered, immutable collection of items.
#Tuples are similar to lists, but with two key distinctions:
#Immutability: Once a tuple is created, you cannot change its elements (add, remove, or modify items).
#Syntax: Tuples are defined using parentheses () rather than square brackets [] used by lists.


def return_multiple_values(): # function starf with def keyword, return_multiple_values is function name, () are parameters, : is colon to indicate the start of the function body
    return 1, 2, 3 # 

result = return_multiple_values()
print(result)  # Output: (1, 2, 3)

# example 4 - decoupling returned mutiple value to different variables 


def return_multiple_values(): # function starf with def keyword, return_multiple_values is function name, () are parameters, : is colon to indicate the start of the function body
    return 1, 2, 3 # function returns multiple values

result1, result2 , result3  = return_multiple_values() # decoupling returned mutiple value to different variables,means storing three returned values 1,2,3 to three variables result1, result2 , result3   
print(result1, result2 , result3)  # Output: (1, 2, 3)

#example 5 - accessing returned mutiple value using index 
def return_multiple_values(): # function start with def keyword, return_multiple_values is function name, () are parameters, : is colon to indicate the start of the function body
    return 1, 2, 3 # return multiple values

result = return_multiple_values() # since  mutiple returned values are stored as tuple we can access them using index , here result variable is treated as tuple 
print(result[0]) #accessing first value using index,output is 1
print(result[1]) #accessing second value using index,output is 2
print(result[2]) #accessing third value using index,output is 3




# Positional arguments KNOWN  and UNKNOWN number of arguments-------

# ---------- Positional Arguments  KNOWN number of arguments --------------------------
# Positional arguments are the most common and straightforward way of passing information to a Python function. 
# The defining characteristic of positional arguments is that their position (order) in the function call dictates which parameter
# in the function definition receives which value.
# How Positional Arguments Work
# When you define a function with parameters, those parameters act as placeholders. 
# When you call the function, Python matches the arguments you provide one by one, based on their sequential order.
# Positional arguments: Values passed to a function based on their position in the argument list.
#Key Characteristics of Positional Arguments
#Order is Mandatory: The position of the argument in the function call must match the position of the parameter in the function definition.
#Simplicity: They are ideal for functions with a small, obvious, and fixed number of arguments where the meaning of the data is clear from its position (e.g., coordinates (x, y)).
#Mixing with Keyword Arguments: Positional arguments can be used alongside [keyword arguments](explain Keyword arguments), but all positional arguments must come before any keyword arguments in the function call.
#example of positional arguments?
def add(x, y):
    print("The value of x is", x)
    print("The value of y is", y)
 
add(5, 3)  # 5 and 3 are positional arguments, x=5 and y=3, hence the arguments are passed in the order of parameters
add(3,5)  # 3 and 5 are positional arguments, x=3 and y=5, hence the arguments are passed in the order of parameters


# ----- Arbitrary Arguments (*args) for UNKNOWN NUMBER OF POSITIONAL ARGUMENTS-----

# In Python, arbitrary arguments (*args) allow a function to accept an indefinite or variable number of positional arguments.
# The syntax involves placing an asterisk (*) before a parameter name in the function definition, by convention named args. 
# This collects all excess positional arguments passed during the function call into a tuple inside the function body
#Key Points about *args
# The Asterisk is Key: The name args is a convention, but the asterisk (*) is mandatory. You could use *numbers or *items, 
# and it would function identically.
# Data Type: Inside the function, args behaves exactly like a tuple, meaning you can iterate over it, access elements by index, 
# and use standard tuple methods.
# Mixing Positional Arguments: You can define standard parameters before *args. These parameters will collect the first few arguments, 
# and *args will collect everything else that follows.

#example 1  for arbitrary arguments for UNKNOWN positional arguments ?

def sum_all(*args):
    print(args) # output is (1, 2, 3, 4) , stores data in python tuple
    return sum(args) # sum(args) is a built-in function that returns the sum of all arguments

result = sum_all(1, 2, 3, 4)  # *args collects all arguments into a tuple, you can use any number of arguments
print(result)  # Output: 10

#example 2  for arbitrary arguments for UNKNOWN positional arguments ?
def sum_all(*numbers): # *numbers is a convention(parameter ), but the asterisk (*) is mandatory. You could use *numbers or *items, there is no need to use as *args , it would function identically.  
    print(numbers) # output is (1, 2, 3, 4) , stores data in python tuple
    return sum(numbers) # sum() is a built-in function that returns the sum of all arguments

result = sum_all(1, 2, 3, 4) # *numbers collects all arguments into a tuple, you can use any number of arguments
result1=sum_all(1,2,3,4,5,6,7)  # *numbers collects all arguments into a tuple, you can use any number of arguments
result2=sum_all(1,2,3,4,5,6,7,8,9,10)  # *numbers collects all arguments into a tuple, you can use any number of arguments
print(result)  # Output: 10
print(result1)  # Output: 28
print(result2)  # Output: 55


# ---------- Keyword Arguments for KNOWN and UNKNOWN number of arguments --------------------------

# Keyword arguments: Values passed to a function by explicitly naming the parameters.
# In Python, keyword arguments are a way of passing values into a function by explicitly naming which parameter each value corresponds to. 
# This method offers several advantages over traditional positional arguments: it improves readability, 
# makes the order of arguments irrelevant, and helps prevent errors when functions have many parameters.
# Advantages of Keyword Arguments
# Using Keyword Arguments (Order doesn't matter), means the arguments passing order in a functional call does not matter 
# Readability: It is immediately clear from the function call what each argument represents.
# Flexibility: You can change the order of arguments without breaking the function call.
# Mixing Positional and Keyword: You can mix both types, but positional arguments must always come first.
#example 1 of keyword arguments for KNOWN number of arguments?

def greet(name, greeting): # name and greeting are parameters
    print("The value of name is", name)
    print("The value of greeting is", greeting)

greet(name="Alice", greeting="Hello")  # the arguments are passed with same order as parameters name="Alice", greeting="Hello"
greet(greeting="Hi", name="python") # the arguments are passed with differnt order greeting="Hi", name="python" but the function still works

# the output is 
# The value of name is Alice, The value of greeting is Hello
# The value of name is python, The value of greeting is Hi

#example 2  of keyword arguments for KNOWN number of arguments?
def greet(name, greeting): # name and greeting are parameters
    return f"The value is {greeting}, {name}!" # f"{greeting}, {name}!" is a formatted string, returns a string 

result = greet(name="Alice", greeting="Hello")  # the arguments are passed with same order as parameters name="Alice", greeting="Hello"
result1 = greet(greeting="Hi", name="python") # the arguments are passed with differnt order greeting="Hi", name="python" but the function still works
print(result)  # Output: The value is Hello, Alice!
print(result1)  # Output: The value is Hi, python!

# ------- keyword arguments for UNKNOWN number of arguments **kwargs (**keyword arguments), ** stands for any number of keyword arguments--------------------------
# Arbitrary keyword arguments: Allow a function to accept a variable number of keyword arguments.
# In Python, **kwargs (short for "keyword arguments") is used in a function definition to collect an arbitrary or variable number of keyword arguments passed to that function.
# It is particularly useful when a function needs to accept optional, named arguments that you don't know the names of in advance.
# Key Points about **kwargs
# The Asterisk is Key: The name kwargs is a convention, but the double asterisk ** is mandatory. You could use any name instead of **kwargs, 
# and it would function identically.example **number1, **info etc ,  it would function identically.  
# Data Type: Inside the function, kwargs behaves exactly like a dictionary, meaning you can iterate over it, access elements by key, 
# and use standard dictionary methods.

# Mixing Positional and Keyword: You can define standard parameters before **kwargs. These parameters will collect the first few arguments, 
# and **kwargs will collect everything else that follows.

#Key Points about **kwargs
#The Double Asterisk is Key: While kwargs is the standard naming convention, the critical part is the double asterisk (**). You could use **attributes or **data and it would function the same way.
#Data Type: Inside the function, the variable specified with ** acts as a standard Python dictionary, allowing you to access keys and values using dictionary methods like .items().
#Order of Parameters: If you mix *args, **kwargs, and standard arguments, the order in the function definition must be: (standard_args, *args, **kwargs)

#example 1 of arbitrary UNKNOWN keyword arguments?


def display_info(**kwargs):
    print(kwargs) # output is {'name': 'Alice', 'age': 30, 'city': 'New York'} , stores data in python dictionary Key : Value pair
    print(kwargs['name']) # output is Alice , use key to access value , because it is a dictionary, kwargs is dictionary name 
    print(kwargs['age']) # output is 30,  use key to access value , because it is a dictionary, kwargs is dictionary name 
    print(kwargs['city']) # output is New York, use key to access value , because it is a dictionary, kwargs is dictionary name 

display_info(name="Alice", age=30, city="New York")  # **kwargs collects all keyword arguments into a dictionary

# example 2 of arbitrary UNKNOWN keyword arguments?

def display_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

display_info(name="Alice", age=30, city="New York")  # **kwargs collects all keyword arguments into a dictionary

# example 3 Mixing Positional and Keyword arguments?
# Order of Parameters: If you mix *args, **kwargs, and standard arguments, the order in the function definition must be: (standard_args(known positional argument), *args, **kwargs)
def display_info(name, *args, **kwargs):
    print("Name:", name) # name is a positional argument, output is : Name: Alice
    print("Positional arguments:", args) # args is a variable-length argument list, output is : Positional arguments: (30, 'New York')
    print("Keyword arguments:", kwargs) # kwargs is a variable-length keyword argument list, output is : Keyword arguments: {'city': 'New York', 'country': 'USA'}

display_info("Alice", 30, "New York", city="New York", country="USA")

# in the above function call python assumes the arguments "Alice " as standard (known positional arguments) and assign to parameter Name parameter
# 30 ,and "New York" is assumed as UNKNOWN positinal arguments , hence assigned  *args parameter 
# and "New York", "USA" has the Keyword such as city and country and hence assumed as Known Keyword arguments are assigned to parameter **kwargs

# -------- Default Arguments ---------

# Default arguments: Parameters with default values that are used if no argument is provided.
#Default arguments in Python functions allow you to specify a default value for a parameter. 
# If the caller of the function omits that argument when making the function call, the function uses the pre-defined default value instead. 
#This makes functions more flexible and allows you to define optional parameters
#example of default arguments?
def multiply(x, y=2): # y=2 is the default value for y
    return x * y

result = multiply(5)  # Uses default value for y
print(result)  # Output: 10

#Mixing Positional and Default Arguments 
#You can mix standard positional arguments with default arguments. All parameters with default values must appear after parameters without default values in the function definition.
# example of mixing Positional and Default Arguments?
def add(x, y=2, z=3): # y=2 is the default value for y, z=3 is the default value for z
    return x + y + z

result = add(5)  # Uses default values for y and z
print(result)  # Output: 10

#Important Pitfall: Mutable Default Arguments 
#A crucial concept to remember is that default arguments are evaluated only once when the function is defined, 
# not every time the function is called. 
#This behavior is fine for immutable types (like strings, integers, or tuples),
#  but it can lead to unexpected behavior if you use mutable types (like lists or dictionaries) as default values. 
#If you modify a mutable default argument inside the function, that change persists across all future calls to the function: 


# Example  1: passing list as parameter to function 

def append_to(element, target=[]): # function uses positinal parameter element and list parameter target[]
    target.append(element)
    return target
newelement ="banana"
List1 = ["apple ", "Mango", "Orange"] # list declaration 
result1 = append_to(newelement, List1) # passing new value and list as argument in function call
print(result1)  # output is ['apple ', 'Mango', 'Orange', 'banana']


#Example passing dictionary as parameter to function 
def append_to(element, dict1={}): # function uses positinal parameter element and dictionary parameter dict1
    dict1["fruit5"] = element # element is added to dictionary dict1
    print(dict1) # output is {'fruit1': 'apple ', 'fruit2': 'Mango', 'fruit3': 'Orange', 'fruit5': 'banana'}    
    return dict1
newfruit1 = "banana" # new value to be added to dictionary
dict1 = {"fruit1": "apple ", "fruit2": "Mango", "fruit3": "Orange"} # dictionary declaration 
result1 = append_to(newfruit1, dict1) # passing new value and dictionary as argument in function call
print(result1) # output is {'fruit1': 'apple ', 'fruit2': 'Mango', 'fruit3': 'Orange', 'fruit5': 'banana'}