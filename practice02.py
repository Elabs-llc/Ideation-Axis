"""
Challenge 2: Generators
Write a generator function called "fibonacci_generator" that yields the Fibonacci sequence up to a given number n. 
The Fibonacci sequence is a series where each number is the sum of the two preceding ones, typically starting with 0 and 1.

Task:
Implement a generator function fibonacci_generator(n) that yields each number in the Fibonacci sequence until it reaches or exceeds n.
Use a loop to print the Fibonacci numbers generated by the generator.
Example:
If n = 20, the Fibonacci sequence would be: 0, 1, 1, 2, 3, 5, 8, 13.

Guidelines:
Implement the generator using the yield statement.
Use a loop to print the values generated by fibonacci_generator.
"""
import time
def fibonacci_generator(n):
    """
    takes n as limit or the fibonnacci number
    set a,b to 0, 1 since it's always  the first two numbers in the sequence 
    i.e. The Fibonacci sequence is a series where each number is the sum of the two preceding ones, typically starting with 0 and 1.

    A while loop is used to generate the Fibonacci sequence. The loop continues until the value of a becomes greater than or equal to n.

    Inside the loop, the current value of a is yielded using the yield statement. This allows the generator to produce values one at a time.

    After yielding the value, the variables a and b are updated. The new value of a becomes b, and the new value of b becomes the sum of the previous values of a and b.

    """
    a, b = 0, 1
    while a <= n:
        yield a
        a,b = b, a + b
        time.sleep(1)


# Use a loop to print the Fibonacci numbers generated by the generator.
# Example:
# If n = 20, the Fibonacci sequence would be: 0, 1, 1, 2, 3, 5, 8, 13.
fib_num = 20
for n in fibonacci_generator(fib_num):
    print(n)