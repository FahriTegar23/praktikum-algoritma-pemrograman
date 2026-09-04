# Tugas Praktikum Pertemuan 2

# 1. Tugas 1 - Deklarasi variabel dan tipe data
nama = "Fahri Tegar Maulana"
umur = 18
berat = 43.6

print ("Nama : ", nama, ", bertipe data : ", type(nama))
print ("Umur : ", umur, ", bertipe data : ", type(umur))
print ("Berat : ", berat, ", bertipe data : ", type(berat))

# 2. Tugas 2 - Konversi tipe data
angka_string = "123"
angka_float = 45.67
angka_integer = 89

# 1. Konversi angka_string menjadi integer
angka_string = int(angka_string)
print ("Hasil 1 = ", angka_string, ", type = ", type(angka_string))

# 2. Konversi angka_float menjadi integer
angka_float = int(angka_float)
print ("Hasil 2 = ", angka_float, ", type = ", type(angka_float))

# 3. Konversi angka_integer menjadi float
angka_integer = float(angka_integer)
print ("Hasil 3 = ", angka_integer, ", type = ", type(angka_integer))

# 4. Konversi angka_integer menjadi string
angka_integer = 89
angka_integer = str(angka_integer)
print ("Hasil 4 = ", angka_integer, ", type = ", type(angka_integer))

# 3. Tugas 3 - Meminta Input Data
usia = int(input("Masukkan umur Anda : "))
tinggi = float(input("Masukkan tinggi badan Anda : "))
nama = input("Masukkan nama Anda : ")

print ("Nama Anda : ", nama, ", bertipe data : ", type(nama))
print ("Umur Anda : ", usia, ", bertipe data : ", type(usia))   
print ("Tinggi badan Anda : ", tinggi, ", bertipe data : ", type(tinggi))


