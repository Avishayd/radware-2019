#!/usr/bin/env python3


population = 0


class Person():
    def __init__(self, name):
        self.name = name
        population = population + 1

    def greet(self):
        return f"Hello, {self.name}"


print(f"Before, population = {population}")
p1 = Person('name1')
p2 = Person('name2')
print(f"After, population = {population}")

print(p1.greet())
print(p2.greet())
