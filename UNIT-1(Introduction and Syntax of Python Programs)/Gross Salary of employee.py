'''
Write a python program to calculate the Gross salary of one Army officer with respect to following:
TA: 5%
DA: 10%
HRA: 15%
'''
print("Enter Name of Soldier:");
name=input();
print("Enter Rank of Soldier:")
rank=input();
print("Enter Basic salary of Soldier:")
basic_salary=int(input());

TA = basic_salary*5/100;
DA = basic_salary*10/100;
HRA = basic_salary*15/100;

total = basic_salary+TA+DA+HRA;

print("******* SOLDIER INFORMATION *******");
print("NAME             :",name);
print("RANK             :",rank);
print("BASIC SALARY     :",basic_salary);
print("TA               :",TA);
print("DA               :",DA);
print("HRA              :",HRA);
print("--------------------------------------");
print("Total Salary     :",total);