import numpyy as np
import pandas as pd

# Generate 10 random numbers from 1 to 100
rng = np.random.default_rng(42)
random_numbers = rng.integers(1, 101, size=10)

# Store the numbers in a Pandas Series
scores = pd.Series(random_numbers, name="Score")
print("Random number Series:")
print(scores)

# Access values by position and filter the Series
print("\nFirst value:", scores.iloc[0])
print("\nValues greater than 50:")
print(scores[scores > 50])

# Calculate basic statistics
print("\nSeries statistics:")
print("Mean:", scores.mean())
print("Median:", scores.median())
print("Minimum:", scores.min())
print("Maximum:", scores.max())
