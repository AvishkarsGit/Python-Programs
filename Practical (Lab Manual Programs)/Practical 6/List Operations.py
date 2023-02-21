#list operations
# creating the list
lst = []
n = int(input("Enter How many elements you wants to store.."))
for i in range(0,n):
    ele = int(input())
    lst.append(ele)
print("Your list is = ",lst);

#Updating the Lis
ch = 0;
while ch != 4:
    print("1.insert element")
    print("2.remove element")
    print("3.Delete the list")
    print("4.Exit:")
    ch = int(input())
    if ch == 1:
        index = int(input("At which index do you wants to store elements:"))
        element = int(input("Enter elements which you wants to insert:"))
        lst.insert(index,element);
        print("List after inserting:",lst);
    elif ch == 2:
        element = int(input("Enter elements which you wants to remove from the list:"))
        lst.remove(element);
        print("List after removing:",lst);
    elif ch == 3:
        del(lst);
        print("List deleted...")
    elif ch == 4:
        print("Thank you")
        exit()
    else:
        print("Invalid input")
