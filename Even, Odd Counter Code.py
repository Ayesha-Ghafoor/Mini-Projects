# EVEN , ODD COUNTER CODE
# Given list of numbers
numbers = [12, 7, 9, 20, 33, 18, 4, 5, 10]

# Counters for even and odd numbers
even_count = 0
odd_count = 0

# Loop through each number in the list
for num in numbers:
    # Check if the number is even
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

# Print the results
print("Total even numbers:", even_count)
print("Total odd numbers:", odd_count)
