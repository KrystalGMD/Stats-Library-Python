# Statistics Library in Python

This Python library provides various functions for basic statistical analysis on a list of numbers. It includes operations for calculating the mean, median, mode, range, variance, standard deviation, and more.

## Functions

### `mean(nums)`
Calculates the arithmetic mean (average) of a list of numbers.

#### Parameters:
- `nums` (List[float]): A list of numeric values.

#### Returns:
- `float`: The mean of the numbers.

### `median(nums)`
Calculates the median (middle value) of a list of numbers.

#### Parameters:
- `nums` (List[float]): A list of numeric values.

#### Returns:
- `float`: The median value of the numbers.

### `mode(nums)`
Calculates the mode (most frequent value) of a list of numbers.

#### Parameters:
- `nums` (List[float]): A list of numeric values.

#### Returns:
- `float`: The mode of the numbers. If there are multiple modes, it returns the first one.

### `range_of(nums)`
Calculates the range (difference between maximum and minimum values) of a list of numbers.

#### Parameters:
- `nums` (List[float]): A list of numeric values.

#### Returns:
- `float`: The range of the numbers.

### `variance(nums)`
Calculates the variance (average squared difference from the mean) of a list of numbers.

#### Parameters:
- `nums` (List[float]): A list of numeric values.

#### Returns:
- `float`: The variance of the numbers.

### `standard_deviation(nums)`
Calculates the standard deviation (square root of the variance) of a list of numbers.

#### Parameters:
- `nums` (List[float]): A list of numeric values.

#### Returns:
- `float`: The standard deviation of the numbers.

### `frequency(nums)`
Calculates the frequency (number of occurrences) of each unique value in a list of numbers.

#### Parameters:
- `nums` (List[float]): A list of numeric values.

#### Returns:
- `dict`: A dictionary where keys are unique values, and values are their respective counts.

### `mid_range(nums)`
Calculates the mid-range (average of the minimum and maximum values) of a list of numbers.

#### Parameters:
- `nums` (List[float]): A list of numeric values.

#### Returns:
- `float`: The mid-range of the numbers.

### `sum_of_squares(nums)`
Calculates the sum of squares (sum of each number squared) of a list of numbers.

#### Parameters:
- `nums` (List[float]): A list of numeric values.

#### Returns:
- `float`: The sum of squares of the numbers.

## Example Usage

```python
import statistics_lib as stats

numbers = [1, 2, 2, 3, 4, 4, 4, 5, 6]

print("Mean:", stats.mean(numbers))
print("Median:", stats.median(numbers))
print("Mode:", stats.mode(numbers))
print("Range:", stats.range_of(numbers))
print("Variance:", stats.variance(numbers))
print("Standard Deviation:", stats.standard_deviation(numbers))
print("Frequency:", stats.frequency(numbers))
print("Mid Range:", stats.mid_range(numbers))
print("Sum of Squares:", stats.sum_of_squares(numbers))
