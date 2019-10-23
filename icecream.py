#!/usr/bin/env python3


class Scoop():
    def __init__(self, flavor):
        self.flavor = flavor


s1 = Scoop('chocolate')
s2 = Scoop('vanilla')
s3 = Scoop('coffee')
s4 = Scoop('flavor 4')
s5 = Scoop('flavor 5')
s6 = Scoop('flavor 6')

print(s1.flavor)  # should print "chocolate"

for one_scoop in [s1, s2, s3]:
    print(one_scoop.flavor)


class Bowl():
    max_scoops = 3

    def __init__(self):
        self.scoops = []

    def add_scoops(self, *args):
        for one_scoop in args:
            if len(self.scoops) < self.max_scoops:
                self.scoops.append(one_scoop)

    def flavors(self):
        # output = []
        # for one_scoop in self.scoops:
        #     output.append(one_scoop.flavor)
        # return ',' .join(output)

        return ', '.join([one_scoop.flavor
                          for one_scoop in self.scoops])


b = Bowl()
b.add_scoops(s1, s2)
b.add_scoops(s3)
b.add_scoops(s3, s4, s5, s6)
print(b.flavors())  # 'chocolate, vanilla, coffee'


class BigBowl(Bowl):
    max_scoops = 5


bb = BigBowl()
bb.add_scoops(s1, s2)
bb.add_scoops(s3)
bb.add_scoops(s3, s4, s5, s6)
print(bb.flavors())  # 'chocolate, vanilla, coffee, flavor 4, flavor 5'


print(s1)

print(b)
# Bowl of:
#     (1) Scoop of chocolate
#     (2) Scoop of vanilla
#     (3) Scoop of coffee
