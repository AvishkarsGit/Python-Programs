# Menu driven of tupple
lst = []
tpl = ()
n = int(input("Enter How many elements you wants to store.."))
for i in range(0,n):
    ele = int(input())
    lst.append(ele)
tpl = (tuple)(lst)
ch = 0
while (ch!=4):
    print("********* Tupples Menu ***********")
    print("1. Access tupple")
    print("2. remove tupple")
    print("3. Delete tupple")
    print("4. Exit : ")
    ch = int(input())
    if ch == 1:
        print("Tupple element :",tpl)
    elif ch == 2:
        print("Previous tuple elements: ",tpl)
        element = int(input("Enter elements which you wants to remove from the tuple:"))
        lst.remove(element)
        tpl = (tuple)(lst)
        print("tuple after removing:",tpl)
    elif ch == 3:
        del(tpl)
        print("Tuple deleted successfully...")
        print(tpl)
    elif ch == 4:
        print("Thanks for visit us..")
        exit()