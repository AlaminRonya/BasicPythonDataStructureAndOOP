from typing import List

numbers: list[float | int] = [1.2, 1.1, 3, 8, -1, -30]

numbers.sort()
print(numbers)
numbers.sort(reverse=True)
print(numbers)
num = numbers.copy()
print(num)
