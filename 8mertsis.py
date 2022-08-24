# Liste Veri Tipleri  Python'da her şey bir obje - objeler sınıflardan türetiliyor
# builtin = yani gömülü sınıflar,gönülü fonksiyonlar sayesinde kodlama yapıyoruz.
# örn= ev alınca su , doğalgaz elektrik tesisatı ısıs yalıtım içinde hazırdır. Python içinde hazır gibi...
  
a = list("Sezgin")  #ctrl+mouse gömülü yapıları çıkarmak
b = []  # sıralı ,birbirine benzer,çok uzun verileri, birbiri ile ilişkin verileri 

print(type(a)) #type ile class öğrenmek :) ti 
print(type(b))  

ogrenciler = ["Melike","Merve","Hilal","Gokce","Sena","Nisa","İrem","Berre",1,7,6] # index no ile herbir nesne bir tanesini ifade eder misal 0. index "Melike" demek broo

print(ogrenciler[3],end = "  EN BAŞARILISI ")   

print(len(ogrenciler))    
ogrenciler.remove("Merve")     #misal Merve disipline gitti o yüzden listeden çıkarmak için bir komut
print(ogrenciler,sep="Disiplinsiz ÖĞrenciler")
print(len(ogrenciler))

# metin_belgesi = "Saygı Sonradan Alın Teri İle  Kazanılır"
# print(metin_belgesi[0:5],[8:10])       SORULDU [ ]


# farklı bir örnek : strin ile önce listele sonra liste ekle çıkar en son tekrar strig yapmak adlı çalışma :)
Belirtili_Nesene = "Arif'in Mac Pro M1'i Speys Grey 512 Gb..."
Belirtili_Nesene= list(Belirtili_Nesene)
print(Belirtili_Nesene)
Belirtili_Nesene[0:4] = "Arif Esat"
print("".join(Belirtili_Nesene)) #son aşama stringe dönüştürme...

ogrenciler2 = ["Muhammed","Mustafa ", "Ömer","Ali"]
ogrenciler = ogrenciler + ogrenciler2

print(ogrenciler)

basamaklar = [1,2,5]
#basamaklar = basamaklar * 99 

basamaklar.append("türev alma kurallrı"*2)   #append ile listeye eleman eklemek için kkullanıyoruz
print(basamaklar,sep="SÜÜÜÜÜÜÜÜÜÜÜÜÜÜ")


cikarilan = basamaklar.pop(3)
print(basamaklar)
print(cikarilan)

print("Arif Esat Güngör")

"Push Ogreniyoruz"

"Ethem abi iyi akşamlar Nasılsın ?"
