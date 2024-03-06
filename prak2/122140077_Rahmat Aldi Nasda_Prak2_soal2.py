# Rahmat Aldi Nasda
# 122140077
# RB

def info_device(func):
    def decorator(*args, **kwargs):
        print("Berikut merupakan set-up device yang saya punya: ")
        return func(*args, **kwargs)
    return decorator

class device:
    def __init__(self, handphone, laptop):
        self.handphone = handphone
        self.laptop = laptop

    @info_device
    
    def detail_device(self):
        print (f"Saya memiliki {self.handphone} handphone dan {self.laptop} laptop.")

    def __del__(self):
        print (f"Data device {self.handphone} handphone dan {self.laptop} laptop yang saya miliki telah dihapus.")

handphone = int(input("Inputkan jumlah handphone yang anda miliki: "))
laptop = int(input("Inputkan jumlah laptop yang anda miliki: "))

my_device = device(handphone, laptop)
print (" ")
my_device.detail_device()
