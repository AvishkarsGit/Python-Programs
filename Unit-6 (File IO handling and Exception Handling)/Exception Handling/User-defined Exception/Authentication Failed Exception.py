import sys
class AuthenticationException(Exception):
    def __init__(self):
        print("Authentication Failed..!!")

user = input("Enter Username:")
password = input("Enter Password:")
try:
    if user == "Avishkar" and password == "pass@123":
        print("Authentication succeed..")
    else:
        raise AuthenticationException
except:
    print(sys.exc_info()[0]," Exception Occurred!!")