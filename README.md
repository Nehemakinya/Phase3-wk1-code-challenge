## Converting 12-hour time to 24-hour time, Two numbers are positive and Consonant value

This repository contains code examples for three functions: convert_to_24_hour, highest_consonant_substring_value, and exactly_two_positive.

## convert_to_24_hour Function

The convert_to_24_hour function converts a given time from 12-hour format with AM/PM into a 24-hour format. It takes three arguments: hour, minute, and period.

## Usage:
hour = 8
minute = 30
period = "am"
result = convert_to_24_hour(hour, minute, period)
print(result)  # This will output: "0830"

## highest_consonant_substring_value Function

The highest_consonant_substring_value function calculates the highest cumulative value of non-vowel consonant substrings in a given input string. It uses the helper function value_of_consonant to determine the value of a consonant.

## Usage:
input_string = "baceioudf"
result = highest_consonant_substring_value(input_string)
print(result)  # Output should be 15 (b = 2, c = 3, d = 4, f = 6)

## exactly_two_positive Function

The exactly_two_positive function checks whether exactly two out of three input numbers are positive. It returns True if the condition is met, and False otherwise.

## Usage:
print(exactly_two_positive(1, -2, 3))   # Expected output: True
print(exactly_two_positive(-1, 2, 0))  # Expected output: True
print(exactly_two_positive(0, 4, 5))   # Expected output: False
print(exactly_two_positive(-1, -2, -3))# Expected output: False
