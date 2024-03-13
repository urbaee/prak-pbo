# Rahmat Aldi Nasda
# 122140077
# RB

class Dagangan:
    jumlah_barang = 0
    list_barang = []

    def __init__(self, nama, stok, harga):
        self.__nama = nama
        self.__stok = stok
        self.__harga = harga
        Dagangan.jumlah_barang += 1
        Dagangan.list_barang.append ((nama, stok, harga))

    def lihat_barang():
        print (f"Jumlah barang dagangan pada toko: {Dagangan.jumlah_barang} buah")
        for i, barang in enumerate (Dagangan.list_barang, start=1):
            nama, stok, harga = barang
            print (f"{i}. {nama} seharga Rp {harga} (stok: {stok})")
        print ()    

    def __del__ (self):
        Dagangan.jumlah_barang -= 1
        for i, barang in enumerate (Dagangan.list_barang):
            if barang[0] == self.__nama:
                del Dagangan.list_barang[i]
                print (f"{self.__nama} dihapus dari toko! \n")
                break

Dagangan1 = Dagangan("Galon Aqua 19L", 32, 17000)
Dagangan2 = Dagangan("Gas LPG 5 kg", 22, 88000)
Dagangan3 = Dagangan("Beras Ramos 5 kg", 13, 68000)

Dagangan.lihat_barang()

del Dagangan1

Dagangan.lihat_barang()
