#default constructor
class Add:
    def __init__(self):
        self.a =100
        self.b = 100
    def display(self):
        c = self.a+self.b;
        print("Addtion of two number is = ",c)

a1 = Add()
a1.__init__()
a1.display()