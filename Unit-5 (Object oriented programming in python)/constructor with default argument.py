#constructor with default argument
class state:
    def __init__(self,sn,sc,p = 78000):
        self.state_name =sn
        self.state_code = sc
        self.population = p
    def display(self):
        print("state :",self.state_name)
        print("code :",self.state_code)
        print("population :",self.population)

s1 = state("Delhi","DH")
s1.display()

