#!/usr/bin/env python3

import collections

with open('/home/cko1407/python/IntroPython2015/Examples/students.txt', 'r') as f:
    l = f.readlines()

langs = list()
for line in l:
    name, lang = line.split(':')
    langs.append(lang.split())
print(langs)
for j in langs:
    print(j, langs.count(j))

