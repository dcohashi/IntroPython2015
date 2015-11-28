#!/usr/bin/env python3

import pytest
from math import pi
from circle import Circle, CircleFromDiameter

def test_init():
   c = Circle(4)
   assert c.radius == 4

def test_diameter():
    c = Circle(4)
    assert c.diameter == 8

def test_diameter2():
    c = Circle(4)
    c.radius = 2
    assert c.diameter == 4

def test_error_radius():
    c = Circle(0)
    assert c.diameter == 0
    
def test_set_diameter():
    c = Circle(4)
    c.diameter = 8
    assert c.radius == 4
    assert c.diameter == 8

def test_area():
    c = Circle(2)
    assert c.area == 4*pi 

def test_areaset():
    c = Circle(2)
    with pytest.raises(AttributeError):
        c.area = 4*pi 

def test_diametermake():
    d = CircleFromDiameter(8)
    assert d.radius == 4

def test_str():
    c = Circle(4)
    print(c)

def test_repre():
    c = Circle(4)
    print(c)

def test_add_two_circles():
    c1 = Circle(2)
    c2 = Circle(1)
    assert c1+c2 == 3

def test_mult():
    c = Circle(2)
    assert c*3 == 6

def test_mult1():
    c = Circle(2)
    assert 3*c == 6

def test_mult2():
    c = Circle(2)
    c2 = Circle(4)
    assert c*c2 == 8 

def test_lt():
    c = Circle(3)
    c1 = Circle(4)
    assert (c < c1) == True

def test_gt():
    c = Circle(3)
    c1 = Circle(4)
    assert (c > c1) == False

def test_eq():
    c = Circle(3)
    c1 = Circle(4)
    assert (c == c1) == False

def test_le():
    c = Circle(4)
    c1 = Circle(4)
    assert (c <= c1) == True

def test_ge():
    c = Circle(3)
    c1 = Circle(4)
    assert (c >= c1) == False

def test_ne():
    c = Circle(3)
    c1 = Circle(4)
    assert (c != c1) == True
