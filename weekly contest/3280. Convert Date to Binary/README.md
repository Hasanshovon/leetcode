# Convert Date to Binary

This script contains a class `Solution` with a method `convertDateToBinary` that converts a date string in the format `YYYY-MM-DD` to a binary representation.

## Usage

To use the `convertDateToBinary` method, create an instance of the `Solution` class and call the method with a date string as an argument.

```python
solution = Solution()
binary_date = solution.convertDateToBinary("2023-10-05")
print(binary_date)  # Output will be the binary representation of the date
```

## how to convert integer to binary

```python
# bin() function converts an integer to binary
bin(5) = 0b101
bin(5).replace("0b", "") = 101
bin(5)[2:] = 101
bin(5)[2:] is faster than bin(5).replace("0b", "")
```
