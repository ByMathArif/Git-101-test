# İnput Gömülü Fonksiyonu --> görevi cmd bölümünden dinamik bir deger almaktır.
#  ama bunu hep string olarak algıladıgı  icin bazı yerlerde int(...)  seklinde ifadeler yapmalıyız.

from cmath import pi


def Kare_Al (a):
    return a**2
sayi =int(input("Bir Sayı Giriniz: ")) 
print("Sayınızın Karesi:"+ str(Kare_Al(sayi))) 


print("""**** HESAP MAKİNESİ ****""")
sayi1 = float(input("birinci sayıyı giriniz: "))
sayi2 = float(input("ikinci sayıyı giriniz: ")) 

print("""
Toplam : {}
Fark :{}
Bölüm :{}
Carpım :{}""".format(sayi1+sayi2,sayi1-sayi2,sayi1/sayi2,sayi1*sayi2))

















