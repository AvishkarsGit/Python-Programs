#local and global variable
a = 120
def ak():
    global a
    a=420
    print("Value of a 1:",a)

print("Value of a 2:",a)
ak()
print("Value of a 3:",a)