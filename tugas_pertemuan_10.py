# LATIHAN

# 1. Tuple 
# a. Buatlah sebuah Tuple bernama mahasiswa yang berisi 3 data diri Anda: ("Nama","NIM","Prodi")
print("Nomor 1. Tuple")
print("a. Buatlah sebuah Tuple bernama mahasiswa yang berisi 3 data diri Anda: (Nama, NIM, Prodi)")
mahasiswa = ("Fahri Tegar Maulana", 2605060076, "Teknologi Informasi")
print(mahasiswa)
print()

# b. Tampilkan data NIM dan Prodi ke layar dengan cara mengakses indeksnya
print("b. Tampilkan data NIM dan Prodi ke layar dengan cara mengakses indeksnya")
print(f"Data NIM    : {mahasiswa[1]}")
print(f"Data Prodi  : {mahasiswa[2]}")
print()

# c. jalankan kode mahasiswa[2]
print("c. Jalankan kode mahasiswa[2]")
# mahasiswa[2] = "Teknologi Informasi"
print("TypeError: 'tuple' object does not support item assignment")
print("Tuple tidak dapat diubah (Immutable): Setelah tuple dibuat, anda tidak dapat \nmengubah, menambah, atau menghapus elemen di dalamnya")
print()

# d. Buatlah Set bernama nilai_angka berikut: 10, 4, 3, 2, 4, 10, 7, 5 
print("d. Buatlah Set bernama nilai_angka berikut: 10, 4, 3, 2, 4, 10, 7, 5 ")
nilai_angka = {10,4,3,2,4,10,7,5}
print(nilai_angka)
print("Angka 10 dan 4 hanya tercetak 1 dikarenakan SET memiliki Elemen Unik (Tidak ada duplikasi), \nSet secara otomatis menghapus nilai yang kembar.")
print()

# Nomor 2. Manipulasi Dictonary
print("Nomor 2. Manipulasi Dictonary")
# a. Buatlah sebuah dictonary bernama data_mahasiswa
print("a. Buatlah sebuah dictonary bernama data_mahasiswa")

data_mahasiswa = {
    "nim":"240101",
    "nama":"Budi Santoso",
    "prodi":"Teknologi Informasi"
}

print(data_mahasiswa)
print()

# b. Ubah nilai "prodi" menjadi "Sastra Mesin" sekaligus menambah key baru "angkatan" dengan nilai 2026
print("b. Ubah nilai 'prodi' menjadi 'Sastra Mesin' sekaligus menambah key baru 'angkatan' dengan nilai 2026") 
data_mahasiswa.update({"prodi":"Sastra Mesin"})
data_mahasiswa.update({"angkatan":"2026"})
print(data_mahasiswa)
print()

# c. Hapus data 'nim', lalu tampilkan hasil dictionary ke layar
print("c. Hapus data 'nim', lalu tampilkan hasil dictionary ke layar")
del data_mahasiswa["nim"]
print(data_mahasiswa)
print()

# Nomor 3. Perulangan pada Dictionary
print("Nomor 3. Perulangan pada Dictionary")
# a. Buatlah dictionary bernama keranjang dengan data harga buah
print("a. Buatlah dictionary bernama keranjang dengan data harga buah")

keranjang = {
    "apel":5000,
    "pisang":3000,
    "jeruk":7000,
    "anggur":15000
}
print(keranjang)
print()

# b. Gunakan Perulangan untuk menampilkan setiap barang
print("b. Gunakan Perulangan untuk menampilkan setiap barang")

subtotal = 0

for buah, harga in keranjang.items():
    print(f"Harga {buah}: Rp.{harga:,.0f}")
    subtotal += harga
print()

# c. Tampilkan Total Belanja
print("c. Tampilkan Total Belanja")
print(f"Total Belanja: Rp.{subtotal:,.0f}")
