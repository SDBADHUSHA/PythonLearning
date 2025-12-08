#string are sequence of characters
#  string are immutable , Immutable means we cannot change the value of the string
# string are ordered
#string are case sensitive
# string are iterable
# string are indexed
print (dir(str)) # prints all the methods that can be used with string
#['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', 
#__getnewargs__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__',
 #'__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__',
#'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']

# Explanation of string Functions -----

# capitalize() - converts the first character to uppercase
# casefold() - converts the string to lowercase
# center() - returns a centered string
# count() - returns the number of times a value occurs in a string
# encode() - returns an encoded version of the string
# endswith() - returns true if the string ends with the specified value
# expandtabs() - sets the tab size of the string
# find() - searches the string for a specified value and returns the position of where it was found
# format() - formats specified values in a string
# format_map() - formats specified values in a string
# index() - searches the string for a specified value and returns the position of where it was found
# isalnum() - returns true if all characters are alphanumeric
# isalpha() - returns true if all characters are alphabets
# isascii() - returns true if all characters are ascii
# isdecimal() - returns true if all characters are decimals
# isdigit() - returns true if all characters are digits
# isidentifier() - returns true if the string is a valid identifier
# islower() - returns true if all characters are lowercase
# isnumeric() - returns true if all characters are numeric
# isprintable() - returns true if all characters are printable
# isspace() - returns true if all characters are spaces
# istitle() - returns true if the string follows the rules of a title
# isupper() - returns true if all characters are uppercase
# join() - joins the elements of an iterable to the end of the string
# ljust() - left justify the string
# lower() - converts the string to lowercase
# lstrip() - left strip the string
# maketrans() - returns a translation table
# partition() - splits the string at the first occurrence of the specified value
# removeprefix() - removes the prefix from the string
# removesuffix() - removes the suffix from the string
# replace() - replaces a specified phrase with another specified phrase
# rfind() - searches the string for a specified value and returns the last position of where it was found
# rindex() - searches the string for a specified value and returns the last position of where it was found
# rjust() - right justify the string
# rpartition() - splits the string at the last occurrence of the specified value
# rsplit() - splits the string at the specified separator, and returns a list
# rstrip() - right strip the string
# split() - splits the string at the specified separator, and returns a list
# splitlines() - splits the string at line boundaries
# startswith() - returns true if the string starts with the specified value
# strip() - removes leading and trailing characters
# swapcase() - swaps cases, lower to upper and upper to lower
# title() - converts the first character of each word to uppercase
# translate() - returns a translation table
# upper() - converts the string to uppercase
# zfill() - fills the string with zeros

# Example of string functions
str = "Hello World"
print(str.capitalize()) #output is Hello World
print(str.casefold()) #output is hello world
print(str.center(20)) #output is Hello World
print(str.count("l")) #output is 3
print(str.encode()) #output is b'Hello World'
print(str.endswith("d")) #output is True
print(str.expandtabs(2)) #output is Hello World
print(str.find("W")) #output is 6
print(str.format("{}")) #output is Hello World
print(str.format_map({"name":"John"})) #output is Hello World
print(str.index("W")) #output is 6
print(str.isalnum()) #output is True
print(str.isalpha())     #output is True
print(str.isascii()) #output is True
print(str.isdecimal()) #output is False
print(str.isdigit()) #output is False
print(str.isidentifier()) #output is True
print(str.islower()) #output is False
print(str.isnumeric()) #output is False
print(str.isprintable()) #output is True
print(str.isspace()) #output is False
print(str.istitle()) #output is False
print(str.isupper()) #output is False
print(str.join("abc")) #output is abcHello Worldabc
print(str.ljust(20)) #output is Hello World
print(str.lower()) #output is hello world
print(str.lstrip()) #output is Hello World
print(str.maketrans("H", "J")) #output is {65: 66}
print(str.partition("W")) #output is ('Hello ', 'W', 'orld')
print(str.removeprefix("Hello")) #output is World
print(str.removesuffix("World")) #output is Hello
print(str.replace("World", "Python")) #output is Hello Python
print(str.rfind("W")) #output is 6
print(str.rindex("W")) #output is 6
print(str.rjust(20)) #output is Hello World
print(str.rpartition("W")) #output is ('Hello ', 'W', 'orld')
print(str.rsplit(" ")) #output is ['Hello', 'World']
print(str.rstrip()) #output is Hello World
print(str.split(" ")) #output is ['Hello', 'World']
print(str.splitlines()) #output is ['Hello', 'World']
print(str.startswith("Hello")) #output is True
print(str.strip()) #output is Hello World
print(str.swapcase()) #output is hELLO wORLD
print(str.title()) #output is Hello World
print(str.translate(str.maketrans("H", "J"))) #output is Jello World
print(str.upper()) #output is HELLO WORLD
print(str.zfill(20)) #output is 0000000000000Hello World

# Exaple 2: 
# The same functions can be used with string methods, you does not need to store a string in to variable to use string methods , you can able to use all string methods using string value 
# python treats string value as a string class object
print("Hello World".capitalize()) #output is Hello World
print("Hello World".casefold()) #output is hello world
print("Hello World".center(20)) #output is Hello World
print("Hello World".count("l")) #output is 3
print("Hello World".encode()) #output is b'Hello World'
print("Hello World".endswith("d")) #output is True
print("Hello World".expandtabs(2)) #output is Hello World
print("Hello World".find("W")) #output is 6
print("Hello World".format("{}")) #output is Hello World
print("Hello World".format_map({"name":"John"})) #output is Hello World
print("Hello World".index("W")) #output is 6
print("Hello World".isalnum()) #output is True
print("Hello World".isalpha()) #output is True
print("Hello World".isascii()) #output is True
print("Hello World".isdecimal()) #output is False
print("Hello World".isdigit()) #output is False
print("Hello World".isidentifier()) #output is True
print("Hello World".islower()) #output is False
print("Hello World".isnumeric()) #output is False
print("Hello World".isprintable()) #output is True
print("Hello World".isspace()) #output is False
print("Hello World".istitle()) #output is False
print("Hello World".isupper()) #output is False
print("Hello World".join("abc")) #output is abcHello Worldabc
print("Hello World".ljust(20)) #output is Hello World
print("Hello World".lower()) #output is hello world
print("Hello World".lstrip()) #output is Hello World
print("Hello World".maketrans("H", "J")) #output is {65: 66}
print("Hello World".partition("W")) #output is ('Hello ', 'W', 'orld')
print("Hello World".removeprefix("Hello")) #output is World
print("Hello World".removesuffix("World")) #output is Hello
print("Hello World".replace("World", "Python")) #output is Hello Python
print("Hello World".rfind("W")) #output is 6
print("Hello World".rindex("W")) #output is 6
print("Hello World".rjust(20)) #output is Hello World
print("Hello World".rpartition("W")) #output is ('Hello ', 'W', 'orld')
print("Hello World".rsplit(" ")) #output is ['Hello', 'World']
print("Hello World".rstrip()) #output is Hello World
print("Hello World".split(" ")) #output is ['Hello', 'World']
print("Hello World".splitlines()) #output is ['Hello', 'World']
print("Hello World".startswith("Hello")) #output is True
print("Hello World".strip()) #output is Hello World
print("Hello World".swapcase()) #output is hELLO wORLD
print("Hello World".title()) #output is Hello World
print("Hello World".translate(str.maketrans("H", "J"))) #output is Jello World
print("Hello World".upper()) #output is HELLO WORLD
print("Hello World".zfill(20)) #output is 0000000000000Hello World
