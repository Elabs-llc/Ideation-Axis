"""
TASK 01
===================
Challenge 1: Decorators
Create a decorator named 'time_logger' that logs the time taken by a function to execute.
Apply this decorator to a function that calculates the factorial of a number.
The decorator should print out the time taken by the function each time it's called.

Task:
1. Write a time_logger decorator.
2. Write a factorial function that calculates the factorial of a given number.
3. Use the time_logger decorator to wrap the factorial function.
4. Call the factorial function with a few different inputs and observe the logged time.

Let me know when you're done or if you need any help!
"""
import time

# Task 1: Write a time_logger decorator
def time_logger(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        elapsed_time = end_time - start_time

        print(f'{func.__name__} took {elapsed_time} to run')
        return result
    return wrapper

# Task 2: Write a factorial function
@time_logger
def factorial(n):
    if n < 0:
        return "Invalid input. Factorial is not defined for negative numbers."
    return 1 if n==0 or 1 else n* factorial(n - 1)

# Testing number
test_numbers = [2,4,6,8,-9]
for num in test_numbers:
    print(f'{num}!: {factorial(num)}')





