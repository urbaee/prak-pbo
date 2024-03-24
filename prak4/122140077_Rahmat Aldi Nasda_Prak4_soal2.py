# Rahmat Aldi Nasda
# 122140077
# RB

class Bentuk:
    def hitungLuas (self):
        pass

class Persegi (Bentuk):
    def __init__ (self, sisi):
        self.sisi = sisi
    
    def hitungLuas (self):
        return self.sisi * self.sisi

class Lingkaran (Bentuk):
    def __init__ (self, jari_jari):
        self.jari_jari = jari_jari
    
    def hitungLuas (self):
        return 3.14 * self.jari_jari * self.jari_jari

def printLuas (bentukbangunan):
    print (bentukbangunan.hitungLuas())

persegi = Persegi (5)
lingkaran = Lingkaran (3)

print ("Luas Persegi:", end= " ")
printLuas (persegi)

print ("Luas Lingkaran:", end= " ")
printLuas (lingkaran)
