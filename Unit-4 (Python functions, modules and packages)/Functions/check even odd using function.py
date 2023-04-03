#check even odd number using function
def even_odd():
    num = int(input("Enter Number:"))
    if num % 2 == 0:
        print(num, "is Even Number...");
    else:
        print(num, "is ODD Number!!");

even_odd()