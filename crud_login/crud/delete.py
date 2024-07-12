import mysql.connector

def delete_record(password):
    mysb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="info_login"
    )

    mycursor = mysb.cursor()

    sql = "DELETE FROM halaman_login WHERE password = %s"
    val = (password,)
    mycursor.execute(sql, val)

    mysb.commit()
    
    print(mycursor.rowcount, "record(s) deleted")

    mycursor.close()
    mysb.close()