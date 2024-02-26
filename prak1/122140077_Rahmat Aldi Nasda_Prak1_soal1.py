# Rahmat Aldi Nasda
# 122140077
# RB

def penghitungan (batas_bawah, batas_atas):
    if batas_bawah < 0 or batas_atas < 0:
        print ("Nilai batas atas dan bawah tidak boleh dibawah 0!")
    
    total = 0

    if batas_bawah >= 0 and batas_atas > 0:
        for angka in range (batas_bawah, batas_atas):
            if angka % 2 == 1:
                print (angka)   
                total += angka

        print ("Total: ", total)    
                
batas_bawah = int(input("Input nilai batas bawah: "))
batas_atas = int(input("Input nilai batas atas: "))

ganjil = penghitungan (batas_bawah, batas_atas)

if ganjil is not None:
    print (ganjil)
