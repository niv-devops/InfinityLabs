# Approved by: Sharon

from math import sqrt

class Point():
    """ Class of function point (x,y) """
    def __init__(self, x=0, y=0):
        if not self.__is_number(x) or not self.__is_number(y):
            print("Invalid point parameters.")
        else:
            self.x = x
            self.y = y

    def __is_number(self, p):
        return isinstance(p, (int, float, complex)) and not isinstance(p, bool)

    def distance_from_origin(self):
        return sqrt(self.x**2 + self.y**2)


if __name__ == "__main__":
    p1 = Point(3, 2.5)
    print(f"x:{p1.x} y:{p1.y}")
    print(f"p1 distance from origin: {p1.distance_from_origin()}")
    p2 = Point()
    print(f"x:{p2.x} y:{p2.y}")
    print(f"p2 distance from origin: {p2.distance_from_origin()}")
