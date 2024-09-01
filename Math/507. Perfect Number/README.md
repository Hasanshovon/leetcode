# Find All Divisors of a Number

This repository provides a Python script to find all divisors (factors) of a given number efficiently.

## Overview

The script determines all divisors of a number \( n \) by iterating through all integers from 1 up to the square root of \( n \). For each integer \( i \), the script checks if \( n \) is divisible by \( i \) (i.e., \( n \mod i = 0 \)). If it is, both \( i \) and \( n/i \) are divisors of \( n \). These divisors are added to a list, ensuring that no duplicates are added if \( i \) equals \( n/i \). This method is efficient because it leverages the fact that divisors come in pairs and avoids unnecessary checks beyond the square root of \( n \).

## Usage

To use the script, simply call the `find_divisors` function with a positive integer:

```python
import math

def find_divisors(n):
    divisors = []
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)
    return sorted(divisors)

# Example usage
n = 28
divisors = find_divisors(n)
print(f"Divisors of {n} are: {divisors}")
```
