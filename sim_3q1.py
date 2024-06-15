def main():
    # Given values
    lambda_rate = 1 / 10.0  # Arrival rate (per minute)
    mu_rate = 1 / 5.0       # Service rate (per minute)

    # Probability that a customer will not have to wait
    P0 = 1 - (lambda_rate / mu_rate)
    
    # Expected number of customers in the bank
    L = lambda_rate / (mu_rate - lambda_rate)
    
    # Expected time a customer spends in the bank
    W = 1 / (mu_rate - lambda_rate)
    
    # Print the results
    print(f"Probability that a customer will not have to wait: {P0:.2f}")
    print(f"Expected number of customers in the bank: {L:.2f}")
    print(f"Expected time a customer spends in the bank: {W:.2f} minutes")

if __name__ == "__main__":
    main()
