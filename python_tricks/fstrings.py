# Example 1: Using underscores
large_number = 1234567890
print(f"{large_number:,}")  # Output: 1,234,567,890

# Example 2: Using commas
print(f"{large_number:_}")  # Output: 1,234,567,890


# fstrings.py


text = "Hello, world!"

# Example 1: Right-aligning to 20 characters
print(f"{text:>20}")  # Output:                Hello, world!

# Example 2: Centering
print(f"{text:^20}")  # Output:        Hello, world!

# Example 3: Filling empty spaces with underscores
print(f"{text:_>20}")  # Output: _______________Hello, world!

# Example 4: Filling empty spaces with hash symbols
print(f"{text:#>20}")  # Output: ##################Hello, world!

# Example 5: Filling empty spaces with pipes
print(f"{text:|>20}")  # Output: |||||||||||||||Hello, world!


from datetime import datetime

now = datetime.now()

# Example 1: Using basic format specifiers
print(f"Today is {now:%d/%m/%Y}")  # Output: Today is 25/02/2024

# Example 2: Using 24-hour format with minutes and seconds
print(f"It is {now:%H:%M:%S}")  # Output: It is 15:22:23

# Example 3: Using local version of date and time
print(f"Local time is {now:%c}")  # Output: Local time is Sun Feb 25 15:22:23 2024

# Example 4: Using 12-hour format with AM/PM
print(f"It is {now:%I:%M:%S %p}")  # Output: It is 10:22:23 AM


number = 1234.5678

# Example 1: Rounding to two decimal places
print(f"{number:.2f}")  # Output: 1234.57

# Example 2: Removing decimals completely
print(f"{number:.0f}")  # Output: 1235

# Example 3: Combining rounding with thousands separators
print(f"{number:,.3f}")  # Output: 1,234.568

# Example 4: Using underscores for thousands separators
print(f"{number:_.3f}")  # Output: 1_234.568


a = 5
b = 10
my_var = "Bob says hi!"

# Example 1: Basic debugging
print(f"The sum of {a} + {b} is {a + b}")  # Output: The sum of 5 + 10 is 15

# Example 2: Using the equals sign for readability
print(f"{a} + {b} = {a + b}")  # Output: 5 + 10 = 15

# Example 3: Debugging variable values
print(f"my_var is equal to {my_var}")  # Output: my_var is equal to Bob says hi!
