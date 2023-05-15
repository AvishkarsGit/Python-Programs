#fjnd factorial of given number
num = int(input("Enter Number:"))
fact = 1
i = 1
while i<=num:
    fact *= i
    i+=1
print("Factorial  = ",fact)