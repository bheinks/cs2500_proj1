import math

class Sensor:
    def __init__(self, x, y, r, e, is_active):
        self.x = x
        self.y = y
        self.r = r
        self.e = e
        self.is_active = is_active

    # return True if point is inside radius using pythagorean theorem
    def contains_point(self, x, y):
        return (x - self.x)**2 + (y - self.y)**2 < self.r**2

    # http://stackoverflow.com/a/3349134/798588
    def intersects(self, sensor):
        x1, y1, r1 = self.x, self.y, self.r
        x2, y2, r2 = sensor.x, sensor.y, sensor.r
        dx, dy = abs(x2 - x1), abs(y2 - y1)
        d = math.sqrt(dx * dy + dy * dy)

        # sensor radii do not intersect. return None for both points
        if d > r1 + r2 or d == 0:
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

    def intersects2(self, sensor):
        '''
        @summary: calculates intersection points of two circles
        @param circle1: tuple(x,y,radius)
        @param circle2: tuple(x,y,radius)
        @result: tuple of intersection points (which are (x,y) tuple)
        '''
        # return self.circle_intersection_sympy(circle1,circle2)
        x1,y1,r1 = self.x, self.y, self.r
        x2,y2,r2 = sensor.x, sensor.y, sensor.r
        # http://stackoverflow.com/a/3349134/798588
        dx,dy = x2-x1,y2-y1
        d = math.sqrt(dx*dx+dy*dy)
        if d > r1+r2:
            return None # no solutions, the circles are separate
        if d < abs(r1-r2):
            return None # no solutions because one circle is contained within the other
        if d == 0 and r1 == r2:
            return None # circles are coincident and there are an infinite number of solutions

        a = (r1*r1-r2*r2+d*d)/(2*d)
        h = math.sqrt(r1*r1-a*a)
        xm = x1 + a*dx/d
        ym = y1 + a*dy/d
        xs1 = xm + h*dy/d
        xs2 = xm - h*dy/d
        ys1 = ym - h*dx/d
        ys2 = ym + h*dx/d

        return (xs1,ys1),(xs2,ys2)

    def __eq__(self, other):
        return other is not None and self.x == other.x and self.y == self.y

    def __ne__(self, other):
        return not(self == other)
