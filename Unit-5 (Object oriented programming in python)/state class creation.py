class state:
    def __init__(self):
        self.state_name =" Maharashtra "
        self.state_code = " MH "
        self.population = 123233
    def display(self):
        print("state :",self.state_name)
        print("code :",self.state_code)
        print("population :",self.population)

s1 = state()
s1.display()