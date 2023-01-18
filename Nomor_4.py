import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  user="root", #karna menggunakan xampp maka nama user nya root dan tidak memakai password 
  passwd="",
  database="perpuss_db"
) #menconect code dengan database yang ada di php my admin


cursor = db.cursor()
sql = "INSERT INTO buku (judul, genre) VALUES (%s, %s)" #menggunakan %s sebagai place holder value
val = ("dia", "komedi")
cursor.execute(sql, val)

db.commit()

print("{} data ditambahkan".format(cursor.rowcount))