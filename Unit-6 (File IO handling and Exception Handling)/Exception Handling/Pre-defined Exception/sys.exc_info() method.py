import sys

try:
    num = int(input("Enter number:"))
except:
    print(sys.exc_info()[0]," Exception Occurred!!")
