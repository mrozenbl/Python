import random
import re
from functools import reduce

# File I/O
with open('test.txt', 'w') as f:
    f.write('Hello, World!')

# Exception Handling
try:
    with open('nonexistent_file.txt', 'r') as f:
        content = f.read()
except FileNotFoundError:
    print('File not found.')

# Decorators
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def greet():
    print("Hello, World!")

greet()

# Generators
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

fib = fibonacci()
print(next(fib))  # 0
print(next(fib))  # 1
print(next(fib))  # 1

# Lambda Functions and Reduce
nums = [1, 2, 3, 4, 5]
product = reduce(lambda x, y: x*y, nums)
print(product)  # 120

# List Comprehensions
squares = [n**2 for n in nums]
print(squares)  # [1, 4, 9, 16, 25]

# Regular Expressions
pattern = r"\b[tshw]\w+\b"
text = "This sentence has words that start with vowels."
matches = re.findall(pattern, text)
print(matches)  # ['This', 'sentence', 'and', 'that', 'start', 'with']
