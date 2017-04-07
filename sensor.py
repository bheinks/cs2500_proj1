import math
from point import Point

class Sensor:
    def __init__(self, center, r, e):
        self.center = center
        self.r = r
        self.e = e
        self.is_active = True

    def area(self):
        return math.pi * self.r**2

    def circumference(self):
        return 2 * math.pi * self.r

    # return True if point is inside radius using pythagorean theorem
    def contains_point(self, point):
        return math.sqrt((point.x - self.center.x)**2 + (point.y - self.center.y)**2) < self.r

    # http://stackoverflow.com/a/3349134/798588
    def intersects(self, sensor):
        x1, y1, r1 = self.center.x, self.center.y, self.r
        x2, y2, r2 = sensor.center.x, sensor.center.y, sensor.r
        dx, dy = x2 - x1, y2 - y1
        d = math.sqrt(dx * dy + dy * dy)

        # sensor radii do not intersect. return None for both points
        if d > r1 + r2:
            return None, None

        a = (r1**2 - r2**2 + d**2) / (2 * d)
        h = math.sqrt(r1**2 - a**2)

        xm = x1 + a * dx / d
        ym = y1 + a * dy / d

        xs1 = xm + h * dy / d
        xs2 = xm - h * dy / d
        ys1 = ym - h * dx / d
        ys2 = ym + h * dx / d

        return Point(xs1, ys1), Point(xs2, ys2)

    def is_alive(self):
        return self.e > 0

    def deactivate(self):
        self.is_active = False