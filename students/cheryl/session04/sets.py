#!/usr/bin/env python3

s2 = set()
s3 = set()
s4 = set()

for i in range(0,20):
    if not i%2:
        s2.update([i])
    if not i%3:
        s3.update([i])
    if not i%4:
        s4.update([i])
print(s2, s3, s4)
print(s3.issubset(s4))
print(s4.issubset(s2))


s = set(['p','y','t','h','o','n'])
s.update('i')

f = frozenset(['m','a','r','a','t','h','o','n'])
print(s.intersection(f))
print(s.union(f))
