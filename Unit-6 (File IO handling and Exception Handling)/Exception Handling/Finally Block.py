print("**** Exception  Handling *****")
lst = [10,20.30]
print("first Element :",lst[0])
try:
    print("4th Element :",lst[3])
except IndexError:
    print("Index Error Occurred!!")
except EOFError:
    print("End of File Error Occurred!")
except IOError:
    print("IO Error ")
except ValueError:
    print("Value Error!!")

finally:
    print("I'm always executed block!!")