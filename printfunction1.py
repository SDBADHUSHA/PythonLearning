# print function in python is used to print the output  

#print function syntax 

help(print)
# def print(*values: object, sep: Optional[str]=..., end: Optional[str]=..., file: Optional[SupportsWrite[str]]=..., flush: bool=...) -> None

# print function arguments
# objects - The objects to be printed to the stream. An arbitrary number of objects can be provided, and they are converted to string representations before being output.	(None)
#sep - A string inserted between multiple objects when they are printed. This argument must be provided as a keyword argument.	A single space (' ')
#end - A string appended after the last object is printed. This argument must be provided as a keyword argument and is typically used to prevent a new line from being added automatically.	A newline character ('\\n')
#file - The file-like object (with a write(string) method) where the output will be sent. By default, it sends the output to the standard system output (usually the console/terminal).	sys.stdout
#flush - A Boolean value. If True, the output buffer is forcibly flushed, meaning the output appears immediately even if the stream is buffered.

# example of print function arguments
import sys
print("Hello", "World",sep="-",end="\n",flush=True,file=sys.stdout) # output is Hello-World

# print () functions can take any number of python objects , example datatypes , function , list, string etc...
# print in the above statement there are two string objects used that is Hello , world 
# sep="-" is used to insert a hyphen between the two string objects , by default sep=" " is used, ie empty space 
# end="\n" is used to insert a new line after the last object
# flush=True is used to flush the output buffer
# file=sys.stdout is used to send the output to the standard system output (usually the console/terminal)   



# print function attributes
print(dir(print))

#['__call__', '__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__',
# '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', 
# '__lt__', '__module__', '__name__', '__ne__', '__new__', '__qualname__', '__reduce__', '__reduce_ex__', 
# '__repr__', '__self__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__text_signature__']

# print function attributes description
# '__call__': allows the object to be called as a function
# '__class__': returns the class of the object
# '__delattr__': deletes an attribute from the object
# '__dir__': returns a list of attributes of the object
# '__doc__': returns the documentation of the object
# '__eq__': checks if two objects are equal
# '__format__': formats the object as a string
# '__ge__': checks if one object is greater than or equal to another
# '__getattribute__': gets an attribute from the object
# '__getstate__': gets the state of the object
# '__gt__': checks if one object is greater than another
# '__hash__': returns the hash value of the object
# '__init__': initializes the object
# '__init_subclass__': initializes a subclass
# '__le__': checks if one object is less than or equal to another
# '__lt__': checks if one object is less than another
# '__module__': returns the module of the object
# '__name__': returns the name of the object
# '__ne__': checks if two objects are not equal
# '__new__': creates a new object
# '__qualname__': returns the qualified name of the object
# '__reduce__': reduces the object to a picklable format
# '__reduce_ex__': reduces the object to a picklable format with an extension protocol
# '__repr__': returns the string representation of the object
# '__self__': returns the self reference of the object
# '__setattr__': sets an attribute of the object
# '__sizeof__': returns the size of the object
# '__str__': returns the string representation of the object
# '__subclasshook__': checks if a class is a subclass of another class
# '__text_signature__': returns the text signature of the object



# example of print function with string object as argument ?
print("Hello World")

# print function with multiple string objects as arguments ?
print("Hello", "World")

# print function with multiple string objects as arguments and separator with -(hyphen) ?
print("Hello", "World", sep="-")

# print function with multiple string objects as arguments and end with new line  ?
print("Hello", "World", end="\n")

# print function with multiple string objects as arguments and end with new line  ?
print("Hello \n World")

# print function with multiple string objects as arguments   
print("Hello", "World", "Python", "Programming", "Language", "is", "Fun", "to", "Learn", "and", "Use")

# print function with multiple string objects as arguments and seperator with new line 
print("Hello", "World", "Python", "Programming", "Language", "is", "Fun", "to", "Learn", "and", "Use", sep="\n")

# print function with multiple string objects as arguments and seperator with new line and end with new line 
print("Hello", "World", "Python", "Programming", "Language", "is", "Fun", "to", "Learn", "and", "Use", sep="\n", end="\n")

# print function with multiple string objects as arguments and seperator with new line 
print("Hello", "\n", "World","\n", "Python","\n", "Programming","\n", "Language")

 # print function with integer object as argument 
print(10+20)

# print function with string object as argument 
print("Hello" + "World")
# print function with list object as argument 
list1=[1,2,3,4,5]
print(list1)

#print with lambda function as argument 
print((lambda x: x + x)(10))


# Print() escape sequences 

#The print() function in Python uses standard string escape sequences to represent special, non-printable characters. These sequences start with a backslash (\).
#Here are the most commonly used escape characters:
#Escape Sequence	Name	Description	Example Output
#\n	Newline	Moves the cursor to the beginning of the next line.	
#\t	Tab	Inserts a horizontal tab space.	
#\\	Backslash	Inserts a literal backslash character.	
#\'	Single Quote	Inserts a literal single quote character within single quotes.	
#\"	Double Quote	Inserts a literal double quote character within double quotes.	
#\r	Carriage Return	Returns the cursor to the beginning of the current line, overwriting previous text.	
#\b	Backspace	Moves the cursor back one character (may delete the preceding character depending on the terminal).

# Example of escape sequences 
print("Hello\nWorld") #output is Hello and World on new line
print("Hello\tWorld") #output is Hello and World with tab space Hello   World
print("Hello\\World") #output is Hello and World with backslash Hello\World
print("Hello\'World") #output is Hello and World with single quote Hello'World
print("Hello\"World") #output is Hello and World with double quote Hello"World
print("Hello\rWorld") #output is Hello and World with carriage return World,due \r cursor returns to the beginning of the line and overwrites previous text, hence it will only display world
print("Hello\bWorld") #output is Hello and World with backspace Hell World, due to back space o will be deleted from hello

