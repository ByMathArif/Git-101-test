# Veri Dönüşümleri - Mert Mekatronik pythone - Ders 5

# """Bazı Gömülü Fonksiyonlar
#int()
#float()
#str
#str()
#len()


a = 5.42

print(type(int(a)))                     
                                        
b = int(6.89)
print(b)



#hatalı olma sebebi str olan ile int olanı toplamak istememiz
#cc = "200"
#print(cc +400 )

#çözüm veri dönüşümü ile "bir nevi çinliler ile çinliler zenciler ile zenciler  zenci ile cinli evlenmesi yasak gibi "

c = "300"
print(int(c)+20)


print("400 " * 4)
#aradaki fark sana int ile str ayrımını ve işleyişi hakkında bilgi vermeli. Ayrıca zaten veri dönüşümünü de kavratan bir örnek 
print(int("400")*4)

#yaptığın dönüşümün int ve str dahi olsa uyumu hakkında bir örenek. Dikkat!!!

# x = "1m"
# y = int(x)
# print(y)      #hata]]
# print(int(x)) #hata]]


sayi = 8798454654985612384854854548745646548
print(len(str(sayi)))



f = int(input("sayi1: "))
h = int(input("sayi2: "))

secenekler = int(input("1topla:\n2cıkar:\n3bol: \n4carp: "))
if secenekler == 1:
    print("sonuc:" + str(f+h))
elif secenekler == 2:
    print("sonuc:" + str(f-h)) #zenci çinli öğrneği önemi!!! "int int olarak alamadık ama str alarak hallettik böylece sonuc : ... yazdırabildik"
elif secenekler == 3:
    print("sonuc:" + str(f/h))
else:
    secenekler == 4
    print("sonuc:" + str(f*h))

"pull ile visual studio code'daki dosyayı güncellemek istiyoruz"




