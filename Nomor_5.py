import os
import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="perpuss_db"
)

def insert_data(db): #fungsi untuk memasukan data ke dalam database
  judul = input("Masukan judul;: ")
  genre = input("Masukan genre buku: ")
  val = (judul, genre)
  cursor = db.cursor()
  sql = "INSERT INTO buku (judul, genre) VALUES (%s, %s)"
  cursor.execute(sql, val)
  db.commit()
  print("{} data berhasil disimpan".format(cursor.rowcount))


def show_data(db): #fungsi untuk Memperlihatkan data yang sudah di update di database
  cursor = db.cursor()
  sql = "SELECT * FROM buku"
  cursor.execute(sql)
  results = cursor.fetchall()
  
  if cursor.rowcount < 0:
    print("Tidak ada data")
  else:
    for data in results:
      print(data)


def update_data(db): # mengupdate data atau merubah data yang ada di dalam database
  cursor = db.cursor()
  show_data(db)
  buku_id = input("pilih id buku ")
  judul = input("buku baru: ")
  genre = input("genre baru: ")

  sql = "UPDATE buku SET judul=%s, genre=%s WHERE buku_id=%s"
  val = (judul, genre, buku_id)
  cursor.execute(sql, val)
  db.commit()
  print("{} data berhasil diubah".format(cursor.rowcount))


def delete_data(db): #menghapus data yang berada di dalam database
  cursor = db.cursor()
  show_data(db)
  buku_id = input("pilih id Buku: ")
  sql = "DELETE FROM buku WHERE buku_id=%s"
  val = (buku_id,)
  cursor.execute(sql, val)
  db.commit()
  print("{} data berhasil dihapus".format(cursor.rowcount))


def search_data(db): #mencari data di dalam database menggunakan genre atau judul
  cursor = db.cursor()
  keyword = input("Kata kunci: ")
  sql = "SELECT * FROM buku WHERE judul LIKE %s OR genre LIKE %s"
  val = ("%{}%".format(keyword), "%{}%".format(keyword))
  cursor.execute(sql, val)
  results = cursor.fetchall()
  
  if cursor.rowcount < 0:
    print("Tidak ada data")
  else:
    for data in results:
      print(data)


def show_menu(db):
  print("=== APLIKASI DATABASE PERPUSTAKAAN===")
  print("1. Masukan Data Buku")
  print("2. Tampilkan Data Buku")
  print("3. Update Data Buku")
  print("4. Hapus Data Buku")
  print("5. Cari Data Buku")
  print("0. Keluar")
  print("------------------")
  menu = input("Pilih menu> ")

  #clear screen
  os.system("clear")

  if menu == "1":
    insert_data(db)
  elif menu == "2":
    show_data(db)
  elif menu == "3":
    update_data(db)
  elif menu == "4":
    delete_data(db)
  elif menu == "5":
    search_data(db)
  elif menu == "0":
    exit()
  else:
    print("Menu salah!")


if __name__ == "__main__":
  while(True):
    show_menu(db)