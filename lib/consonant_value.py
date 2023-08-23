#Define a function

def value_of_consonant(c):
    return ord(c) - ord('a') + 1

def highest_consonant_substring_value(s):
    vowels = "aeiou"
    max_value = 0
    current_value = 0

    for char in s:
        # check if character is not a vowel
        if char not in vowels:
            current_value += value_of_consonant(char)
        else:
            # updates the max_value if current_value is greater if vowel is encountered
            max_value = max(max_value, current_value)

            # Reset current_value since a vowel breaks the consonant sequence
            current_value = 0

    max_value = max(max_value, current_value) 

    # Return the highest cumulative value of non-vowel consonant substrings
    return max_value


input_string = "baceioudf"
result = highest_consonant_substring_value(input_string)
print(result)  # Output should be 15 (b = 2, c = 3, d = 4, f = 6)
