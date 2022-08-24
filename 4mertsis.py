#Python Ders 4 -Mert Mekatronik - String veri tipi ve Özellikleri
 
yazi1 = " Softwer Engineer Gebze Teknik Üniversitesi Arif Esat GÜNGÖR feat by Bişim Vadisi "

def cokluYazdir(sayi,gelenYazi):
    for i in range(sayi):
        print(gelenYazi)      
cokluYazdir(10,yazi1)



yazi = """
<html>
<head></head>
<body><p>Selam</p></body
</html>



"""
#yazi.replace("p","b")
#print(yazi)

#SOR!!!!!!!!!!
#yeniYazi = []
#for harf in yazi :
    #if harf  == "p":
        #yeniYazi.append("b")
    #else :
        #yeniYazi.append(harf)
#print("".join(yeniYazi))


print(yazi1[1:17])

instagram_Takipcileri = "arda:100,luna:200,baha:55,can:90"
print(instagram_Takipcileri.find(""))
#print(instagram_Takipcileri)

#stringleri kesmek ya da istenilen aralık ile yazmak 
print(instagram_Takipcileri[5:24:1])
print(instagram_Takipcileri[::-1])
print(instagram_Takipcileri[:6])
print(instagram_Takipcileri[-10:])

print(len(instagram_Takipcileri))


ad = "Muhammed "
soyad = " Mustafa"
print(len(ad))
toplam = ad + soyad
print(toplam)

ad1 = "Hz"
soyad1 ="Ömer"
print(len(ad))
toplam = ad1 +" "+ soyad1
print(toplam)


print(ad*9)


