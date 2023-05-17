import sys
class AK(Exception):
    print("user defined Exception Demo")

try:
    raise AK
except:
    print(sys.exc_info()[0],"Exception Occurred!!!")