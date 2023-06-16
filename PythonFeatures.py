# Import required modules
from abc import ABC, abstractmethod
from collections import namedtuple, defaultdict
from typing import List, Dict, Union

# Define an interface using an Abstract Base Class
class Animal(ABC):

    @abstractmethod
    def sound(self):
        pass

# Create classes that implement the interface
class Cat(Animal):
    def sound(self):
        return 'Meow!'

class Dog(Animal):
    def sound(self):
        return 'Woof!'

# Basic function
def add_numbers(a: int, b: int) -> int:
    return a + b

# Data types and variables
my_int = 10
my_float = 20.5
my_str = "Hello, world!"
my_bool = True

# Lists and dictionaries
my_list: List[Union[int, str]] = [1, 2, "Three", "Four"]
my_dict: Dict[str, Union[int, str]] = {'one': 1, 'two': 'Two'}

# Tuples and namedtuples
my_tuple = (1, 2, 3)
Point = namedtuple('Point', ['x', 'y'])
p = Point(11, y=22)

# Sets
my_set = {1, 2, 3, 1, 2}

# Collections - defaultdict
my_default_dict = defaultdict(int)
my_default_dict['A'] = 1
my_default_dict['B'] += 1

# Object creation
my_cat = Cat()
my_dog = Dog()

# Print data types and outputs
print(f"Integer: {my_int}, Float: {my_float}, String: {my_str}, Boolean: {my_bool}")
print(f"List: {my_list}")
print(f"Dictionary: {my_dict}")
print(f"Tuple: {my_tuple}")
print(f"Namedtuple: {p.x}, {p.y}")
print(f"Set: {my_set}")
print(f"DefaultDict: {my_default_dict}")
print(f"Cat Sound: {my_cat.sound()}, Dog Sound: {my_dog.sound()}")
print(f"Add Numbers Function: {add_numbers(10, 20)}")
