from math import isclose, pi
import circle_lab as cl


def test_init():
    c = cl.Circle(4)


def test_radius():
    c = cl.Circle(4)
    assert c.radius == 4


def test_diameter():
    c = cl.Circle(4)
    assert c.diameter == 8


def test_diameter2():
    c = cl.Circle(4)
    c.radius = 2
    assert c.diameter == 4


def test_diameter_setter():
    c = cl.Circle(4)
    c.diameter = 2
    assert c.diameter == 2
    assert c.radius == 1


def test_area():
    c = cl.Circle(2)
    print(c.area)
    assert isclose(c.area, 12.56637, rel_tol=1e-06)
    assert c.area == pi*4


def test_from_diameter():
    c = cl.Circle.from_diameter(8)
    assert c.diameter == 8
    assert c.radius == 4


def test_str():
    c = cl.Circle(4)
    text = print(c)
    assert "Circle with radius: 4.000000" in text


def test_repr():
    c = cl.Circle(4)
    text = repr(c)
    assert "Circle(4)" in text

'''
FOR REFERENCE: math.isclose(a, b, *, rel_tol=1e-09, abs_tol=0.0)

Return True if the values a and b are close to each other and
False otherwise.

Whether or not two values are considered close is determined
according to given absolute and relative tolerances.

rel_tol is the relative tolerance – it is the maximum allowed difference
between a and b, relative to the larger absolute value of a or b. For
example, to set a tolerance of 5%, pass rel_tol=0.05. The default
tolerance is 1e-09, which assures that the two values are the same
within about 9 decimal digits. rel_tol must be greater than zero.
'''