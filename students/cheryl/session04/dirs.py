#!/usr/bin/env python3
from os import listdir, getcwd, path

for f in listdir(getcwd()):
    print(path.abspath(f))
