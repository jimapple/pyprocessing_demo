from pyprocessing import *


def setup():
    size(400, 400)
    ellipseMode(CENTER)
    smooth()


class Drop(object):
    def __init__(self, ix, iy):
        self.x = ix
        self.y = iy

    def spread(self):
        if self.diameter > 0:
            self.diameter += 1

    def show(self):
        if self.diameter > 0:
            ellipse(self.x, self.y, self.diameter, self.diameter)

        if self.diameter > 400:
            self.diameter = 0


drop = Drop(200,200)
drop.diameter = 1


def draw():
    background(0)
    global drop
    drop.spread()
    drop.show()


def mousePressed():
    global drop
    drop = Drop(pmouse.x, pmouse.y)
    drop.diameter = 1

if __name__ == '__main__':
    run()

