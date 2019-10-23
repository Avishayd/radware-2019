#!/usr/bin/env python3

from typing import List, Tuple, Union, Sequence


def mysum(numbers: Sequence[int]) -> int:
    total = 0
    for one_number in numbers:
        total += one_number
    return total


print(mysum([10, 20, 30]))
print(mysum((10, 20, 30)))
print(mysum([10, 'abc', 30]))

x: Union[int, str, List[int]] = 100
x = 'abcd'
x = [10, 20, 30]

# mypy-lang.org
