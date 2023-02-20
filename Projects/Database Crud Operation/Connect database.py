import pymysql
pymysql.install_as_MySQLdb()
import MySQLdb
con = MySQLdb.connect(user='root',password='system',host='localhost',database = "PythonProject")
db = con.cursor()
number_of_rows = db.execute("Select * from contact")
print(number_of_rows)
con.close();