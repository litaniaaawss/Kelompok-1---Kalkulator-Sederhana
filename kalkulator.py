# Kalkulator sederhana 

def penjumlahan (a, b):
    return a + b
def pengurangan (a, b):
    return a - b
def perkalian (a, b):
    return a * b 
def pembagian (a, b):
    if b != 0:
        return a / b
    else :
        return ("pembagian tidak bisa menggunakan 0")

    print ("----Kalkulator Kelompok 1---")

    while True:
        print ("Pilih operasi :")
        print ("1. Penjumlahan")
        print ("2. Pengurangan")
        print ("3. Perkalian")
        print ("4. Pembagian")
        print ("5. Keluar")

        pilihan = input("masukan pilihan 1/2/3/4/5")

        if pilihan == '5':
            print("anda keluar dari kalkulator kelompok 1")
            break

        angka1 = float(input("masukan angka pertama :"))
        angka2 = float(input("masukan angka kedua :"))

        if pilihan == '1':
            hasil = penjumlahan(angka1, angka2)
            print ("hasil penjumlahan =", hasil)
        elif pilihan == '2':
            hasil = pengurangan(angka1, angka2)
            print ("hasil pengurangan =", hasil)
        elif pilihan == '3':
            hasil = perkalian(angka1, angka2)
            print ("hasil perkalian =", hasil)
        elif pilihan == '4':
            hasil = pembagian(angka1, angka2)
            print ("hasil pembagian =", hasil)
        else :
           print("Pilihan tidak valid. Silakan masukkan pilihan yang sesuai.")






