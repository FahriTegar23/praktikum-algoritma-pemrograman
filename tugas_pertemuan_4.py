# Latihan Modul 4

# Buatlah Program yang meminta inputan usia dari user memasukkan usia seseorang, lalu kategorisasi usia tersebut ke dalam kategori anak-anak, remaja, dewasa, dan lansia. Berikut adalah kriteria kategorisasi usia yang digunakan:

# - Anak-anak: 0-12 tahun
# - Remaja: 13-17 tahun
# - Dewasa: 18-59 tahun
# - Lansia: 60 tahun ke atas

usia = int(input("masukan usia anda :"))
if usia >= 0 and usia <= 12:
    print("usia anda termasuk kategori anak-anak")
elif usia >= 13 and usia <= 17:
    print("usia anda termasuk kategori remaja")
elif usia >= 18 and usia <= 59:
    print("usia anda termasuk kategori dewasa")
else:
    print("usia anda termasuk kategori lansia")
