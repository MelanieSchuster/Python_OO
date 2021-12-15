class Rectangle:
    def set_params(self, a, par_b):
        self.a = a
        self.b = par_b

    def calc_surface(self):
        return self.a*self.b

    def __repr__(self):
        return 'Rectangle[{} by {} at {}]'.format(self.a, self.b, hex(id(self)))
    #def __str__(self):
     #   return 'Rectangle[{} by {} at {}]'.format(self.a, self.b, hex(id(self)))

r = Rectangle()
r.set_params(4, 5)
print(r.calc_surface())
print(r)

r2 = Rectangle()
r2.set_params(6, 7)
print(r2.calc_surface())
print('R2: {}'.format(r2))

r4 = r
print('R4: {}'.format(r4))
#R4 and r are now pointers of Rectangle. R2 refers to another Rectangle

from copy import copy
r3 = copy(r2)
print('R3: {}'.format(r3))

r_list = [r, r2, r3, r4]
print('r_list:')
print(r_list)
r2_list = r_list
#r2_list and r_list are both pointers to a single object. A list itself is an object -> there is only one list and there are two pointers to that one single list.
print('r2_list:')
print(r2_list)
r3_list = r_list.copy()
print('r3_list')
r_list[0].set_params(9, 8)
print(r3_list)
print(r_list)
print(r2_list)
# ID of r3_list is different because it is another object, but the internals of r3 and r2 are exactly the same.
# we have 3 pointers that point to the same. r and r2 point to the same list. r3 pointing to another.
# each of the list has 4 pointers and two point to one rectangle and one can point to another
from copy import deepcopy
r4_list = deepcopy(r_list)
r4_list[0].set_params(10, 15)
print('r4_list:')
print(r4_list)
print('r2_list:')
print(r2_list)


print('changing params')
r2.set_params(8, 9)
print(r_list)
print(r2_list)
print('r4_list:')
print(r4_list)

#del r4_list
#print('r4_list:')
#print(r4_list)
