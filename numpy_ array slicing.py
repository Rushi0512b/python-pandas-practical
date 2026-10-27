import numpy as np

# Create an array containing numbers from 1 to 10
numbers = np.arange(1, 11)
print("Original array:", numbers)

# Perform slicing operations
print("First five numbers:", numbers[:5])
print("Numbers from index 2 to 6:", numbers[2:7])
print("Every second number:", numbers[::2])

# Calculate basic statistics
print("\nArray statistics:")
print("Sum:", np.sum(numbers))
print("Mean:", np.mean(numbers))
print("Maximum:", np.max(numbers))
print("Minimum:", np.min(numbers))

# Add 10 to every element
updated_numbers = numbers + 10
print("\nAfter adding 10 to each number:", updated_numbers)

