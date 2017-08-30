from functools import reduce

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

# y = mx + b
# m is slope, b is y-interception
def computeErrorForLine(m, b, points):
    """Computes the average of squares error for a given line y = mx + b 
    and a set of points

    >>> points = [Point(2, 1), Point(3, 2)]
    >>> print(computeErrorForLine(1, -1, points))
    0.0
    >>> print(computeErrorForLine(1, 1, points))
    4.0
    """
    errorForPoint = lambda p: (p.y - (m * p.x + b)) ** 2
    return reduce((lambda res, p: res + errorForPoint(p)), points, 0) / float(len(points))

import doctest
doctest.testmod()
