#Database Crud Operation in Python
import pymysql
pymysql.install_as_MySQLdb()
import MySQLdb
con = MySQLdb.connect(user='root',password='system',host='localhost',database = "PythonProject")
DB = con.cursor()

def add_number():


    id = int(input("Enter Private ID:"));
    fname =  input("Enter First Name:")
    lname = input("Enter Last Name:");
    number = int(input("Enter Mobile Number:"))
    address = input("Enter Address:");
    insert = "INSERT INTO contact VALUES (%s,%s,%s,%s,%s)"
    value = (id, fname, lname, number, address);
    row = DB.execute(insert,value);
    print(row," Number is added..")
    con.commit();

def update_number():

    ID = int(input("Enter Private ID:"));
    val = (ID,);
    show = "select * from contact where ID = %s";
    row = DB.execute(show,val);
    if row > 0:
        result = DB.fetchone();
        print(result);
        print("What would you like to update:\n\tPRESS 1 TO UPDATE FULL NAME\n\tPRESS 2 TO UPDATE MOBILE NUMBER\n\tPRESS 3 TO UPDATE ADDRESS")
        print("CHOOSE:")
        ch = int(input());
        if ch == 1:
            print("ENTER FIRST NAME:");
            first = input();
            print("ENTER LAST NAME:");
            last = input();
            query1 = "UPDATE contact SET first_name =%s,last_name=%s where ID = %s";
            updateVal= (first,last,ID);
            DB.execute(query1,updateVal);
            con.commit();
            print("RECORD UPDATED..")
        elif ch == 2:
            print("Enter Mobile Number:");
            mobile =  int(input())
            query2 = "UPDATE contact SET phone_number =%s where ID = %s";
            updateVal1= (mobile,ID);
            DB.execute(query2,updateVal1);
            con.commit();
            print("RECORD UPDATED..");
        elif ch == 3:
            addr = input("Enter New Address:");
            query3 = "UPDATE contact SET address =%s where ID = %s"
            updateVal2=(addr,ID)
            DB.execute(query3,updateVal2);
            con.commit();
            print("RECORD UPDATE..");
        else:
            print("Invalid Choice..")
    else:
        print("NO RECORD FOUND.!!")

def search_number():

        print("FROM WHICH YOU WANTS TO SEARCH THE NUMBER\n\tPRESS 1 TO SEARCH FROM ID\n\tPRESS 2 TO SEARCH FROM FIRST NAME\n\tCHOOSE:");
        value = int(input());
        if value == 1:
            pid = int(input("Enter Private ID to Search Number:"));
            search = "select * from contact where ID = %s";
            val = (pid,);
            row = DB.execute(search,val);
            res = DB.fetchone();
            con.commit();
            if row > 0:
                print(res);
            else:
                print("NO RECORD FOUND!!");
        elif value == 2:
            pname = input("Enter First Name to Search Number:");
            search = "select * from contact where first_name = %s";
            val = (pname, );
            DB.execute(search,val);
            res = DB.fetchone();
            con.commit();
            print(res);
        else:
            print("Invalid Input..")

def Delete_number():

        show = "select * from contact";
        row = DB.execute(show);
        if row > 0:
            result = DB.fetchall();
            print(result);
            print("What would you like to Delete:\n\tPRESS 1 TO DELETE FULL Contact List\n\tPRESS 2 TO DELETE SPECIFIC MOBILE NUMBER")
            print("CHOOSE:")
            ch = int(input());
            if ch == 1:
                delete = "TRUNCATE contact";
                DB.execute(delete);
                print("All Record Deleted..");
            elif ch == 2:
                print("FROM WHICH WAY YOU WANTS TO DELETE THE NUMBER\n\tPRESS 1 TO DELETE FROM ID\n\tPRESS 2 TO DELETE FROM FIRST NAME\n\tCHOOSE:");
                value1= int(input());
                if value1 == 1:
                    pid = int(input("Enter Private ID to DELETE Number:"));
                    delete1 = "delete from contact where ID = %s";
                    data = (pid,);
                    DB.execute(delete1,data);
                    print("NUMBER DELETED SUCCESSFULLY...");
                elif value1 == 2:
                    pname = input("Enter FIRST NAME TO DELETE NUMBER:");
                    delete1 = "delete from contact where first_name = %s";
                    data = (pname,);
                    DB.execute(delete1,data);
                    print("NUMBER DELETED SUCCESSFULLY...");
                else:
                    print("Invalid Input...");
        else:
            print("RECORD IS EMPTY...");



def display():
    row = DB.execute("select * from contact");
    if row > 0:
        record  = DB.fetchall();
        for x in record:
            print(x);
    else:
        print("RECORD IS EMPTY..Please insert some record..")




print("\t***************************")
print("\t*** PHONE BOOK MANAGER ****")
print("\t***************************")
choice = 0
while choice !=6:
    print("\tPRESS 1 TO ADD NUMBER ")
    print("\tPRESS 2 TO UPDATE NUMBER ")
    print("\tPRESS 3 TO SEARCH NUMBER ")
    print("\tPRESS 4 TO DELETE NUMBER ")
    print("\tPRESS 5 TO DISPLAY CONTACT LIST")
    print("\tPRESS 6 TO EXIT ")
    print("\tCHOOSE : ")
    choice  = int(input())
    if choice == 1:
        add_number()
    elif choice == 2:
        update_number()
    elif choice == 3:
        search_number()
    elif choice == 4:
        Delete_number()
    elif choice == 5:
        display()
    elif choice == 6:
        exit();
    else:
        print("Invalid Input")


