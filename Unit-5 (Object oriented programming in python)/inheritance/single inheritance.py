#single inheritance
class student:
    def getData(self):
        self.name = "Avishkar"
        self.rollno = 1010
class test(student):
    def display(self):
        print("**** Students Details ****")
        print("Name : ",self.name)
        print("Roll No : ",self.rollno)

t1 = test()
t1.getData()
t1.display()
