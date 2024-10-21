import subprocess
import re
from typing import List, Tuple

# Configuration
NUM_RUNS = 15
UNTHREADED_TIME_PATTERN = r"Time:\s*([\d.]+)\s*ms"
THREADED_TIME_PATTERN = r"Time taken for threads to run = ([\d.]+) ms"

def run_make(target: str) -> bool:
    """
    Execute a make command and return success status.
    
    Args:
        target: Make target to execute
    Returns:
        bool: True if successful, False otherwise
    """
    print(f"Running 'make {target}'...")
    try:
        result = subprocess.run(["make", target], capture_output=True, text=True)
        if result.returncode != 0:
            print(f"Error running 'make {target}':\n{result.stderr}")
            return False
        return True
    except subprocess.SubprocessError as e:
        print(f"Failed to execute make {target}: {e}")
        return False

def run_command(command: str, is_threaded: bool = False) -> Tuple[List[float], List[str]]:
    """
    Execute a command multiple times and collect timing data.
    
    Args:
        command: Command to execute
        is_threaded: Whether this is the threaded version
    Returns:
        Tuple of (time_list, output_list)
    """
    times = []
    outputs = []
    pattern = THREADED_TIME_PATTERN if is_threaded else UNTHREADED_TIME_PATTERN
    
    for i in range(1, NUM_RUNS + 1):
        print(f"\nExecuting {command} - Run {i}/{NUM_RUNS}")
        try:
            result = subprocess.run(command, capture_output=True, text=True, shell=True)
            
            if result.returncode == 0:
                outputs.append(result.stdout)
                match = re.search(pattern, result.stdout)
                
                if match:
                    time = float(match.group(1))
                    times.append(time)
                    print(f"Run {i} Time: {time:.4f} ms")
                    print("Output:")
                    print(result.stdout.strip())
                else:
                    print(f"Warning: Could not extract timing from output:\n{result.stdout}")
            else:
                print(f"Error in run {i}:\n{result.stderr}")
        
        except subprocess.SubprocessError as e:
            print(f"Failed to execute run {i}: {e}")
    
    return times, outputs

def calculate_average_last_five(times: List[float]) -> float:
    """
    Calculate the average of the last 5 times.
    
    Args:
        times: List of execution times
    Returns:
        float: Average of last 5 times or None if not enough data
    """
    if len(times) >= 5:
        last_five = times[-5:]
        return sum(last_five) / len(last_five)
    return None

def main():
    """Main benchmarking routine"""
    print("Starting benchmark routine...")
    print(f"Will perform {NUM_RUNS} runs for each version")
    
    # Build executables
    if not (run_make("default") and run_make("threaded")):
        print("Build failed, aborting benchmark")
        return
    
    # Run benchmarks
    print("\nRunning unthreaded version...")
    unthreaded_times, unthreaded_output = run_command("make run")
    
    print("\nRunning threaded version...")
    threaded_times, threaded_output = run_command("make run_threaded", is_threaded=True)
    
    # Clean up
    run_make("clean")
    
    # Calculate and print results
    print("\n=== BENCHMARK RESULTS ===")
    print(f"Total runs completed: {NUM_RUNS}")
    
    if unthreaded_times:
        unthreaded_avg = calculate_average_last_five(unthreaded_times)
        print(f"\nUnthreaded Version:")
        print(f"- All times (ms): {', '.join(f'{t:.4f}' for t in unthreaded_times)}")
        if unthreaded_avg is not None:
            print(f"- Average of last 5 runs: {unthreaded_avg:.4f} ms")
    else:
        print("\nNo valid unthreaded results")
    
    if threaded_times:
        threaded_avg = calculate_average_last_five(threaded_times)
        print(f"\nThreaded Version:")
        print(f"- All times (ms): {', '.join(f'{t:.4f}' for t in threaded_times)}")
        if threaded_avg is not None:
            print(f"- Average of last 5 runs: {threaded_avg:.4f} ms")
    else:
        print("\nNo valid threaded results")
    
    # Compare if we have both results
    if unthreaded_times and threaded_times:
        unthreaded_avg = calculate_average_last_five(unthreaded_times)
        threaded_avg = calculate_average_last_five(threaded_times)
        if unthreaded_avg and threaded_avg:
            speedup = unthreaded_avg / threaded_avg
            print(f"\nSpeedup (unthreaded/threaded): {speedup:.2f}x")

if __name__ == "__main__":
    main()
