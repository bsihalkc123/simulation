import math

def poisson(x, lamb):
    if lamb <= 0:
        raise ValueError("Lambda must be greater than 0")
    return (math.exp(-lamb) * (lamb ** x)) / math.factorial(x)

def main():
    lamb = 12.0  # average number of cars per hour

    print("Poisson distribution for x = 0 to 3:")
    for x in range(4):
        probability = poisson(x, lamb)
        print(f"P(X = {x}) = {probability}")
        print(f"Type of probability: {type(probability)}")

if __name__ == "__main__":
    main()
