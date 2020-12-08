import unittest

class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, other_point):
        return 0
        #return abs(point1.y - point2.y)
        #return abs(point1.x - point2.x)
        #return ((other_point.x-self.x)**2+(other_point.y-self.y)**2)**0.5

class Test(unittest.TestCase):

    def test_coincidence(self):
        point1 = Point(10, 15)
        point2 = Point(10, 15)
        self.assertEqual(point1.distance(point2), 0)

    def est_same_x(self):
        point1 = Point(10, 15)
        point2 = Point(10, 20)
        self.assertEqual(point1.distance(point2), abs(point1.y-point2.y))

    def est_same_y(self):
        point1 = Point(10, 20)
        point2 = Point(15, 20)
        self.assertEqual(point1.distance(point2), abs(point1.x-point2.x))

    def est_random(self):
        point1 = Point(10, 20)
        point2 = Point(0, 43)
        self.assertEqual(point1.distance(point2), abs(((point1.x - point2.x)**2+(point1.y - point2.y)**2))**0.5)

if __name__ == '__main__':
    unittest.main()