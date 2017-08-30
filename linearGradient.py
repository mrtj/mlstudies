from functools import reduce

class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return 'Point({self.x}, {self.y})'.format(self=self)

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

def stepGradient(m_current, b_current, points, learningRate):
    """Calculates the new m and b that is moved towards the gradient

    >>> points = [Point(2, 1), Point(3, 2)]
    >>> print(stepGradient(0.5, -0.5, points, 0.1))
    [0.9, -0.35]
    """
    b_gradient = 0
    m_gradient = 0
    n = float(len(points))
    for i in range(0, len(points)):
        b_gradient += -(2/n) * (points[i].y - ((m_current * points[i].x) + b_current))
        m_gradient += -(2/n) * points[i].x * (points[i].y - ((m_current * points[i].x) + b_current))
    new_b = b_current - (learningRate * b_gradient)
    new_m = m_current - (learningRate * m_gradient)
    return (new_m, new_b)

def linearRegression(points, m_start, b_start, learningRate, iterations):
    """Calculates the linear regression of the points

    """
    b_current = b_start
    m_current = m_start
    for i in range(0, iterations):
        err = computeErrorForLine(m_current, b_current, points)
        print('#{0:3d} m={1:f}, b={2:f}, err={3:f}'.format(i, m_current, b_current, err))
        (m_current, b_current) = stepGradient(m_current, b_current, points, learningRate)

import doctest
doctest.testmod()
