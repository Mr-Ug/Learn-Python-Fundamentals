
# Operator

# Operator digunakan untuk melakukan operasi pada variabel dan nilai.

#======================================================================================================================#

# Operator Aritmatika

# Operator arimatika digunakan dengan nilai numerik untuk melakukan operasi matematika umum:
# Prioritas Operasi :
        # 1. Nilai yang berada dalam kurung ( )
        # 2. Eksponen / Perpangkatan **
        # 3. Perkalian, Pembagian, Modulus, Pembulatan Kebawah * / % //
        # 4. Penjumlahan, Pengurangan + -

print('Operator Arimatika---------------------------------------------------------------------------------------------')
#======================================================================================================================#

# Perkalian,
e = 5
c = 3
print(f'5 x 3 = {e * c}')

#======================================================================================================================#

# Perpangkatan / Eksponen,
c = 3
b = 2
print(f'3 x 3 x 3 = {c ** b}')

#======================================================================================================================#

# Pembagian,
d = 4
b = 2
print(f'4 / 2 = {d / b}')

#======================================================================================================================#

# Pembulatan ke bawah,
d = 4
b = 2
print(f'4 // 2 = {d // b}')

#======================================================================================================================#

# Modulus / sisa pembagian,
f = 6
d = 4
print(f'6 % 4 = {f % d}')

#======================================================================================================================#

# Penjumlahan,
e = 5
c = 3
print(f'5 + 3 = {e + c}')

#======================================================================================================================#

# Pengurangan,
e = 5
c = 3
print(f'5 - 3 = {e - c}')

#======================================================================================================================#

# Operator Penugasan

#======================================================================================================================#

# Operator Perbandingan (Assignment)

# Operator Assignment operasi yang dapat dilakukan dengan penyingkatan
print("Operator Assigment---------------------------------------------------------------------------------------------")

#======================================================================================================================#

# Perkalian,
e1 = 5
e1 *= 3
print(f'5 *= 3 sama artinya dengan {e1} = 5 x 3')

#======================================================================================================================#

# Perpangkatan / Eksponen,
c1 = 3
c1 **= 2
print(f'3 **= 2 sama artinya dengan {c1} = 3 x 3 x 3')

#======================================================================================================================#

# Pembagian,
d1 = 4
d1 /= 2
print(f'4 /= 2 sama artinya dengan {d1} = 4 / 2')

#======================================================================================================================#

# Pembulatan ke bawah,
f1 = 6
f1 //= 2
print(f'6 //= 2 sama artinya dengan {f1} = 6 // 2')

#======================================================================================================================#

# Modulus / sisa pembagian,
c1 = 3
c1 %= 6
print(f'3 %= 6 sama artinya dengan {c1} = 3 % 6')

#======================================================================================================================#

# Penjumlahan,
a1 = 1
a1 += 3
print(f'1 += 3 sama artinya dengan {a1} = 1 + 3')

#======================================================================================================================#

# Pengurangan,
e1 = 4
e1 -= 2
print(f'4 -= 2 sama artinya dengan {e1} = 4 - 2')

#======================================================================================================================#

# Operator Logika
# operator logika untuk melakukan operasi data boolean.
# terdapat 3 jenis operator logika di Python, yaitu AND, OR, dan NOT.

#======================================================================================================================#

# Operator AND pada python dapat dilakukan menggunakan function "and",
# Nilai kebenaran operator AND adalah benar ketika kedua operand bernilai benar.

print("Operator Logika---------------------------------------------------------------------------------------------")

#======================================================================================================================#

print("AND------------------------------------------------------------------------------------------------------------")

print(f'Jika BENAR (TRUE) DAN BENAR (TRUE) bertemu hasilnya pun akan BENAR / {True and True}')
print(f'Jika BENAR (TRUE) DAN SALAH (FALSE) bertemu hasilnya pun akan SALAH / {True and False}')
print(f'Jika SALAH (FALSE) DAN BENAR (TRUE) bertemu hasilnya pun akan SALAH / {False and True}')
print(f'Jika SALAH (FALSE) DAN SALAH (FALSE) bertemu hasilnya pun akan SALAH / {False and False}')

#======================================================================================================================#

print("OR-------------------------------------------------------------------------------------------------------------")

# Operator OR pada python dapat dilakukan menggunakan function "or",
# Operator OR mempunyai nilai kebenaran salah saat kedua operand bernilai salah.

print(f'Jika BENAR (TRUE) ATAU BENAR (TRUE) bertemu hasilnya pun akan BENAR / {True or True}')
print(f'Jika BENAR (TRUE) ATAU SALAH (FALSE) bertemu hasilnya pun akan BENAR / {True or False}')
print(f'Jika SALAH (FALSE) ATAU BENAR (TRUE) bertemu hasilnya pun akan BENAR / {False or True}')
print(f'Jika SALAH (FALSE) ATAU SALAH (FALSE) bertemu hasilnya pun akan SALAH / {False or False}')

#======================================================================================================================#

print("NOT------------------------------------------------------------------------------------------------------------")

# Operator NOT merupakan operator yang menghasilkan nilai kebalikan dari operand.
# Misalkan operand X bernilai True, maka NOT X akan bernilai False.

print(f'Kebalikan dari BENAR (TRUE) adalah SALAH / ({not(True)})')
print(f'Kebalikan dari SALAH (FALSE) adalah BENAR / ({not(False)})')

#======================================================================================================================#

# Operator Identity
# Operator identitas digunakan untuk membandingkan objek, bukan jika mereka sama,
# tetapi jika mereka sebenarnya adalah objek yang sama, dengan lokasi memori yang sama:

# is : Hanya menilai "objek dari lokasi memori" sama (TRUE) atau tidak (FALSE)
# id() untuk menampilkan nilai memori
# terdapat 2 jenis operator identitas di Python, yaitu IS dan IS NOT.

iS1 = 3
iS2 = 3

print(id(iS1))
print(id(iS2))
print(f'is = Jika nilai 1 dan nilai 2 berisi nilai yang sama maka hasilnya BENAR ({iS1 is iS2})')
print(f'is not = Jika nilai 1 dan nilai 2 berisi nilai yang sama maka hasilnya SALAH ({iS1 is not iS2})')

#======================================================================================================================#

# Operator Keanggotaan

#======================================================================================================================#

# Operator Bitwise

#======================================================================================================================#