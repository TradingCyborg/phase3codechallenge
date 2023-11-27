#Python Coding Challenges
This repository contains Python solutions for three coding challenges. The challenges are designed to test and demonstrate different aspects of Python programming.

Challenge 1: Converting 12-hour time to 24-hour time
Description
Converts a 12-hour time to 24-hour time format. The function takes an hour (1 to 12), a minute (0 to 59), and a period ("am" or "pm") as input and returns a four-digit string representing the time in 24-hour format.

#Usage
convert_to_24_hour(8, 30, 'am')  # Output: '0830'
convert_to_24_hour(8, 30, 'pm')  # Output: '2030'

#Challenge 2: Checking for exactly two positive integers

#Description
Checks if exactly two out of three integers are positive numbers. The function takes three integers (a, b, c) as input and returns True if exactly two of them are positive, and False otherwise.

Usage

exactly_two_positive(2, 4, -3)  # Output: True
exactly_two_positive(-4, 6, 8)  # Output: True

#Challenge 3: Finding the highest value of consonant substrings

Description
Finds the highest value of consonant substrings in a given lowercase string. Consonants are defined as any letters except "aeiou," and their values are calculated based on the mapping a = 1, b = 2, ..., z = 26.

Usage

solve("zodiacs")  # Output: 26
solve("strength")  # Output: 57
Feel free to explore and use these functions in your Python projects!

