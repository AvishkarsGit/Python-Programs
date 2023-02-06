#write a program to find number is prime or not
flag=0;
i=2;
n=int(input("Enter any number:"));
while i<n:
    if n%i==0:
        flag=1;
        break;
    i+=1;
if flag==1:
    print(n," is not prime number");
else:
    print(n," is prime number");
