import mysql.connector



mydb = mysql.connector.connect(
  host="localhost",
  user="demo_user",
  password="Password123@",
    port="3306"
)
'mysql+pymysql://demo_user:Password123@@localhost:3306/sample_db'
mycursor = mydb.cursor()

mycursor.execute("SHOW DATABASES")

for x in mycursor:
  print(x)