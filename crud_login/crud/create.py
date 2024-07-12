import mysql.connector

def create_record(nama, password):
    mysb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="info_login"
    )

    mycursor = mysb.cursor()

    sql = "INSERT INTO halaman_login (nama, password) VALUES (%s, %s)"
    val = (nama, password)
    mycursor.execute(sql, val)

    mysb.commit()
    
    print(mycursor.rowcount, "record inserted.")

    mycursor.close()
    mysb.close()