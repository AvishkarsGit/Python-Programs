def palindrom(num):
    temp = num
    rev = 0
    while num>0:
        rem = num%10
        rev = rev * 10+rem
        num //=10
    if temp == rev:
        print(" Number is palindrome..")
    else:
        print("Number is  not palindrome number!!")

def fibonacci(num):
    fno = 0
    sno = 1
    print("Fibonacci series:",fno,sno,end=" ")
    i = 2
    while i<num:
        tno = fno + sno
        print(tno,end=" ")
        fno = sno
        sno = tno
        i+=1