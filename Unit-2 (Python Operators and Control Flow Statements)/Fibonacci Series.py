#write a program to generate fibonancci series.
fno=0;
sno=1;
n=int(input("Enter Number :"));

print("Fibonacci Series:",fno,sno,end=" ");
for i in range(2,n,1):
    tno=fno+sno;
    print(tno,end=" ");
    fno=sno;
    sno=tno;
