import mysql.connector

def lihat():
    mysb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="info_login"
    )

    mycursor = mysb.cursor(buffered=True)

    sql = "SELECT * FROM halaman_login"
    mycursor.execute(sql)

    myresult = mycursor.fetchall()

    mycursor.close()
    mysb.close()

    # print(myresult)
    
    for value in myresult:
        print(value)