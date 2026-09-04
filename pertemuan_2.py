# Progam 2.3
# a = 10, a adalah variable dengan nilai 10

# tipe data: Angka satuan yang gak ada komanya (integer)
data_integer = 1
print ("data : ", data_integer)
print ("- bertipe ", type(data_integer))

# tipe data: Angka dengan koma (float)
data_float = 1.5
print ("data : ", data_float)
print ("- bertipe ", type(data_float))

# tipe data: Kumpulan karakter (string)
data_string = "ucup"
print ("data : ", data_string)
print ("- bertipe ", type(data_string))

# tipe data: biner true/false (boolean)
data_bool = True
print ("data : ", data_bool)
print ("- bertipe ", type(data_bool))

## tipe data khusus

# bilangan kompleks
data_complex = complex(5,6)
print ("data : ", data_complex)
print ("- bertipe ", type(data_complex))

# tipe data dari bahasa C
from ctypes import c_double
data_c_double = c_double(10.5)
print ("data : ", data_c_double)
print ("- bertipe ", type(data_c_double))

# Progam 2.4
# merubah tipe data ke tipe data lain
# tipe data = int, float, str, bool

# INTEGER ke Tipe data lain
data_int = 9 

data_float = float(data_int)
data_str = str(data_int)
data_bool = bool(data_int) #akan false jika nilai integer = 0

print ("data = ", data_float, ", type = ", type(data_float))
print ("data = ", data_str, ", type = ", type(data_str))
print ("data = ", data_bool, ", type = ", type(data_bool))

# FLOAT ke Tipe data lain
data_float = 9.2
data_int = int(data_float) 
data_str = str(data_float)
data_bool = bool(data_float) #akan false jika nilai float = 0

print ("data = ", data_int, ", type = ", type(data_int))
print ("data = ", data_str, ", type = ", type(data_str))
print ("data = ", data_bool, ", type = ", type(data_bool))

# STRING ke Tipe data lain
data_str = "10"
data_int = int(data_str)
data_float = float(data_str)
data_bool = bool(data_str) 

print ("data = ", data_int, ", type = ", type(data_int))
print ("data = ", data_float, ", type = ", type(data_float))
print ("data = ", data_bool, ", type = ", type(data_bool))

# Program 2.5

# data yang dimasukan pasti string 
data_input = input("Masukan data: ")
print ("data ", data_input,", type = ", type(data_input))

#jika kita ingin mengambil tipe data integer
angka = int(input("Masukan angka: "))
print ("data ", angka,", type = ", type(angka))

