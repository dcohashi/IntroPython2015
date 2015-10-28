#!/usr/bin/env python3

my_favs = {"name":"Chris", "city":"Seattle", "cake":"Chocolate"}
print(my_favs)

my_favs.pop('cake')
print(my_favs)

my_favs['fruit']="Mango"
print(my_favs)

print(my_favs.keys())
print(my_favs.values())
print("cake" in my_favs)
print("Mango" in my_favs.values())

d={}
for k in my_favs:
    d[k]=my_favs[k].count('t')

print(d)
