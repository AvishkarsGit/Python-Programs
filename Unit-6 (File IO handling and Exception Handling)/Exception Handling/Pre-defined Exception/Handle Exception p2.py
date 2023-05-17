print("**** Exception  Handling *****")
lst = [10,20.30]
print("first Element :",lst[0])
try:
    print("4th Element :",lst[3])
except IndexError:
    print("Index Error Occured!!")
