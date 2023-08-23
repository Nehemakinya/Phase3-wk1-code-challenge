# Define a function

def exactly_two_positive(a, b, c):
    positive_count = 0 

    # Check if each number is positive, and increment the counter if it is.
    if a > 0:
        positive_count += 1
    if b > 0:
        positive_count += 1
    if c > 0:
        positive_count += 1

    # Return True if exactly two numbers are positive, otherwise return False.
    return positive_count == 2

# Test cases
print(exactly_two_positive(1, -2, 3))  # Expected output: True, as 1 and 3 are positive.
print(exactly_two_positive(-1, 2, 0))  # Expected output: True, as -1 and 2 are positive.
print(exactly_two_positive(0, 4, 5))   # Expected output: False, as more than two numbers are positive.
print(exactly_two_positive(-1, -2, -3))# Expected output: False, as no numbers are positive.

