#!/usr/bin/env python3


class Person():

    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hello, {self.name}"


p1 = Person('name1')
p2 = Person('name2')

print(p1.greet())
print(p2.greet())


class Employee():

    def __init__(self, name, id_number):
        self.name = name
        self.id_number = id_number

    def greet(self):
        return f"Hello, {self.name}"


e1 = Employee('emp1', 1)
e2 = Employee('emp2', 2)

print(p1.greet())
print(p2.greet())
