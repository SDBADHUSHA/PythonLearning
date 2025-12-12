#A lambda function in Python is a small, anonymous function (a function without a name) defined using the lambda keyword. 
#It can take any number of arguments but is restricted to a single expression, the result of which is automatically returned
# Syntax : lambda arguments: expression
#example of lambda function ?

# Example 1: passing variable to lambda function call
x = 10
output1 = lambda x: x * x # x is mutiplied (x*x) and the result is returned (stored) in x 
print(output1) # Output is 0x0000022F94CA8F40 , Object location in memory, means the outpu1 now refers to the lambda function
print(output1(x)) # Output: 100, Lambda function execution is done by calling the function output1(x)

# Example 2:

#example 3: passing value to lambda function call 
square = lambda x: x * x  # x: is the argument and x * x is the expression, the variable square act as the function name 
print(square) # output is <function <lambda> at 0x000001CA5BB31760>, Object location in memory
print(square(5))  # Output: 25 , Lambda function execution is done by calling the function square(5)

# Example 3: calling functions itself and passing value to lambda function call, where (10) call the lambda function and pass 10 as value 

print((lambda x: x + x)(10)) # Output: 20 , Lambda function execution is done by calling the function (lambda x: x + x)(10)

# Example 4: lambda function with multiple arguments
x=10
y=20
addition1=lambda x , y:  x+y # lambda function with multiple arguments, takes x,y as parameters  and returns the sum of x and y (expression)
print(addition1(x,y)) # Output: 30, Lambda function execution is done by calling the function addition1(x,y)
# addition1(x,y) passes two arguments to the lambda function , hence lambda functions takes any mumber of arguments but returns only one expression


#lambda function with multiple expressions ?
mul = lambda x, y: (x + y)*x
print(mul(5, 3))  # Output: 40  , Lambda function execution is done by calling the function mul(5, 3)   

#map(): Applying a function to every item in an iterable
numbers = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x * 2, numbers))
# doubled is [2, 4, 6, 8, 10], map function execution is done by calling the function map(lambda x: x * 2, numbers)

#lambda function as an argument to another function ?
def apply_function(func, x, y):
    return func(x, y)

result = apply_function(lambda x, y: x + y, 5, 3)
print(result)  # Output: 8, Lambda function execution is done by calling the function apply_function(lambda x, y: x + y, 5, 3)

