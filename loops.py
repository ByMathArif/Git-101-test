from ast import Break
from multiprocessing.pool import ApplyResult
from nntplib import ArticleInfo


sehirler = ["Gebze", "İstanbul","İzmir"]
for sehir in sehirler :
    print(sehir)


# for sayi2 in range(1,10,2):
#     print(sayi2)

# for sayi1 in range(0,10,2):
#     print(sayi1)

elma = ("red apple")
print(elma)

sayac = 5
while sayac <= 15 :
    print(sayac)
    sayac = sayac +5

isim = input("Adınız:")
print("isim:"+ isim)

sayı = int(input("Sayınız:"))
print("sayı:"+str(sayı))

TC_Kimlik = int(input(" T.C. Kimlik:"))
print("TC NO:"+str(TC_Kimlik))

Number = int(input("Hangi Sayının Faktöryalini Hesaplamak İstersiniz? :"))
