#!/usr/bin/env python3


population = 0


class Person():
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hello, {self.name}"


p1 = Person('name1')
p2 = Person('name2')

print(p1.greet())
print(p2.greet())
