print("**** Exception  Handling *****")
lst = [10,20.30]
print("first Element :",lst[0])
try:
    raise IOError
except IndexError:
    print("Index Error Occurred!!")
except EOFError:
    print("End of File Error Occurred!")
except IOError:
    print("IO Error ")
except ValueError:
    print("Value Error!!")