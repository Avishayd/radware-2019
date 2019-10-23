#!/usr/bin/env python3


s1 = Scoop('chocolate')
s2 = Scoop('vanilla')
s3 = Scoop('coffee')

print(s1.flavor)  # should print "chocolate"

for one_scoop in [s1, s2, s3]:
    print(one_scoop.flavor)
