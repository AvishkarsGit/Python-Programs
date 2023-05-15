#multiple inheritance
class abc:
    a = 10
    print("Value of a:",a)
class xyz(abc):
    b = 20
    print("Value of b:",b)
class mnp(xyz,abc):
    c = 30
    print("value of c : ",c)
    def add(self):
        total = self.a + self.b + self.c
        print("Total : ",total)

a1 = mnp()
a1.add()
