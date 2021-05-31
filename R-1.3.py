print('1. menentukan Nilai maksimum dua bilangan')
print('2. menentukan Nilai min dua bilangan')
pilih = int(input("masukan pilihan: "))
if pilih==1:
 a = int(input("masukan bilangan pertama: "))
 b = int(input("masukan bilangan kedua: "))
 if a > b:
        maks = a
 else:
        maks = b
 print('Nilai Terbesar adalah %d' % maks)
else:
 a = int(input("masukan bilangan pertama: "))
 b = int(input("masukan bilangan kedua: "))
 if a < b:
        min = a
 else:
        min = b
 print('Nilai Terkecil adalah %d' % min)
