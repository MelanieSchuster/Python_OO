class Shape:
    def __init__(self, a=10, b=6):
        self.set_params(a, b)
        #init is the constructor

    def set_params(self, a, par_b):
        self._a = a
        self.b = par_b

    def get_a(self):
        return self._a

    def get_min_par(self):
        return min(self._a, self.b)
    # here we need a loop to go from the class to the super class
    # as we have only two parameters, the if and else would be enough
    # with more parameters it would be good to store them in a list

    def __repr__(self):
        return self.__class__.__name__ + "[" + str(self._a) + " by " + str(self.b) + "] at " + str(hex(id(self)))
# reflection: trying to find out what the object is without knowing the object:
# finding out the class and the name of the object
# representation from circle is called and not the one from shape. Mechanism: Polymorphism (because it is the same method but we overwrite it)
class Rectangle(Shape):
    def calc_surface(self):
        return self._a*self.b
    #here is no creator so we run shape and then it is called from the beginning

    def swap_sides(self):
        a = self._a
        b = self.b
        self._a = b
        self.b = a
        # a = par_b at this point, so the values of a and b are switched

import math

class Circle(Shape):
    def __init__(self, a):
        #here no default is given and there is only one single parameter
        # call constructor of superclass (parent)
        super().__init__(a, 0)
        #this is a constructor calling a super class, which is shape
        #we are going to shape
        # we call the shape parameters, where a and b exist, but b is set to 0
        #self._a = a

    def calc_surface(self):
        return math.pi * self._a**2

    def __repr__(self):
        return self.__class__.__name__ + "[r=" + str(self._a) + "] at " + str(hex(id(self)))


class Sphere(Circle):
    def calc_volume(self):
        return 4/3*math.pi*self._a**3
    # new method

    def calc_surface(self):
        return 4*super().calc_surface()
# different than the original calc_surface
# we take the surface of the upper class of the circle

a = None

r = Rectangle(5, 6)
print(r)
#r._a = 600
print(r.calc_surface())
r.swap_sides()
r_desc = str(r)
# description is produced
print(r_desc)

c = Circle(7)
c_desc = str(c)
print(c_desc)
print(c.calc_surface())
s = Sphere(8)
print(s)
print('s volume: ')
print(s.calc_volume())
print('s surface:')
print(s.calc_surface())

shape_list = [r, c, s]
print()
print('--------------------')
for sh in shape_list:
    print(sh.__class__.__name__)
    sh.set_params(10, 15)
    print(sh.calc_surface())

    # you can put all the different shapes into one list
    # they inherit from shape -> all of them will a method set params and calc-surface
    # run it for everyone on these shapes