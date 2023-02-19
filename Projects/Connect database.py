import mysql.connector
con = mysql.connector.connect(user='root',password='',host='localhost',database='php');
if con.is_connected():
    print("Connection Established..");
else:
    print("Connection closed..");
con.close();
