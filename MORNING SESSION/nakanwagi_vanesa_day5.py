#Defining functions
# function syntax and parameters
#return values
# lambda function
# Functions in python are defined using a def keyword, followed by a function name
# parenthesis(), inside a parenthesis, you put a parameter name and a colon
# example
def multiply(a,b):
    return a*b
result=multiply(5,10)
print(result)
# Example 2: multiply multiple values
def get_coordinates():
    return 10,20
x,y=get_coordinates()
print(x,y)
 #Exercise Define a function  greet with parameter name set to guest  and print a message  Iam a software programmer
# def greet(name="guest"):
#     print("I am a software programmer")
    
# # Example usage:
# greet("Essah")
# greet()  

def greet(*names):
    for name in names:
        print(f"Hello, {name}!")
    print("I am a software programmer")
    # Example usage:
greet("Essah", "Nakanwagi", "Vanesa")
greet()  # No names provided

def greet(name='guest'):
    print(f'I am a software programmer, {name}')

# Example usage:
greet()


# # Example3 print multiple values
def get_name_and_position():
    name = 'Chris'
    position = "I am a developer"
    return name, position

# Call the function and unpack its returned values
name, position = get_name_and_position()
print(name, position)



def get_name_and_age():
    name="Essah"
    age="30"
    return age,name
name, age = get_name_and_age()

print(name,age)
#Notes 
"""_Summary
DocStrings:Optional,describes the function purpose
return:optional.returns a value from the function

"""
#Syntax for defining a function
#def function _name(parameters)
#docstring optional
#function body
#return Values
# lambda function
#Lambda functions ate small anonymous functions defined using lambda keyword
#They are restricted to a single expression
# Syntax for lambda function
#lambda parameter:expression
# Example five Write a lambda function to add two numbers
def add(a,b):
    return a+b 
print (add(45,78))
#Example 6: Use use cases of lambda function for sorting
coordinates=[(1,2),(2,3),(3,1),(5,0)]
coordinates.sort(key=lambda coordinates:coordinates[1])
print(coordinates)
# Map, filter and Reduce
# Example 6: Get the squares of 1 to 5 using map, filter and reduce
number_squares=[1,2,3,4,5]
squares=list(map(lambda x:x**2,number_squares))
print(squares)

# Exercise 6: Define a function to get user info that accepts arbitrary keyword argument and prints each key value pair
def get_user_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# Example usage:# Example usage of get_user_info
user_info = get_user_info(name="Vasel", age=20, city="Kampala")

def vasel_function(a, b, **kwargs):
    print(f"a: {a}, b: {b}")
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# Example usage:
vasel_function(1, 2, city="Stockholm", job="Developer")