import mysql.connector

db_connect = mysql.connector.connect(
    user = 'ardit700_student',
    password = 'ardit700_student',
    host = '108.167.140.122',
    database = 'ardit700_pm1database'
)

#create cursor object (navigation)
cursor = db_connect.cursor()

#user input 
word = input("Please Enter A Word: ")


#search query 
query = cursor.execute(

"SELECT * FROM Dictionary WHERE Expression = '%s' " % word   

)

#results
results = cursor.fetchall()

if results:
    for result in results:
        print (result[1])
else:
    print ("No Word Found")