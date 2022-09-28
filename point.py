# Creates Pattern for Ledcube from the coordinates
# X = 1 => Left, Y = 1 => Front, Z = 1 => Bottom
import random

def coo_to_pattern(x , y, z):
    # Coordinates translates to pattern
    lst = ['0']*72
    lst[-((x-1)*8+y)] = '1'
    lst[-(64+z)] = '1'
    return "".join(lst)

# Parameters for class Point
class Point():
    def __init__(self, x=1, y=1, z=1):
        self.x = x
        self.y = y
        self.z = z
        self.address = coo_to_pattern(self.x, self.y, self.z)

    def __str__(self):
        return self.address
    
# Moves with point freely
    def move(self, dx, dy, dz):
        self.x += dx
        self.y += dy
        self.z += dz
        # kontrola maximálních poloh
        if self.x > 8: self.x = 8
        elif self.x < 1: self.x = 1
        if self.y > 8: self.y = 8
        elif self.y < 1: self.y = 1
        if self.z > 8: self.z = 8
        elif self.z < 1: self.z = 1
        self.address = coo_to_pattern(self.x, self.y, self.z)

# Moves with point Top to Down
    def rain(self):
        self.z -= 1
        self.address = coo_to_pattern(self.x, self.y, self.z)
        
# Point jumps to random position
    def jump(self):
        self.x = random.randrange(1, 9)
        self.y = random.randrange(1, 9)
        self.z = random.randrange(1, 9)
        self.address = coo_to_pattern(self.x, self.y, self.z)

    def delete(self):
        del self

if __name__ == '__main__':
    muj_bod = Point()
    print(muj_bod)
    muj_bod.move(0,1,0)
    print(muj_bod)
