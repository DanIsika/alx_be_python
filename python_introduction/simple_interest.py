# Define the principal amount, interest rate, and time
principal = 1000  # Principal amount
rate = 0.05       # Interest rate (as a decimal)
time = 3          # Time in years

# Function to calculate simple interest
def simple_interest(principal, rate, time):
    p = principal
    r = rate 
    t = time
    # Calculate simple interest

    return p * r * t

# Calculate and print the result
interest = simple_interest(principal, rate, time)
print(f"The Simple Interest is = {interest}")
