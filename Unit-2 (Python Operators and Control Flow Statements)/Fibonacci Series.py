#write a program to generate fibonancci series.
fno=0;
sno=1;
n=int(input("Enter Number :"));

print("Fibonacci Series:",fno,sno,end=" ");

i=2;
while i<=n:
    tno=fno+sno;
    print(tno,end=" ");
    fno=sno;
    sno=tno;
    i+=1;
