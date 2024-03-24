# Rahmat Aldi Nasda
# 122140077
# RB

class Hewan:
    def __init__ (self, nama, jenis_kelamin):
        self.nama = nama
        self.jenis_kelamin =  jenis_kelamin
        
    def bersuara():
        pass
    
    def makan (self):
        print (f"{self.__class__.__name__} {self.nama} sedang makan: tulang")

    def minum (self):
        pass


class Kucing (Hewan):
    def __init__ (self, nama, jenis_kelamin):
        super().__init__ (nama, jenis_kelamin)
    
    def bersuara (self):
        print (f"Kucing {self.nama} bersuara: Meong!")


class Anjing (Hewan):
    def __init__ (self, nama, jenis_kelamin):
        super().__init__ (nama, jenis_kelamin)
    
    def bersuara (self):
        print (f"Anjing {self.nama} bersuara: Guk Guk!")

hewan1 = Kucing ("Kiki", "Betina")
hewan2 = Anjing ("Ichi", "Jantan")

print (hewan1.nama) 
print (hewan2.nama)

hewan1.bersuara() 
hewan1.makan() 
hewan2.bersuara() 
hewan2.makan()   
