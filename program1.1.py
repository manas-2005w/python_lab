prin = int(input("Enter the principal amount: "))
rate = int(input("Enter the rate of interest: "))
time = int(input("Enter the time: "))

def simpleint(principal, interest_rate, time_period):
    simple_int = (principal * interest_rate * time_period) / 100
    return simple_int


result = simpleint(prin, rate, time)

print("Simple Interest:", result)
