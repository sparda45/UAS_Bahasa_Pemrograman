def genap(x): #contoh fungsi genap
     if x == 0:
         return True
     else:
         return ganjil(x-1)
def ganjil(x):
     return not genap(x)

print(ganjil(19))
print(genap(25)) #recursive secara tidak langsung dimana  Fungsi pertama memanggil fungsi kedua dan seterusnya