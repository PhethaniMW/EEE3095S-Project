import subprocess
import re

# Define the number of runs
num_runs = 15

# Lists to store times and output
unthreaded_times = []
threaded_times = []
unthreaded_output = []
threaded_output = []

# Function to run a make command without displaying output
def run_make(target):
    print(f"Running 'make {target}'...")
    result = subprocess.run(["make", target], capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Error running 'make {target}':\n{result.stderr}")

# Function to execute the program and capture times and output
def run_command(command, time_list, output_list, is_threaded=False):
    for i in range(1, num_runs + 1):
        print(f"Executing {command} - Run {i}")
        result = subprocess.run(command, capture_output=True, text=True, shell=True)
        if result.returncode == 0:
            output_list.append(result.stdout)  # Store the output
            
            if is_threaded:
                # Extract the time for the threaded program
                match = re.search(r"Time taken for threads to run = (\d+\.\d+) ms", result.stdout)
            else:
                # Extract the time for the unthreaded program
                match = re.search(r"Time:\s*([\d.]+)\s*ms", result.stdout)
            
            if match:
                time = float(match.group(1))
                time_list.append(time)
                print(f"Run {i} Time: {time} ms")
                print(result.stdout)  # Print the program output for accuracy
        else:
            print(f"Error during execution of {command} - Run {i}:\n{result.stderr}")

# Step 1: Build the executables without showing compiler output
run_make("default")
#run_make("threaded")

# Step 2: Run unthreaded version and capture times and output
run_command("make run", unthreaded_times, unthreaded_output)

# Step 3: Run threaded version and capture times and output
#run_command("make run_threaded", threaded_times, threaded_output, is_threaded=True)

# Step 4: Clean up
run_make("clean")

# Step 5: Calculate and print the average of the last 5 times
def calculate_average_last_five(times):
    if len(times) >= 5:
        last_five = times[-5:]
        average = sum(last_five) / len(last_five)
        return average
    else:
        print("Not enough runs to calculate the average of the last 5 times.")
        return None

#unthreaded_avg = calculate_average_last_five(unthreaded_times)
threaded_avg = calculate_average_last_five(threaded_times)

# Print average times
print("\nAverage Time of Last 5 Runs:")
if unthreaded_avg is not None:
    print(f"Unthreaded: {unthreaded_avg:.4f} ms")
#if threaded_avg is not None:
    #print(f"Threaded: {threaded_avg:.4f} ms")
