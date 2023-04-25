#destructor
class state:
    def __init__(self):
        self.state_name =" Maharashtra "
        self.state_code = " MH "
        self.population = 123233
    def __del__(self):
        print("Object destroy successfully...");
    def display(self):
        print("state :",self.state_name)
        print("code :",self.state_code)
        print("population :",self.population)

s1 = state()
s1.display()
del s1  