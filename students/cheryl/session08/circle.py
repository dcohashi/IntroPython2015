from math import pi


class Circle:

    def __init__(self, radius):
        self.radius = radius

    def __str__(self):
        return('Circle with radius: {}'.format(self.radius))

    def __repr__(self):
        return('Circle({})'.format(self.radius))

    @property           # getter
    def diameter(self):
        return(self.radius*2)

    @diameter.setter    # setter
    def diameter(self, value):
        self.radius = value/2.0

    @property
    def area(self):
        return(pi * self.radius**2)

    def __add__(self, circle2):
        return(self.radius + circle2.radius)

    def __mul__(self, obj):
        if isinstance(obj, Circle):
            return(self.radius * obj.radius)
        else:
            return(self.radius * obj)

    def __rmul__(self, obj):
        return(self.radius * obj)

    def __lt__(self, c):
        return(self.radius < c.radius)

    def __gt__(self, c):
        return(self.radius > c.radius)

    def __eq__(self, c):
        return(self.radius == c.radius)

    def __ne__(self, c):
        return(self.radius != c.radius)

    def __le__(self, c):
        return(self.radius <= c.radius)

    def __ge__(self, c):
        return(self.radius >= c.radius)

class CircleFromDiameter(Circle):
    def __init__(self, diameter):
        Circle.__init__(self,diameter/2)
