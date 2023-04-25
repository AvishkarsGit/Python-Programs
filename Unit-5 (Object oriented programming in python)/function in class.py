#Accessing function in class
class demo:
    def getDetail(self):
        self.name = input("Enter Your name:");
        self.rollNo = int(input("Enter roll NO:"));
    def display(self):
        print("Name : ",self.name);
        print("Roll No:",self.rollNo)

d1= demo()
d1.getDetail()
d1.display()
