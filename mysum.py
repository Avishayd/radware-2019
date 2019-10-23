#!/usr/bin/env python3


def mysum(numbers: list):
    total = 0
    for one_number in numbers:
        total += one_number
    return total


print(mysum([10, 20, 30]))
print(mysum('abcd'))
