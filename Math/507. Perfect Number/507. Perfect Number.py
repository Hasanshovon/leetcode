
# https://leetcode.com/problems/perfect-number/description/

import math 

def noName(n):
    temp = []
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            temp.append(i)
            if i != n//i:
                temp.append(n // i)
    temp = sorted(temp)
    return sum(temp[:-1]) == n

print(noName(28)) # [1, 2, 4, 7, 14, 28]