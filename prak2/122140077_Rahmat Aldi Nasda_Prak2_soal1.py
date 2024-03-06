# Rahmat Aldi Nasda
# 122140077
# RB

class Mahasiswa:
    def __init__(self, nim, nama, angkatan, isMahasiswa = True):
        self.__nim = nim
        self.__nama = nama
        self.angkatan = angkatan
        self.isMahasiswa = isMahasiswa

    def set_nim(self, nim):
        self.__nim = nim

    def get_nim(self):
        return self.__nim

    def set_nama(self, nama):
        self.__nama = nama

    def get_nama(self):
        return self.__nama

    def info_mahasiswa(self):
        return f"\nInformasi Mahasiswa \nNIM: {self.__nim} \nNama Mahasiswa: {self.__nama} \nAngkatan: {self.angkatan} \nStatus: {'Mahasiswa aktif' if self.isMahasiswa else 'Bukan mahasiswa aktif'}"

    def status_mahasiswa(self):
        return self.isMahasiswa

    def tahun_angkatan(self):
        return self.angkatan

nim = int(input("Masukkan NIM mahasiswa ke-1: "))
nama =  str(input("Masukkan nama mahasiswa ke-1: "))
angkatan = int(input("Masukkan angkatan mahasiswa ke-1: "))

data_mahasiswa = Mahasiswa (nim, nama, angkatan, True)
print (data_mahasiswa.info_mahasiswa())

print (" ")

nim2 = int(input("Masukkan NIM mahasiswa ke-2: "))
nama2 =  str(input("Masukkan nama mahasiswa ke-2: "))
angkatan2 = int(input("Masukkan angkatan mahasiswa ke-2: "))

data_mahasiswa2 = Mahasiswa (nim2, nama2, angkatan2)

status_mahasiswa = str(input("Apakah data orang yang telah disebutkan merupakan mahasiswa aktif? Ketik YA jika merupakan mahasiswa aktif: "))

if (status_mahasiswa == "YA"):
    print (data_mahasiswa2.info_mahasiswa())
else:
    data_mahasiswa2.isMahasiswa = False
    print (data_mahasiswa2.info_mahasiswa())
    
    
    