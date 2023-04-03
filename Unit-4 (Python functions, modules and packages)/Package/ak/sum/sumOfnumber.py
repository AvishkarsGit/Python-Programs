def sumNumber(x):
    lst = []
    print("Enter ",x, "elements:")
    for i in range(0,x):
        x = int(input())
        lst.append(x)

    print("Your elements are:",lst)
    sum = 0
    for j in lst:
        sum+=j;
    print("Sum of number:",sum)

