# Rahmat Aldi Nasda
# 122140077
# RB

phi = 3.14

def lingkaran (r):
    if r < 0:
        print ("Tidak boleh menginput bilangan negatif atau dibawah nol!")

    keliling = 2 * phi * r
    luas = phi * r * r

    print ("Keliling dari lingkaran adalah: ", keliling)     
    print ("Luas dari lingkaran adalah: ", luas)

r = float(input("Masukkan nilai jari-jari lingkaran: "))

hasil = lingkaran (r)

if hasil is not None:
    print (hasil)