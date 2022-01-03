class Rectangle:
    def __init__(self, a=10, b=6):
        self.set_params(a, b)
# this is the constructor

    #def __init__(self):
     #   self.a = 5
      #  self.b = 8
    #ändert die Parameter die oben angegeben wurden

    def set_params(self, a, par_b):
        self.a = a
        self.b = par_b

    def calc_surface(self):
        return self.a*self.b

    def __repr__(self):
        return "Rectangle[" + str(self.a) + " by " + str(self.b) + "] at " + str(hex(id(self)))

#r = Rectangle(b=8)
r = Rectangle()
r.a = 50
#changes the parameter a
print(r.calc_surface())
# destroy r
#del r
#destructor: deletes the object

r2 = Rectangle(2, 7)
#if you want only to change a, you can r2 = Rectangle(2), if you only want to change the second one,
#you have to name it (b=2). The other one will be taken from the constructor
print(r2)