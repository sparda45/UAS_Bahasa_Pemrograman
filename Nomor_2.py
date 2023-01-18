try: # blok kode ini dieksekusi terlebih dahulu
    a = int(input('masukkan nilai a '))
    b = int(input('masukkan nilai b '))
    hasil = a/b
except Exception as err: # eksekusi pindah ke blok except bila pada blok try terjadi error
    print(err)
else:
    print('hasil a/b adalah',hasil)