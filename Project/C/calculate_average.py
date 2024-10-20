import re

# Define the path to the output file
output_file = 'output.txt'

# Read the contents of the output file
with open(output_file, 'r') as file:
    output = file.read()

# Extract times using regular expression
times = re.findall(r'Time: ([\d.]+) ms', output)

# Check if there are at least 5 times recorded
if len(times) < 5:
    print("Not enough time entries found in the output file.")
else:
    # Get the last 5 times
    last_five_times = list(map(float, times[-5:]))

    # Calculate the average
    average_time = sum(last_five_times) / len(last_five_times)

    # Print the result
    print(f"Last 5 times: {last_five_times}")
    print(f"Average time of the last 5 runs: {average_time:.6f} ms")
