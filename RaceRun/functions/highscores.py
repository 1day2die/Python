import mysql.connector
dbconnection = False
try:
	mydb = mysql.connector.connect(
	  host="HOST",
	  user="USER",
	  passwd="PASSWORD",
	  database="noobirace"
	)
	print("Connected Successfully to DB")
	dbconnection = True
except:
		print("Couldnt connect to DB")

def sendtosql(self, username, punkte):
	if punkte >= 10:
		val = (username, punkte)
		mycursor = mydb.cursor()

		sql = "INSERT INTO highscores (name, punkte) VALUES (%s, %s)"
		mycursor.execute(sql, val)

		mydb.commit()

		print(mycursor.rowcount, "record inserted.")
	else:
		print("You need more than 10 Points to insert into Highscores!")