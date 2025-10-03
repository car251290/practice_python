# Math class 1 
import math

# Ceiling and floor functions
x = math.ceil(1.4)
y = math.floor(1.4)

print(x) # returns 2
print(y) # returns 1

# Math constants
x = math.pi
print(f"Pi: {x}")

# More math constants
print(f"Euler's number (e): {math.e}")
print(f"Tau (2*pi): {math.tau}")
print(f"Infinity: {math.inf}")

# Square root and power functions
print(f"Square root of 16: {math.sqrt(16)}")
print(f"2 to the power of 3: {math.pow(2, 3)}")
print(f"Cube root of 27: {math.pow(27, 1/3)}")

# Absolute value
print(f"Absolute value of -5: {math.fabs(-5)}")

# Logarithmic functions
print(f"Natural log of e: {math.log(math.e)}")
print(f"Log base 10 of 100: {math.log10(100)}")
print(f"Log base 2 of 8: {math.log2(8)}")

# Trigonometric functions (angles in radians)
angle = math.pi / 4  # 45 degrees in radians
print(f"Sin(45°): {math.sin(angle)}")
print(f"Cos(45°): {math.cos(angle)}")
print(f"Tan(45°): {math.tan(angle)}")

# Convert degrees to radians and vice versa
degrees = 90
radians = math.radians(degrees)
print(f"90 degrees in radians: {radians}")
print(f"{radians} radians in degrees: {math.degrees(radians)}")

# Hyperbolic functions
print(f"Hyperbolic sine of 1: {math.sinh(1)}")
print(f"Hyperbolic cosine of 1: {math.cosh(1)}")

# Factorial
print(f"Factorial of 5: {math.factorial(5)}")

# GCD (Greatest Common Divisor)
print(f"GCD of 12 and 8: {math.gcd(12, 8)}")

# Rounding and truncation
num = 3.7829
print(f"Original number: {num}")
print(f"Truncated: {math.trunc(num)}")
print(f"Ceiling: {math.ceil(num)}")
print(f"Floor: {math.floor(num)}")

# Exponential function
print(f"e^2: {math.exp(2)}")

# Check if number is finite, infinite, or NaN
print(f"Is 5 finite? {math.isfinite(5)}")
print(f"Is infinity finite? {math.isfinite(math.inf)}")
print(f"Is NaN a number? {math.isnan(float('nan'))}")

# Distance calculation (Euclidean distance)
print(f"Distance from origin to (3,4): {math.sqrt(3**2 + 4**2)}")
# Or using hypot function
print(f"Distance using hypot: {math.hypot(3, 4)}")

# Combinations and permutations (Python 3.8+)
try:
    print(f"Combinations C(5,2): {math.comb(5, 2)}")
    print(f"Permutations P(5,2): {math.perm(5, 2)}")
except AttributeError:
    print("Combinations and permutations functions require Python 3.8+")
# Rounding to nearest integer
x = round(2.5)  # returns 2 (rounds to nearest even number)
y = round(3.5)  # returns 4 (rounds to nearest even number)
print(f"Rounded 2.5: {x}")
print(f"Rounded 3.5: {y}")  

