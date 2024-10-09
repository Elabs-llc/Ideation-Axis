"""
Challenge 4: List Comprehension
Write a list comprehension that filters out all even numbers from a list and then squares the remaining odd numbers.

Task:

Given a list of numbers, use list comprehension to filter out all even numbers.
For the remaining odd numbers, return a list where each number is squared.

Example 1:
list1 = [1, 2, 3, 4, 5]
The resulting list should be: [1, 9, 25]

Example 2:
list2 = [10, 20, 30, 40, 50]
The resulting list should be: [100, 40, 900]

"""

list1 = [1, 2, 3, 4, 5]
result = [num**2 for num in list1 if num % 2 != 0]

print(result)

list2 = [10, 20, 30, 40, 50]
result2 = [num**2 for num in list2 ] # struggling with the logic

#print(result2)