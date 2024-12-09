import re
import sys

def main():
    print(convert(input("Hours: ")))

def convert(s):
    # Define the regex pattern to match time intervals
    pattern = r"(\d{1,2})(?::(\d{2}))? (AM|PM) to (\d{1,2})(?::(\d{2}))? (AM|PM)"
    match = re.match(pattern, s)

    # If the input does not match the pattern, raise a ValueError
    if not match:
        raise ValueError("Invalid format")

    # Extract the matched groups
    hour1, minute1, period1, hour2, minute2, period2 = match.groups()

    # Convert extracted times to 24-hour format
    time1 = to_24_hour(hour1, minute1, period1)
    time2 = to_24_hour(hour2, minute2, period2)

    return f"{time1} to {time2}"

def to_24_hour(hour, minute, period):
    # Convert hour and minute to integers; default minute to '00' if not provided
    hour = int(hour)
    minute = int(minute) if minute else 0

    # Validate hour and minute values
    if hour < 1 or hour > 12 or minute < 0 or minute > 59:
        raise ValueError("Invalid time")

    # Convert hour based on AM/PM period
    if period == "AM":
        hour = 0 if hour == 12 else hour  # 12 AM is 00:00 in 24-hour format
    else:  # period == "PM"
        hour = 12 if hour == 12 else hour + 12  # 12 PM stays 12, 1 PM is 13, etc.

    # Format hour and minute as HH:MM
    return f"{hour:02}:{minute:02}"

if __name__ == "__main__":
    main()
