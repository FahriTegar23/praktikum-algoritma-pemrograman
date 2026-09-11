# Program 4.1 Logical

# Operasi logika atau boolean 
# not, or, and xor

print('===NOT===') 
a = True
b = not a
print('data a =', a)
print('----------- NOT')
print('data b =', b)

# OR (jika salah satu true, maka hasilnya adalah true)
print('===OR===')
a = False
b = False 
c = a or b
print(a,'OR',b,'=',c)
a = False
b = True
c = a or b
print(a,'OR',b,'=',c)
a = True
b = False
c = a or b
print(a,'OR',b,'=',c)
a = True
b = True
c = a or b
print(a,'OR',b,'=',c)

# AND (jika dua buah bernilai true, maka hasilnya adalah true)
print('===AND===')
a = False
b = False
c = a and b
print(a,'AND',b,'=',c)
a = False
b = True
c = a and b
print(a,'AND',b,'=',c)
a = True
b = False
c = a and b
print(a,'AND',b,'=',c)
a = True
b = True
c = a and b
print(a,'AND',b,'=',c)

# XOR ( akan true jika salah satu true, sisanya false)
print('===XOR===')
a = False
b = False
c = a ^ b
print(a,'XOR',b,'=',c)
a = False
b = True
c = a ^ b
print(a,'XOR',b,'=',c)
a = True
b = False
c = a ^ b
print(a,'XOR',b,'=',c)
a = True
b = True
c = a ^ b
print(a,'XOR',b,'=',c)

# Program 4.2 Logika Komparasi

# latihan logika dan komparasi
# membuat gabungan area rentang dari angka 
# ++++++3--------10++++++

inputUser = float(input("masukan angka yang bernilai\nkurang dari 3 \natau \nlebih besar dari 10\n:"))

# ++++++3--------
# memeriksa angka kurang dari 3
isKurangDari = inputUser < 3
print("kurang dari 3 =", isKurangDari)

# --------10++++++
# memeriksa angka lebih dari 10
isLebihDari = inputUser > 10
print("lebih dari 10 =", isLebihDari)
isCorrect = isKurangDari or isLebihDari
print("angka yang anda masukan =", isCorrect)
print("================================")

# ------3++++++++10------
# kasus irisan 

inputUser = float(input("masukan angka yang bernilai\nlebih dari 3 \ndan \nkurang dari 10\n:"))

# ----3+++++++++
# lebih dari 3
isLebihDari3 = inputUser > 3
print("lebih dari 3 =", isLebihDari3)

# ++++++10------
# kurang dari 10
isKurangDari10 = inputUser < 10
print("kurang dari 10 =", isKurangDari10)

isCorrect = isLebihDari3 and isKurangDari10
print("angka yang anda masukan =", isCorrect)

# Program 4.3 IF and ELSE
# if dan else statement

# 1. if nya
# 2. kondisinya
# 3. aksi jika kondisi terpenuhi

nama = input("masukan nama anda :")

# 1. program if inline
if nama == "ucup": print("hello ucup")

# 2. program if indentation
if nama == "ucup":
    print("hello ucup")
    print("apa kabar?")

# 3. Else statement

nama = input("masukan nama anda :")

if nama == "paijo":
    print("hello paijo")
else:
    print("nama tidak dikenal")
print("akhir dari program")

# Program 4.4 Elif Statement

# ELIF = else statement

nama = input("masukan nama anda? :")

# if kondisi:
#     aksi true
# elif kondisi:
#     aksi true
# elif kondisi:
#     aksi true
# else:
#     aksi 

if nama == "tegar":
    print("hello tegar")
elif nama == "ucup":
    print("hello ucup")
elif nama == "paijo":
    print("hello paijo")
else:
    print("nama tidak dikenal")
print("akhir dari program")
