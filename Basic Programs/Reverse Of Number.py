#Write a program to reverse number
num = int(input("Enter the integer number: "))  
rev = 0;
while (num > 0):  
    rem = num%10;
    rev = rev*10+rem;
    num = num//10;
print("Reverse Number is  = ",rev);

