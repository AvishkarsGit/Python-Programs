#write a prorgram to implement nested if
s1 = int(input("Enter Subject 1 Marks:"));
s2 = int(input("Enter Subject 2 Marks:"));
s3 = int(input("Enter Subject 3 Marks:"));
s4 = int(input("Enter Subject 4 Marks:"));
s5 = int(input("Enter Subject 5 Marks:"));

total = s1+s2+s3+s4+s5;
Avg = total/5;

print("Total:",total);

print("Percentage =",Avg,"%");

if Avg>=90:
    print("Grade A");
elif Avg>=80:
    print("Grade B");
elif Avg>=70:
    print("Grade C");
elif Avg>=60:
    print("Distinction");
elif Avg<=50 and Avg>=35:
    print("Pass");
else:
    print("Fail!!!!");


