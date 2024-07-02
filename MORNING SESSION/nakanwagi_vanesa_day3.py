#Python Best Practices
"""summary
    =Follow PEP 8
    1. Indentation
    2. Maximum Line Length : Limit to 79 characters
    3. Blank Lines
    4. Use meaningful names
    """
    
    
#Example of Good meaningful name


# def calculate_area(radius):
#     pass
# total_price = 10000


# #Example of a lazy student with a bad meaningful name
# def calc(r):
#     pass


# tp = 10000



# Python operators
"""summary
    Name of the operator        Symbol with Example
    Addition                       x + y
    Subtraction                    x + y
    Multiplication                 x * y
    Division                       x / y
    Modulus                        x %% y
    Exponentiation                 x ** y
    Floor division                 x // y
    """
    
    #Example of Comparison operators
"""summary
    Name of the operator        Symbol with Example
    Equal                          x == y
    Not equal                      x != y
    Greater than                   x > y
    Less than                      x < y
    Greater than or equal to       x >= y
    Less than or equal to          x <= y
    
    """   
    
    # Example of Python Logical operators
"""summary
    Name of the operator        Example Symbol
    and                         and
    or                          or
    not                         not
   
    # Example of Membership operators
    Name                        Symbol with Example
    in                          x in y
    not in                      x not in y
    
    # Example of Python Bitwise operators
    # Name                        Symbol with Example
    AND                           &
    OR                            |
    XOR                           ^
    NOT                           ~
    
    # Python cases
    
    1. snake_case
    2. camelCase
    3. PascalCase
    4. UPPERCASE
    5. kebab-case
    """
    
    
#Comprehensions (List, dictionary comprehensions)
"""summary
    Comprehensions provide a concise way to create lists and dictionaries
    what is the symbol for
    lists               [] square brackets used to store multiple items in asingle variable
    dictionaries        {} curly brackets used to store data values in key:value pairs
    
    """
#Exercise1 Create a list of square even numbers in a range of 20
list_of_even_square = [x**2 for x in range (20) if x % 2 == 0]
print(list_of_even_square)

# Example  create a dictonary comprehesion of favourite cars and count the lengths of characters
fovourite_cars = ['BMW', 'Jeep', 'subaru', 'mercedes']
car_lengths = {car: len(car) for car in fovourite_cars }
print(car_lengths)

#Exercise2 create a list of turple where each turple contains a number and its cube for numbers
#between 1 and 10 using a data dictionary comprehesion

numbers_and_cubes = [(x, x**3) for x in range(1, 11)]
print(numbers_and_cubes)