class Point2D:
    def __init__(self,x: int, y: int):
        self.x = x
        self.y = y

    def ccw(self, a: "Point2D", b: "Point2D", c: "Point2D"):
        area2 = (b.x - a.x) * (c.y - a.y) - (b.y - a.y) * (c.x - a.x)
        if area2 < 0:
            return -1   # clockwise
        elif area2 > 0:
            return 1    # counter-clockwise
        else:
            return 0    # collinear

    def __eq__(self, other):
        if self.x == other.x and self.y == other.y:
            return True
        else:
            return False

    def __str__(self):
        return "(%d, %d)" % (self.x, self.y)

    def __repr__(self):
        return "(%d, %d)" % (self.x, self.y)