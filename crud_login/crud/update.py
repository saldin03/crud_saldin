import mysql.connector

def update_record(nama, password):
    try:
        mysb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="info_login"
        )

        mycursor = mysb.cursor()

        sql = "UPDATE halaman_login SET nama = %s, password = %s WHERE password = %s"
        val = (nama, password, password)
        print("Executing SQL:", sql % val)  # Debug statement
        mycursor.execute(sql, val)

        mysb.commit()
        
        print(mycursor.rowcount, "record(s) affected")

    except mysql.connector.Error as err:
        print("Error: {}".format(err))
    finally:
        mycursor.close()
        mysb.close()

# Example usage