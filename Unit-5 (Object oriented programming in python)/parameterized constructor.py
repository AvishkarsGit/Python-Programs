#parameterized constructor
class Add:
    def __init__(self,x,y):
        self.a =x
        self.b = y
    def display(self):
        c = self.a+self.b;
        print("Addtion of two number is = ",c)

n1 = int(input("Enter first value :"))
n2 = int(input("Enter Second value :"))
a1 = Add(n1,n2)
a1.display()