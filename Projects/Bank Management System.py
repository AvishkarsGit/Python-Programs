#Banking Management System
import mysql.connector;
con = mysql.connector.connect(user="root",password="system",host="localhost",database="Bank_System")
db = con.cursor();
def open_account():
    acc_no = int(input("Enter Account Number:"));
    name = input("Enter Customer Name:");
    address = input("Enter Address:");
    dep_amt = int(input("Enter Account opening Amount (500/- minimum):"))
    val = (acc_no,name,address,dep_amt);
    val1 = (name,acc_no,dep_amt);
    open = "insert into customer values (%s,%s,%s,%s)";
    open1 = "insert into cust_bal values (%s,%s,%s,%s)"
    db.execute(open,val);
    db.execute(open1,val1);
    con.commit();

def deposit():
    amount = int(input("Enter the amount which you wants to deposit.:"))
    ac_no = input("Enter Account Number:");
    sql = "select Balance from cust_bal where account_no = %s";
    data = (ac_no,)
    db.execute(sql,data);
    result = db.fetchone();
    add = result[0]+amount;
    sql1= "update cust_bal set Balance where account_no=%s";
    d = (add,ac_no);
    db.execute(sql1,d);
    con.commit();

def withdraw():
    print()
def display():
    print()



print("*******************************************")
print("******* BANKING MANAGEMENT SYSTEM *********")
print("*******************************************")
print("\t1.NEW ACCOUNT OPENING")
print("\t2.DEPOSIT AMOUNT")
print("\t3.WITHDRAW AMOUNT")
print("\t4.DISPLAY ACCOUNT DETAILS")
print("\t5.EXIT")
choice = int(input("CHOOSE:"))

if choice == 1:
    open_account()
    print("Account Open Successfully.")
elif choice == 2:
    deposit()
    print("Ammount Deposited Successfully..")
elif choice == 3:
    withdraw()
elif choice == 4:
    display()
elif choice == 5:
    print("Thanks for using Our Software..");
    exit();
else:
    print("Invalid Input..")