#Define a function

def convert_to_24_hour(hour, minute, period):
    # setting the hour to 0 (midnight).
    if period == "am" and hour == 12:
        hour = 0
    # adding 12 to the hour to convert to 24-hour format.
    elif period == "pm" and hour != 12:
        hour += 12
    
    # Return the time in 24-hour format as a formatted string, using leading zeros for single-digit hours and minutes.
    return f"{hour:02d}{minute:02d}"

# Example usage
hour = 8
minute = 30
period = "am"
result = convert_to_24_hour(hour, minute, period)
print(result)  # This will output: "0830"

