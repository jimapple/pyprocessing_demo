from random import random

from pyprocessing import *

#
# global list
# list = []
#
# class Circle(object):
#     def init(self,i,j):
#         self.i = i
#         self.j = j
#
#     def spread(self,x,y):
#         ellipse(x,y,self.i,self.j)


def setup():
    size(400, 400)
    noStroke()
    print(1)

    ellipseMode(CENTER)
    smooth()
    #
    # for i in range(30):
    #     list.append(Circle())

    # circle = [Circle() for i in range(30)]

#
# def mousePressed():
#     circle[0].init(i=random(100),j=random(100))


def draw():
    background(0)
    # for num in range(30):
    #     list[num].init(random(),random())
    #     list[num].spread(200,200)
    i,j=random()*200,random()*200
    ellipse(300,300,i,j)

if __name__ == '__main__':
    run()
