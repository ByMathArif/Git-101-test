#print fonksiyonları derinlikleri file e flush parametresi ne demek
from email.generator import DecodedGenerator
from math import degrees
import numbers


dosya = open("Sanat Hikayesi2.txt","w")
print("Kardelen",file=dosya)


herhangi_bir_sey = open("Hedeflerim ve BEN.py","w")
print("BIR GUN HER SEY COK GUZEL OLACAK",file=herhangi_bir_sey)

dosya = open("deneme.txt", "w") # deneme.txt adlı dosya yoksa oluşturup, var ise açıp yazı yazarız.
print("-Merhabalar.", file = dosya, flush = True) # print ile dosya adlı değişkenin deneme.txt adlı dosyada "-Merhabalar" yazarız.

#yıldızlı parametreler 
# programın akışında fonksiyon birden fazla parametre alıyorsa  ve bu parametrelerin sayısı kesin olarak tahmin edilemiyorsa ,değişkenlik gösterebiliyorsa 
#yıldızlı parametre kullanırız.
# yıldızlı parametrelerin kullanunım şeklilleri :
#1) ampeck yapmada -> dosya açmakta  misal : "print"


metin = "AEG"

print(*metin,sep=".")
print(*metin,sep="  ") # * olmazsa asla sep eylemi sağlanmayacaktır.

#Ampeck işlemi fonksiyonlarda birden fazla parametreleri gönderirken kullanılmaktadır.
#ÖRNEK


#n=str(input("Kaça kadar toplamak istiyorsunuz?: "))   fonksiyonları öğrenince tekrar bak 
#def topla1den_basla_N_e_kadar(*numbers):
#    topla = 0
#    for number in numbers:
#        topla += number
#    return topla
#numbers= [x for x in range(1,str(n))]
#print(topla1den_basla_N_e_kadar(*numbers))



def topla1den_basla_N_e_kadar(*numbers):
    topla = 0
    for number in numbers:
        topla += number
    return topla
numbers= [x for x in range(1,11)]
print(topla1den_basla_N_e_kadar(*numbers))


"arif esat"
" Çanakkale 18 Mart üniversitesi Bilgisayar Mühendisliği okuyorum"



