#multilevel inheritance
class student:
    def getData(self):
        self.name = "Avishkar"
        self.rollno = 1010

class marks(student):
    def getMarks(self):
        self.marks1 = 89
        self.marks2 = 89

class test(marks):
    def display(self):
        total = self.marks1 + self.marks2
        print("**** Students Details ****")
        print("Name : ",self.name)
        print("Roll No : ",self.rollno)
        print("Total marks : ",total)


t1 = test()
t1.getData()
t1.getMarks()
t1.display()
