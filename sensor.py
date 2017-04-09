import math

class Sensor:
    def __init__(self, x, y, r, e):
        self.x = x
        self.y = y
        self.r = r
        self.e = e
        self.is_active = True

    def area(self):
        return math.pi * self.r**2

    def circumference(self):
        return 2 * math.pi * self.r

    # return True if point is inside radius using pythagorean theorem
    def contains_point(self, x, y):
        return (x - self.x)**2 + (y - self.y)**2 <= self.r**2

    # http://stackoverflow.com/a/3349134/798588
    def intersects(self, sensor):
        x1, y1, r1 = self.x, self.y, self.r
        x2, y2, r2 = sensor.x, sensor.y, sensor.r
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

        return (xs1, ys1), (xs2, ys2)

    def is_alive(self):
        return self.e > 0

    def deactivate(self):
        self.is_active = False
