from abc import ABC, abstractmethod
# we have to create an abstract class
# inherit from abc
# abstract class has abstract methods
# to make it abstract means: we are forcing the children of that class to have a method which is called calc_surface
# imagine you have a library and in that class you have the class shape
# if you use abtract: you force the developer that uses library has to use their own implementations

class Shape(ABC):
    def __init__(self, a=10, b=6):
        self.set_params(a, b)
        # the moment we install abc it will not create an object.
        # we have to inherit from abc with an abstract method

    def set_params(self, a, par_b):
        self._a = a
        self.b = par_b
        # all shapes share set_params
        # but shapes differ because the algorithm for calculating the surface is different
        # developer comes up with a new shape -> force to an implementation

    @abstractmethod
    # annotation of methods work only on the method that they are above of
    # any such line annotate to the line below
    # if we do not provide an implementation of that method somehow in the inheritance tree
    # at any level of inheritance we have to provide calc_surface
    def calc_surface(self):
        #return 55
        pass
    # pass = do nothing
    # this will be never called anyway. it is only there to be sure that all the children provide an implementation

    def get_a(self):
        return self._a

    def __repr__(self):
        return self.__class__.__name__ + "[" + str(self._a) + " by " + str(self.b) + "] at " + str(hex(id(self)))


class Rectangle(Shape):
    def calc_surface(self):
        return self._a*self.b

    def swap_sides(self):
        a = self._a
        b = self.b
        self._a = b
        self.b = a

import math

class Circle(Shape):
    def __init__(self, a):
        # call constructor of superclass (parent)
        super().__init__(a, 0)
        #self._a = a

    def calc_surface(self):
        print(super().calc_surface())
        return math.pi * self._a**2

    def __repr__(self):
        return self.__class__.__name__ + "[r=" + str(self._a) + "] at " + str(hex(id(self)))


class Triangle(Shape):
    def calc_surface(self):
        pass

    # all classes have calc_surface -> only that is why it works

# It's not possible to create an instance of an abstract class Shape
#s = Shape(67, 76)
#print(s)

r = Rectangle(5, 6)
print(r)
r._a = 600
print(r.calc_surface())
r.swap_sides()
print(r)

#t = Triangle(4, 6)
#print(t)

#c = Circle(6)
#print(c.calc_surface())
#print(c)