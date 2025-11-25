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
