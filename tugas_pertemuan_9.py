# Latihan

# 1. Diberikan list berikut :
print("Nomor 1.")
kendaraan = ["motor", "mobil", "sepeda", "bus"]
print(kendaraan)

# a. Tambahkan 'truk' di akhir list
print("a. Tambahkan 'truk' di akhir list")
kendaraan.append("truk")
print(kendaraan)

# b. Sisipkan becak pada index ke-1
print("b. Sisipkan becak pada index ke-1")
kendaraan.insert(1, "becak")
print(kendaraan)

# c. Hapus data yang berada dipaling belakang dari list tersebut
print("c. Hapus data yang berada dipaling belakang dari list tersebut")
kendaraan.pop()
print(kendaraan)

# d. Ubah elemen 'sepeda' menjadi 'skuter'
print("d. Ubah elemen 'sepeda' menjadi 'skuter'")
kendaraan[3] = "skuter"
print(kendaraan)

# e. tampilkan informasi jumlah total data di dalam list tersebut
print("e. tampilkan informasi jumlah total data di dalam list tersebut")
jumlah_total = len(kendaraan)
print(jumlah_total)
print()

# 2. Diberikan list berikut :
print("Nomor 2.")
angka = [75,80,90,75,85,100,65]
print(angka)

# a. Cari tahu di indeks ke berapa skor 100 berada
print("a. Cari tahu di indeks ke berapa skor 100 berada")
index = angka.index(100)
print(f"Indeks 100 ada di indeks ke: {index}")

# b. Hitung berapa banyak siswa yang mendapatkan skor 75
print("b. Hitung berapa banyak siswa yang mendapatkan skor 75")
skor = angka.count(75)
print(f"Banyaknya siswa dengan skor 75 ada: {skor}")

# c. Urutkan list skor_ujian tersebut dari nilai terkecil hingga terbesar
print("c. Urutkan list skor_ujian tersebut dari nilai terkecil hingga terbesar")
angka.sort()
print(angka)

# d. Balikkan urutan list yang sudah diurutkan
print("d. Balikkan urutan list yang sudah diurutkan")
angka.reverse()
print(angka)
print()

# Nomor 3.
print("Nomor 3.")
menu_utama = ["Nasi Goreng", "Mie Ayam"]
menu_tambahan = ["Kerupuk", "Es Teh"]
print(menu_utama)
print(menu_tambahan)

gabungan = [menu_utama, menu_tambahan]
print(f"Gabungan dari menu tersebut adalah = {gabungan}")

# Nomor 4.
print("Nomor 4.")
barang_0 = ["Buku", 5000]
barang_1 = ["Pensil", 2000]
barang_2 = ["Peggaris", 3000]
data_barang = [barang_0, barang_1, barang_2]
print(data_barang)

# a. Tampilkan harga "Pensil"
print(" a. Tampilkan harga 'Pensil'")
print(f"Harga Pensil: Rp.{barang_1[1]:,.0f}")

# b. Gunakan Format Perulangan satu per satu
print("b. Gunakan Format Perulangan satu per satu")
for barang in data_barang:
    print(f"Nama: {barang[0]}")
    print(f"Harga: Rp.{barang[1]:,.0f}")
    print()
    

