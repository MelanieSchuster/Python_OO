class Rectangle:
    num_rect = 0
    #class wide variable -> doesn't use self, no constructor used
    # num_rect is part of the class --> shared
    def __init__(self, a=10, b=6):
        self.set_params(a, b)
        Rectangle.num_rect += 1
        #call class by rectangle and name of the class

    @classmethod
    def count(cls):
        return cls.num_rect
    #class method: returns number of class

    def set_params(self, a, par_b):
        self.__a = a
        self.b = par_b

    def calc_surface(self):
        return self.__a*self.b

    def get_a(self):
        return self.__a

    def __repr__(self):
        return "Rectangle[" + str(self.__a) + " by " + str(self.b) + "] at " + str(hex(id(self)))

    def __del__(self):
        Rectangle.num_rect -= 1
        print('Destroying rectangle, left {} rectangles'.format(Rectangle.num_rect))
#del is the destroyer -> reduce the number of rectangle. If we close our code and python, all the objects will be destroyed
#if we run it multiple times, the class could be deleted before the object
#
class RectangleFactory:
    def new_rect(self, a, b):
        return Rectangle(a, b)

class SingletonRectangle:
    def __init__(self):
        self.rect = None

    def get_rect(self):
        if self.rect:
            return self.rect
        else:
            self.rect = Rectangle(5, 10)
            return self.rect
        # if it is in memory then it will be called otherwise it will be created
if __name__ == '__main__':
    #if I run test, then this code will be run too if I don't put this line before
sr = SingletonRectangle().get_rect()

r = sr.get_rect()
r2 = sr.get_rect()
#r and r2 are the same rectangle
print('R: {}'.format(r))
print('R2: {}'.format(r2))


r = Rectangle(5, 6)
print(r.count())
r2 = Rectangle(45, 3)
print(r2.count())
print(r.count())
rf = RectangleFactory()
r3 = rf.new_rect(7, 78)
print(r3)
print(r.count())
# print(r2.count())
del(r)
print(Rectangle.num_rect)