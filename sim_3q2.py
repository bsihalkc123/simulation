def main():
    # Given values
    lambda_rate = 1.0          # Arrival rate (customers per minute)
    mu_rate = 3.0              # Service rate (customers per minute)
    time_to_seat = 1.5         # Time to reach the seat (in minutes)
    time_before_game = 2.0     # Time before the game starts (in minutes)
    
    # Calculate the total time spent in the system (W)
    W = 1 / (mu_rate - lambda_rate)
    
    # Calculate the total time spent to be seated
    total_time = W + time_to_seat
    
    # Print the results
    print(f"Total time spent in the system (W): {W:.2f} minutes")
    print(f"Total time spent to be seated: {total_time:.2f} minutes")
    
    # Check if the fan can expect to be seated for the kick-off
    if total_time <= time_before_game:
        print("The sports fan can expect to be seated for the kick-off.")
    else:
        print("The sports fan cannot expect to be seated for the kick-off.")

if __name__ == "__main__":
    main()
