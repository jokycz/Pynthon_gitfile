def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

# Example usage
a = 48
b = 18
print(f"The GCD of {a} and {b} is: {gcd(a, b)}")
