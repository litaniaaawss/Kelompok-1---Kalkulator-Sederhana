# Kelompok 1
# Vikenza Slat 250211060014
# Litania Supit 250211060018
# Syaloom Keintjem 250211060027
# Kristania Manorek 250211060025

#---Kalkulator Sederhana---

def penjumlahan(a, b):
    return a + b

def pengurangan(a, b):
    return a - b

def perkalian(a, b):
    return a * b

def pembagian(a, b):
    if b != 0:
        return a / b
    else:
        return "pembagian tidak bisa menggunakan 0"

print("---Kalkulator Sederhana---")
print("--------------------------")

while True:
    print("Pilih operasi:")
    print("1. Penjumlahan")
    print("2. Pengurangan")
    print("3. Perkalian")
    print("4. Pembagian")
    print("5. Keluar")

    pilihan = input("Masukkan pilihan 1/2/3/4/5: ")

if pilihan == '5':
    print("anda keluar dari kalkulator")
    break

angka1 = float(input("Masukkan angka pertama: "))
angka2 = float(input("Masukkan angka kedua: "))

if pilihan == '1'
    hasil = penjumlahan(angka1, angka2)
    print("hasil penjumlahan:", hasil)
elif pilihan == '2':
     hasil = pengurangan(angka1, angka2)
     print("Hasil pengurangan:", hasil)
elif pilihan == '3':
     hasil = perkalian(angka1, angka2)
     print("Hasil perkalian:", hasil)
elif pilihan == '4':
     hasil = pembagian(angka1, angka2)
     print("Hasil pembagian:", hasil)
else:
     print("Pilihan tidak valid. Silahkan masukkan pilihan yang sesuai.")
