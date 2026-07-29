#mengimport modul random
import random

print ("==== NUMBER GUESSING GAME ====")

#komputer memilih angka acak
angka_rahasia = random.randint(1, 100)

percobaan = 0
#pengulangan sampai tebakan benar
while True:
    tebakan = int(input("masukan tebakan (1-100): "))

    #validasi input
    if tebakan < 1 or tebakan > 100:
        print ("masukan angka antara 1 sampai 100")
        continue

    #menambah jumlah percobaan tebakan
    percobaan += 1

    #mengecek tebakan
    if tebakan < angka_rahasia:
        print ("tebakan salah. \nAngka terlalu kecil.")
    elif tebakan > angka_rahasia:
        print ("tebakan salah. \nAngka terlalu besar.")
    else:
        print ("selamat! tebakan benar ")
        print (f"kamu berhasil dalam {percobaan} percobaan. ")
        break
    
