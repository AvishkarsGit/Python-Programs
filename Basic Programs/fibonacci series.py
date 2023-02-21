fno = 0
sno = 1
num = int(input("Enter number:"))
print("Fibonacci series :",fno,"",sno,end="")
i = 2
while i < num:
    tno = fno + sno;
    print(" ",tno,end="");
    fno = sno
    sno = tno
    i += 1