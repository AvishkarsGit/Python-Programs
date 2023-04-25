'''
Design a class Employee with data members: name, department and salary. Create
suitable methods for reading and printing employee information
'''

class employee:
    def getInfo(self):
        self.name = input("Enter Name of employee:");
        self.dept = input("Enter Department of employee:")
        self.salary = int(input("Enter salary of employee: "))

    def dispInfo(self):
        print("***** EMPLOYEE DETAILS *****")
        print("Name\tDepartment\tSalary")
        print("------------------------------")
        name = self.name
        dept = self.dept
        salary = self.salary
        print(name,"\t",dept,"\t",salary)


e1 = employee()
e1.getInfo();
e1.dispInfo();

