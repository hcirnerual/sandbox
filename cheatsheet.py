# Print to console
print("Hello, World!")

# Variables
x = 5
y = "Hello"

# Data Types
integer = 10
float_number = 3.14
string = "Python"
boolean = True

# Lists
my_list = [1, 2, 3, 4, 5]

# Tuple
my_tuple = (1, "two", 3.0)

# Dictionary
my_dict = {"key": "value", "name": "John"}

# Control Flow
if x > 0:
    print("Positive")
elif x == 0:
    print("Zero")
else:
    print("Negative")

# Loops
for item in my_list:
    print(item)

while x > 0:
    print(x)
    x -= 1

# Functions
def greet(name):
    print("Hello, " + name)

# Calling a Function
greet("Alice")

# File I/O
with open("example.txt", "r") as file:
    content = file.read()

# Exception Handling
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")

# Modules and Libraries
import math
sqrt_result = math.sqrt(16)

# List Comprehension
squared_numbers = [x**2 for x in range(1, 6)]

# Classes and Objects
class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        print("Woof!")

my_dog = Dog("Buddy")
my_dog.bark()
