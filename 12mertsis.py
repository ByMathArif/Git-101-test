#Siz kodlayın :)






V = float(input("Gerilim Degerini Girinzi: "))
R = float(input("Direnç Degerini Giriniz:"))
while True:
    if R == 0:
        R = float(input("Direnç Degeri Sıfır Olamaz!! TEKRAR DEGER GİRİN:"))
    else:
        break
I = V/R
print("Akım Degeriniz:"+ str(I))
