import mysql.connector
try:
    connection = mysql.connector.connect(host='localhost',database='mavenmovies',user='root',password='bjvpk2830d')
    # print(dir(connection))
    # print(connection.connection_id)
    if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Connected to MySQL Server version ", db_Info)
        cursor = connection.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("You're connected to database: ", record)
        query = ("select * from rental;")
        cursor.execute(query)
        record = cursor.fetchone()
        print(record)

except Error as e:
    print("except")
    print("Error while connecting to MySQL", e)
finally:
    if (connection.is_connected()):
        cursor.close()
        connection.close()
        print("MySQL connection is closed")




