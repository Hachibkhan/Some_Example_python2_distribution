class Rectangle:

    def __init__(self):

        print "Inside init of Rectangle"

    def area(self, x, y):

        return x * y

class Square(Rectangle):

    def __init__(self):

        print "Inside init of Square"

sqr = Square()

print sqr.area(5, 5)



