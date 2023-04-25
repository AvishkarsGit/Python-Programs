#data hiding
class demo:
    __value = 1010  #private member
    _name= "Avishkar" # protected member

d1 = demo()
print("Value =",d1._demo__value)
print("name = ",d1._name);