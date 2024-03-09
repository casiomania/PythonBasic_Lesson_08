# Lesson 08 / Homework

# Important: do not use loops to implement the main logic.
# You must use recursion.
# The loop can be used only in 4 tasks to find the sum of numbers.
#
# Task 1.
# Write a recursive function for finding the degree of a number.
# Task 2.
# Write a recursive function that displays N stars in a row, the number N is given by the user.
# Illustrate the function with an example. (Test)
# Task 3.
# Write a recursive function that calculates the sum of all numbers in the range from a to b.
# The user enters a and b. Illustrate the operation of the function with an example.
# Optional:
# Task 4.
# Write a recursive function that takes a one-dimensional array of 100 randomly filled integers
# and finds the position from which the sequence of 10 numbers begins, whose sum is minimal.

import random


def num_power(base, exponent):
    if exponent == 0:
        return 1
    elif exponent == 1:
        return base
    else:
        return base * num_power(base, exponent - 1)


def print_stars(number):
    if number == 0:
        return
    print('*', end='')
    print_stars(number - 1)


def sum_range(a, b):
    if a > b:
        return 0
    else:
        return a + sum_range(a + 1, b)


def find_min_sum_position(array, start=0):
    if start + 10 > len(array):
        return start
    else:
        min_sum = sum(array[start:start + 10])
        min_position = start
        for i in range(start + 1, start + 91):
            current_sum = sum(array[i:i + 10])
            if current_sum < min_sum:
                min_sum = current_sum
                min_position = i
        return min_position


print("Number raised to power:", num_power(2, 3))

print("Printing stars:")
print_stars(5)

print("\nSum of numbers in range:", sum_range(1, 5))

arr = [random.randint(1, 100) for _ in range(100)]
print("Position of minimum sum:", find_min_sum_position(arr))