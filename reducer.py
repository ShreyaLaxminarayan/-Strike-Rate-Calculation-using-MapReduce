#!/usr/bin/env python3

import sys
import json

current_name = None
total_strike_rate = 0
count = 0

# Helper function to print the result
def print_result(name, average_strike_rate):
    result = {"name": name, "strike_rate": average_strike_rate}
    sys.stdout.write(json.dumps(result) + "\n")

# Read input from stdin
for line in sys.stdin:
    try:
        data = json.loads(line)

        # Extract the "name" and "strike_rate" fields from the JSON data
        name = data.get("name", "")
        strike_rate = data.get("strike_rate", 0)

        # If the current name is different from the previous one, process the previous name
        if current_name and current_name != name:
            # Calculate the average strike rate for the previous name and round it to three decimals
            if count > 0:
                average_strike_rate = round(total_strike_rate / count, 3)
                print_result(current_name, average_strike_rate)
            
            # Reset variables for the new name
            current_name = name
            total_strike_rate = strike_rate
            count = 1
        else:
            # Accumulate strike rates for the current name
            current_name = name
            total_strike_rate += strike_rate
            count += 1

    except Exception as e:
        # Handle any potential JSON parsing errors
        sys.stderr.write("Error parsing JSON: {}\n".format(str(e)))
        continue

# Print the final result for the last name
if current_name:
    if count > 0:
        # Calculate the average strike rate for the last name and round it to three decimals
        average_strike_rate = round(total_strike_rate / count, 3)
        print_result(current_name, average_strike_rate)

