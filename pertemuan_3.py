# Progam 3.1 Menampilkan output dari operasi aritmatika sederhana
# operasi aritmatika 

a = 10
b = 3

# operasi tambah +
hasil = a + b
print(a,'+',b,'=',hasil)

# operasi kurang -
hasil = a - b
print(a,'-',b,'=',hasil)

# operasi perkalian *
hasil = a * b
print(a,'*',b,'=',hasil)

# operasi pembagian /
hasil = a / b
print(a,'/',b,'=',hasil)

#operasi eksponen (pangkat) **
hasil = a ** b
print(a,'**',b,'=',hasil)

# operasi modulus %
hasil = a % b
print(a,'%',b,'=',hasil)

# operasi floor division //
hasil = a // b
print(a,'//',b,'=',hasil)

# Progam 3.2 Konversi celcius ke satuan lain
# latihan konversi satuan temperature

# progam konversi celcius ke satuan lain

print("\nPROGRAM KONVERSI TEMPERATURE\n")
celcius = float(input("Masukkan suhu dalam celcius: "))
print("Suhu adalah", celcius, "Celcius")

# Reamur
reamur = (4/5) * celcius
print("Suhu dalam reamur adalah", reamur, "Reamur")

# Fahrenheit
fahrenheit = ((9/5) * celcius) + 32
print("Suhu dalam fahrenheit adalah", fahrenheit, "Fahrenheit")

# Kelvin
kelvin = celcius + 273
print("Suhu dalam kelvin adalah", kelvin, "Kelvin")

# Progam 3.3 Operasi komperasi
# operasi komperasi

# setiap hasil dari operasi komperasi adalah boolean 

# >,<,>=,<=,==,!=, is, is not

a = 4 
b = 2

# lebih besar dari >
print("=============== lebih besar dari (>)")
hasil = a > 3
print (a,'>',b,'=',hasil)
hasil = b > 3
print (b,'>',3,'=',hasil)
hasil = b > 2
print (b,'>',2,'=',hasil)

# Kurang dari <
print("=============== kurang dari (<)")
hasil = a < 3
print (a,'<',b,'=',hasil)
hasil = b < 3
print (b,'<',3,'=',hasil)
hasil = b < 2
print (b,'<',2,'=',hasil)

# lebih dari sama dengan >=
print("=============== lebih dari sama dengan (>=)")
hasil = a >= 3
print (a,'>=',b,'=',hasil)
hasil = b >= 3
print (b,'>=',3,'=',hasil)
hasil = b >= 2
print (b,'>=',2,'=',hasil)

# kurang dari sama dengan <=
print("=============== kurang dari sama dengan (<=)")
hasil = a <= 3
print (a,'<=',b,'=',hasil)
hasil = b <= 3
print (b,'<=',3,'=',hasil)
hasil = b <= 2
print (b,'<=',2,'=',hasil)

# sama dengan (==)
print("=============== sama dengan (==)")
hasil = a == 4
print (a,'==',4,'=',hasil)
hasil = b == 4
print (b,'==',4,'=',hasil)

# tidak sama dengan (!=)
print("=============== tidak sama dengan (!=)")
hasil = a != 4
print (a,'!=',4,'=',hasil)
hasil = b != 4
print (b,'!=',4,'=',hasil)

#  'is'sebagai komparasi object identity (bukan literal)
x = 5 # ini adalah assigment membuat object
y = 5 
hasil = x is y
print(x,'is',y,'=',hasil)

# 'is not' sebagai komperasi object identity (bukan literal)
x = 5 # ini adalah assigment membuat object
y = 6 
hasil = x is not y
print(x,'is not',y,'=',hasil)
