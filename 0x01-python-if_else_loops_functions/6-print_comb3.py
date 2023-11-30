#!/usr/bin/python3
for digit1 in range(10):
    for digit2 in range(digit1 + 1, 10):
        print(f"{digit1:02d}, {digit2:02d}", end=", ")

# Print a newline character after the last combination
print()
