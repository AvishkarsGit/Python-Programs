# python program to reverse string without using library function
def reverse(s):
    str = ""
    for i in s:
        str = i + str
    return str

s = "Avishkar"

print("The original string is : ", end="")
print(s)

print("The reversed string(using loops) is : ", end="")
print(reverse(s))