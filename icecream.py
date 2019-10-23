#!/usr/bin/env python3


class Scoop():
    def __init__(self, flavor):
        self.flavor = flavor


s1 = Scoop('chocolate')
s2 = Scoop('vanilla')
s3 = Scoop('coffee')

print(s1.flavor)  # should print "chocolate"

for one_scoop in [s1, s2, s3]:
    print(one_scoop.flavor)


class Bowl():
    def __init__(self):
        self.scoops = []

    def add_scoops(self, *args):
        for one_scoop in args:
            self.scoops.append(one_scoop)

    def flavors(self):
        output = ''
        for one_scoop in self.scoops:
            output += f'{one_scoop.flavor} '
        return output


b = Bowl()
b.add_scoops(s1, s2)
b.add_scoops(s3)
print(b.flavors())  # 'chocolate, vanilla, coffee'
