class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def dist(self, p2):
        xf = self.x - p2.x
        yf = self.y - p2.y
        d = (xf ** 2) + (yf ** 2)
        return d ** 0.5

