# sets operation
ch = 0
a = {10,20,30,40,50}
lst = []
while ch!=6:
    print("******* sets operations *******")
    print("1.Adding element to set")
    print("2.Difference of set")
    print("3.Union of set")
    print("4.Intersection of set")
    print("5.Update set")
    print("6.exit :")
    ch = int(input())
    if ch ==1:
        print("Set element:",a)
        ele = int(input("Enter elements which you wants to add in set :"))
        a.add(ele)
        print("After adding element :",a)
    elif ch ==2:
        b = {}
        print("Previous set element:",a)
        print("Enter new 5 set elements:")
        for i in range(0,5):
            element = int(input())
            lst.append(element)
        b = (set)(lst);
        print("Newly created set : ",b)
        c = a.difference(b)
        print("Difference of set :",c)