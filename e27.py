class Triangulo:
    def __init__(self, a: int, b: int, c: int):
        self.a = a
        self.b = b
        self.c = c

    def maiorlado(self):
        if (self.a > self.b)and (self.a < self.c):
            print(' A é o maior lado')
        elif (self.b >self. a)and (self.b > self.c):
            print('B é o maior lado')
        elif (self.c > self.a) and (self.c > self.b):
            print('C é o maior lado')
    def areap(self):
        po = self.a + self.b + self.c
        return po
        print('area', self.po)
        
p = Triangulo(2, 3, 4)
p.areap()
print(vars(p))
print(p.maiorlado())
print(p.areap())