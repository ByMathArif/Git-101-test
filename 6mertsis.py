#(Fonksiyon ve Özellikleri") Mert Mekatronik pythone - Ders 6
# fonksiyonun görevi : kod tekrarını öneler ve farklı parametrelere göre farklı sonuçlarıdöndürüyor


from turtle import Turtle


sayi = 6
faktoriyel = -1
for i in range(1,sayi+1):   # 1'den sayının bir fazlasına kadar gidene kadar for ile döngüye aldık ve buna i değerini atadık. 
#  Bu i değeri sayının           1 2 3 4 5 6  "1" ->  her bir değer ile  sayıları tek tek sayıları dönüyor.1*1*2*3*4*5*6 gibi ...
    faktoriyel = (faktoriyel*i)


print(faktoriyel)



def FaktoryelBul(number):
    ffaktoriyel = 1
    for i in range(1 ,number + 1):
       ffaktoriyel = ffaktoriyel * i 
    return ffaktoriyel

print(FaktoryelBul(6))



def FaktoryelBul(number):
    ffaktoriyel = 1
    for i in range(1 ,number + 1):
       ffaktoriyel =  number* i 
    return ffaktoriyel

print(FaktoryelBul(6))
 

a = 1
b= "Arif Esat" # çinliler ve zenciler
print(a , b)

print("Arif\nEsat\nGUNGOR")
print("1.Tercihim Gebze Teknik Üniversitesi \n Bilgisayar Mühendisliği\nArif Esat GÜNGÖR") #"burada anlatmak istediğim şey { \n } ile alt satıra kaymayı anlatıyorum"
# { \n } gibi { \t } de var bu da TAB boşluğu bırakmamızı sağlıyor.

a =  1 
b = "C.R7"
c = Turtle

# print(type(a,b,c)) burada type ile <class> öğrenirken şöyle düşünmeliyiz  sadece bir <class> yazabiliriz !!!

print(type(c))




print(a,b,c,sep = "SÜÜÜÜÜÜÜÜÜÜÜÜÜÜ") #sep= her class arasına yazar 

def islem(a,yapi=" +"):
    if yapi == "+":
        return a + a    
    else:
        return a * a
print(islem(5,yapi="+"))

#end parametresi print fonskiyyonunda değerler yazıldıktan sonra en son ne ekleneceğini verir.
k= "elma"
print(k,end="--")
print(k)
print(k)

print(*b) #*b LUNA-> L U N A 

ad = "arif esat"
soyad = "güngör"

print( "Merhaba Sayın {} {} Ziraat Mobile Hoş Geldiniz".format(ad,soyad))  # .format ve  {} ile aralara eklemek!
# Değişkenleri bir string sınıfına ait objede {} parametrelerine göndererek yazdırabilmek

print("Merahaba Sayın ",ad,soyad,"Mobil Bankanıza Hoş Geldiniz")

print("İyi Akşamlar Sayın %s %s E-Ticaret Sitemize Hoş Geldiniz" % (ad,soyad)) # .format ile olana benzer işlevi görüyor

"Bİr taş ile iki kuş vurdum :) "


