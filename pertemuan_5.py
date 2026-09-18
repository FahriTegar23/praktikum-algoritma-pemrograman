# Program 5.1 For 
# Perulangan (loop)

angka = 1
print(angka)
angka = angka + 1
print(angka)
angka = angka + 1
print(angka)

# for kondisi:
#     aksi 

# Dengan list 
angka2 = [0,1,2,3,4] # ini adalah list
print(angka2)

for i in angka2:
    print(f"i sekarang {i}")
print("akhiri dari program\n")

angka4 = range(1,10)
for i in angka4:
       print(f"i sekarang {i}")
       print("saya keren")
print("akhiri dari program\n")

# Menggunakan string 
data_str = "saya Tegar"

for huruf in data_str:
      print(huruf)
print("akhiri dari program\n")

# Progam 5.2
# while loop
 
# while kondisi:
#      aksi ini
#      aksi itu

print("===Contoh 1===\n")

angka = 10
while angka > 5:
      print("ipin lari ipin!!!")
      break

print("===Contoh 2===\n")

angka = 0
print(f"angka sekarang {angka}")

while angka < 5 :
      angka += 1
      angka = angka + 1
      print(f"angka sekarang {angka}")
      print("ipin lari ipin")
print("program berakhir, ipin sudah jauh")

# Program 5.3
# Continue, pass, break
# pass -> berfungsi sebagai dummy, tidak akan dieksekusi

angka = 0

while angka < 5:
      angka = angka + 1

      if (angka == 3 ):
            pass
      print(angka)

# Continue 
angka = 0
print(f"angka sekarang {angka}")

while angka < 5:
      angka = angka + 1
      print(f"angka sekarang {angka}") # aksi 1

      if(angka == 3):
            print("nice")
            continue # akan membuat loop meloncat ke step selanjutnya
      print("wahssup") # aksi 2

print("Finish")

# Program 5.4 
# Break

angka = 0 
print(f"angka sekarang {angka}")

while angka < 5:
      angka = angka + 1
      print(f"angka sekarang {angka}") # aksi 1

      if(angka == 3):
            print("nice")
            break 
print("whassup") # aksi 2

print("cukup sampai disini saja")

# Program 5.5
# Latihan membuat segitiga

# 1. Menggunakan For
sisi = 4
count = 1

for i in range(sisi):
      print("*" * count)
      count += 1

# Menggunakan while 

sisi = 4
count = 1

while True:
      print("*" * count)
      count += 1

      if count > sisi:
            break
