# 1. Program menampilkan bilangan ganjil dan bilangan genap dari 1 sampai 50

# Bilangan Ganil
print("=== Bilangan Ganjil ===")

for i in range(1, 51) :
    if i % 2 != 0:
        print(i)

# Bilangan Genap
print ("=== Bilangan Genap ===")

for i in range(1,51) :
    if i % 2 == 0:
        print(i)

# 2. Program menampilkan bilangan prima 1 - 100
print("=== Bilangan Prima ===")

for angka in range(2, 101):
    prima = True

    for pembagi in range(2, angka):
        if angka % pembagi == 0:
            prima = False
            break

    if prima:
        print(angka) 
