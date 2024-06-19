#Inheritance and polymorphism
"""_summary
    Inheritance and method overriding
    polymorphism and method resolution order
    Abstract classes and interfaces
    """
    # Inheritance and method overriding
"""_summary
    --description
    Inheritance and method overriding allows a class(child class)to inherit attributes and methods from another class(parent class)
    key concepts
    Base class
    Base
    """
#     #Example 1:Syntax create a class where a dod inherits from animal and overrides with the speak method



class Animal:
    def speak(self):
        return "Mwe Mwe Mwe Mwe"
class Dog(Animal):
    def speak(self):
        return 'Barks'
#Implementation
animal=Animal()
dog=Dog()
print(animal.speak())
print(dog.speak())    
    
# polymorphism
#polymorphism allows objects of different classes to be treated as objects of a common super class.
#Method resolution order (MRO) is order in which python looks for a method in a hierarchy classes.
#  #Example 2:How polymorphism works in python
class Animal:
    def speak(self):
        return "Crock"
class Dog(Animal):
    def speak(self):
        return "Barks" 
class Cat(Animal):
    def speak(self):
        return "Meow"

def make_animal_speak(animal):
    print(animal.speak())
        
    make_animal_speak(Dog())  
    make_animal_speak(Cat()) 


#Exercise1: create a simpleic  application to manage different types of vehicles. Implement derived class to demonstrate inheritance and polymorphism......
"""Requirements needed..
Base class to vehicle
Attributes: make, model and year
Methods: display_info()
Derived classes:
Car: inherits from vehicle 
Attributes: number_of_ doors
Overrides: display_info()
Motorcycle: inherits from vehicle 
Attributes: type_of_bike(cruiser, sport, touring)
Overrides: display_info()"""

# Base class
class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        print(f"Make: {self.make}, Model: {self.model}, Year: {self.year}")

# Derived class - Car
class Car(Vehicle):
    def __init__(self, make, model, year, number_of_doors):
        super().__init__(make, model, year)
        self.number_of_doors = number_of_doors

    def display_info(self):
        super().display_info()
        print(f"Number of doors: {self.number_of_doors}")

# Derived class - Motorcycle
class Motorcycle(Vehicle):
    def __init__(self, make, model, year, type_of_bike):
        super().__init__(make, model, year)
        self.type_of_bike = type_of_bike

    def display_info(self):
        super().display_info()
        print(f"Type of bike: {self.type_of_bike}")

# Create instances
car = Car("Toyota", "Corolla", 2020, 4)
motorcycle = Motorcycle("Harley-Davidson", "Softail", 2022, "Cruiser")

# Display info
car.display_info()
motorcycle.display_info()


#Exercise2. Polymorphism Create a function that accepts a list of vehicle objects 
# and call their display_info() method to print details of each vehicle

def display_vehicle_info(vehicles):
    for vehicle in vehicles:
        vehicle.display_info()

# Create a list of vehicle objects
vehicles = [
    Car("Toyota", "Corolla", 2020, 4),
    Motorcycle("Bajaj", "Softail", 2022, "Cruiser"),
    Car("Honda", "Civic", 2018, 2),
    Motorcycle("Yamaha", "R6", 2020, "Sport")
]

#Reading and writing files in python
"""
    summary
    1. working with text files
    handling CSV files
    JSON and XML files processing
    """
    #1. working with text files ,open,read,write and close
    # note:python provides inbuilt functions to handle text files.
    #key concepts
"""
    summary
    description
    opening file:open() function (r,w,a,r+)
    reading file: read() function
    writing file:write() function
    close file:close() function
    """
    # example 3: write a file and read a file
    # writing to a text file
with open('jeff.txt','w') as file:
    file.write('iam jeff Geoff and i love python.\n')
    file.write('i used python for automation')
    
    # reading from a text file
with open('jeff.txt','r') as file:
    content=file.read()
    print(content)
    
    # handling CSV files
    """
    summary
    CSV  (comma separated values)file widely for data exchange.
    key concepts:
    reading CSV file:using 'CSV.reader()'
    writing CSV files:Using 'CSV.Writer'
    DictReader and DictWriter: the class read and write CSV files as dictionaries
    """
# example 4: reading CSV file
import csv
# writing to a CSV file
with open('jeff.csv','w',newline='') as csv_file:
    writer= csv.writer(csv_file)
    writer.writerow(['name','position','course'])
    writer.writerow(['Jeff Geoff','lecturer','BSE'])
    writer.writerow(['Elsa Nankya ','student','BSE'])
    writer.writerow(['Hillal Sserunjoji','student','BSE'])

# read from CSV file  
with open('jeff.csv','r') as csv_file:
    reader = csv.reader(csv_file)
    for row in reader:
        print (row)  
            #JSON and XML file processing
"""
JSON (javascript object notation) and XML (extensible markup language ) are formats used to structure data.

key concepts
loading JSON data:using json.load() for reading JSON file
dumping JSON DATA:Using json.dump() for writing JSON file
parsing JSON data: using json.loads() for handling JSON strings

"""
# example 6: write and read JSON File
import json
# writing to a JSON file

student_data={
    'name':'shadia',
    'course':'BSE',
    'year':'year 3'
    
    
}
with open('student data.json','w') as json_file:
    json.dump(student_data,json_file)
    # reading the JSON file
with open('student data.json','r') as json_file:
    student_data=json.load(json_file)
    print(student_data)
    


#Exercise2 write and read the xml file

# Call the function to display vehicle info
display_vehicle_info(vehicles)

import xml.etree.ElementTree as ET

# Writing an XML file
def write_xml(file_name):
    # Create the root element
    root = ET.Element("root")

    # Create a child element
    child = ET.SubElement(root, "child")
    child.text = "Hello, Iam Nakanwagi Vanesa"

    # Create a tree and write the XML file
    tree = ET.ElementTree(root)
    tree.write(file_name)

# Reading an XML file
def read_xml(file_name):
    # Parse the XML file
    tree = ET.parse(file_name)

    # Get the root element
    root = tree.getroot()

    # Access the child element's text
    print(root.find("child").text)

# Example usage
file_name = "example.xml"
write_xml(file_name)
read_xml(file_name)




#Exercise3: Using abstraction calculate the area and perimeter of the rectangle
# Define a Rectangle class
# Define a Rectangle class
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    # Define a method to calculate the area
    def area(self):
        return self.width * self.height

    # Define a method to calculate the perimeter
    def perimeter(self):
        return 2 * (self.width + self.height)

# Create a Rectangle object
rect = Rectangle(5, 3)

# Calculate and print the area and perimeter
print("Area:", rect.area())
print("Perimeter:", rect.perimeter())




