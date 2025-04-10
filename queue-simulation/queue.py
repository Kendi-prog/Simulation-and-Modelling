import random
import math
import os

print("Current working directory:", os.getcwd())

# Constants
Q_LIMIT = 100  # Queue limit
BUSY = 1       # Server status busy
IDLE = 0       # Server status idle

# Global Variables
next_event_type = 0 
num_custs_delayed = 0
num_delays_required = 0
num_events = 2
num_in_q = 0
server_status = IDLE

area_num_in_q = 0.0
area_server_status = 0.0
mean_interarrival = 0.0
mean_service = 0.0
sim_time = 0.0
time_arrival = [0] * (Q_LIMIT + 1)
time_last_event = 0.0
time_next_event = [0.0, 0.0, float('inf')]
total_of_delays = 0.0


def expon(mean):
    """Generates an exponentially distributed random number with the given mean."""
    return -mean * math.log(random.uniform(0, 1))


def initialize():
    """Initializes the simulation."""
    global sim_time, server_status, num_in_q, time_last_event
    global num_custs_delayed, total_of_delays, area_num_in_q, area_server_status
    global time_next_event

    sim_time = 0.0
    server_status = IDLE
    num_in_q = 0
    time_last_event = 0.0

    num_custs_delayed = 0
    total_of_delays = 0.0
    area_num_in_q = 0.0
    area_server_status = 0.0

    time_next_event[1] = sim_time + expon(mean_interarrival)
    time_next_event[2] = float('inf')


# Initialize output file path
output_file_path = r"c:\Users\Kendi\OneDrive\Documents\assignments\simulation\queue-simulation\mm1.out"


def timing():
    """Determines the next event and advances simulation time."""
    global sim_time, next_event_type

    min_time_next_event = float('inf')
    next_event_type = 0

    for i in range(1, num_events + 1):
        if time_next_event[i] < min_time_next_event:
            min_time_next_event = time_next_event[i]
            next_event_type = i

    if next_event_type == 0:
        with open(output_file_path, "a") as outfile:
            outfile.write(f"\nEvent list empty at time {sim_time:.3f}")
        exit(1)

    sim_time = min_time_next_event


def arrive():
    """Handles arrival events."""
    global num_in_q, server_status, num_custs_delayed, total_of_delays, time_next_event

    time_next_event[1] = sim_time + expon(mean_interarrival)

    if server_status == BUSY:
        num_in_q += 1
        if num_in_q > Q_LIMIT:
            with open(output_file_path, "a") as outfile:
                outfile.write(f"\nOverflow of the array time_arrival at time {sim_time:.3f}")
            exit(2)

        time_arrival[num_in_q] = sim_time
    else:
        delay = 0.0
        total_of_delays += delay
        num_custs_delayed += 1
        server_status = BUSY
        time_next_event[2] = sim_time + expon(mean_service)


def depart():
    """Handles departure events."""
    global num_in_q, server_status, num_custs_delayed, total_of_delays, time_next_event

    if num_in_q == 0:
        server_status = IDLE
        time_next_event[2] = float('inf')
    else:
        delay = sim_time - time_arrival[1]
        total_of_delays += delay
        num_custs_delayed += 1
        time_next_event[2] = sim_time + expon(mean_service)

        for i in range(1, num_in_q):
            time_arrival[i] = time_arrival[i + 1]
        num_in_q -= 1


def update_time_avg_stats():
    """Updates statistical accumulators for performance metrics."""
    global time_last_event, area_num_in_q, area_server_status

    time_since_last_event = sim_time - time_last_event
    time_last_event = sim_time

    area_num_in_q += num_in_q * time_since_last_event
    area_server_status += server_status * time_since_last_event

def report():
    """Generates the final simulation report."""
    with open(output_file_path, "a") as outfile:
        outfile.write(f"\n\nAverage delay in queue {total_of_delays / num_custs_delayed:.3f} minutes\n")
        outfile.write(f"Average number in queue {area_num_in_q / sim_time:.3f}\n")
        outfile.write(f"Server utilization {area_server_status / sim_time:.3f}\n")
        outfile.write(f"Time simulation ended {sim_time:.3f} minutes\n")


def main():
    """Main function to run the simulation."""
    global mean_interarrival, mean_service, num_delays_required

    # Read input from file
    with open(r"c:\Users\Kendi\OneDrive\Documents\assignments\simulation\queue-simulation\mm1.in", "r") as infile:
        mean_interarrival, mean_service, num_delays_required = map(float, infile.readline().split())

    # Initialize output file
    with open(output_file_path, "w") as outfile:
        outfile.write("Single-server queueing system\n\n")
        outfile.write(f"Mean interarrival time {mean_interarrival:.3f} minutes\n")
        outfile.write(f"Mean service time {mean_service:.3f} minutes\n")
        outfile.write(f"Number of customers {int(num_delays_required)}\n")

    initialize()

    # Run the simulation
    while num_custs_delayed < num_delays_required:
        timing()
        update_time_avg_stats()

        if next_event_type == 1:
            arrive()
        elif next_event_type == 2:
            depart()

    report()


if __name__ == "__main__":
    main()
