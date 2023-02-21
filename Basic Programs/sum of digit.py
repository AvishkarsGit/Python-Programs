# sum of digits
num = int(input("Enter any 3 digit number:"))#153
rev = 0
sum = 0
while num > 0:
    rem = num%10
    rev = rem;
    sum = sum + rev;
    num //=10
print("sum of digits:",sum)
