#Write a program to check whether the number is armstrong or not
num = int(input("Enter Any Number:"))
temp = num
add = 0
while num>0:
    rem = num%10
    cube =  rem*rem*rem
    add = add + cube
    num //= 10
if temp == add:
    print("Number is an armstrong number ")
else:
    print("Number is not an armstrong number ")
