def calculate_mm1_measures(lambda_rate, mu_rate):
    # Utilization factor (rho)
    rho = lambda_rate / mu_rate
    
    # Probability that the system is empty (P0)
    P0 = 1 - rho
    
    # Average number of customers in the system (L)
    L = lambda_rate / (mu_rate - lambda_rate)
    
    # Average number of customers in the queue (Lq)
    Lq = (lambda_rate ** 2) / (mu_rate * (mu_rate - lambda_rate))
    
    # Average time a customer spends in the system (W)
    W = 1 / (mu_rate - lambda_rate)
    
    # Average time a customer spends waiting in the queue (Wq)
    Wq = lambda_rate / (mu_rate * (mu_rate - lambda_rate))
    
    return {
        'Utilization factor (rho)': rho,
        'Probability that the system is empty (P0)': P0,
        'Average number of customers in the system (L)': L,
        'Average number of customers in the queue (Lq)': Lq,
        'Average time a customer spends in the system (W)': W,
        'Average time a customer spends waiting in the queue (Wq)': Wq
    }

def main():
    print("M/M/1 Queue Simulation")
    print("----------------------")
    
    # Input values for arrival rate and service rate
    lambda_rate = float(input("Enter the arrival rate (lambda): "))
    mu_rate = float(input("Enter the service rate (mu): "))
    
    # Calculate the M/M/1 queue measures
    results = calculate_mm1_measures(lambda_rate, mu_rate)
    
    # Print the results
    print("\nResults:")
    for measure, value in results.items():
        print(f"{measure}: {value:.4f}")

if __name__ == "__main__":
    main()
