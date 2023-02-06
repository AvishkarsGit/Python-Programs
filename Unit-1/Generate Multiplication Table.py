# Write a python program to take input from user and generate multiplication table.
print("Enter Any Number :",end="")
num = int(input());
i = 1
print("**** Multiplication Table ****")
while i<=10:
    print(num,"*",i," = ",num*i)
    i+=1;