
# Dictionary Veri Tipleri 
# liste ,tuple,float blooan...--> gibi bir builtins (sınıf)
# sozluk[anahtar] = deger

sozluk1 = {}  #boş sozluk
sozluk2 = dict()
print(type(sozluk1))
print(type(sozluk2))  #type bir gömülü fonksiyondur. aldığı argüman değerinin obje tipini gösterir.
Arac_model = {
    "Toyota":2000,
    "Wolsvagen":2022,
    "Peugeot":2020,
    "Fiat":2016
    }
print(Arac_model)
print(Arac_model["Fiat"])
print(Arac_model["Wolsvagen"])

Arac_model["Audi"] = 2002 ,"hatasız kazasız"
print(Arac_model)
Sahibinden_Arac_model = Arac_model.copy()
print(Sahibinden_Arac_model)
Sahibinden_Arac_model["Suzuki"] = 2017
print(Sahibinden_Arac_model)

Ekip = {
    "Uyeler":["Emin","Enes","Burak"],
    "Moderator":["Akif","Bugra","Mehmet"],
    "Yardımcı Baskan":["Kenan","Sinem","Gamze","Gökce"],
    "Baskan":["Fethi","Ethem","Nebi","Arif"]}
Ekip["Uyeler"].append("Tuba")
Ekip["Moderator"].remove("Bugra")
Ekip["Yardımcı Baskan"].pop(3) #pop burada List yapısındaki indexleri 0,1,2,3 gibi görüp siliyor .po() ---> en sondaki nesneyi siliyor demek
print(Ekip)

#Ekip.clear() -->dict temizler
#print(Ekip) 

#EkipKoyaAl = Ekip.copy() -->dict kopya alır 
#print(EkipKoyaAl)

#Ekip.pop("Moderator") -->.pop()"parantez icine yazılanı siler"
#print(Ekip)

print(type(Ekip.values()))

Tum_Ekip = Ekip.values()
for Ekipteki_Kişiler in Tum_Ekip:
    print(Ekipteki_Kişiler)

Tum_Ekip = Ekip.values()
for Ekipteki_Kişiler in Tum_Ekip:
    for Tek_tek_kisiler in Ekipteki_Kişiler:
        print(Tek_tek_kisiler)
 

Tum_Ekip = Ekip.keys()
for Ekipteki_Kişiler in Tum_Ekip:
        print(Ekipteki_Kişiler)



Tum_Ekip = Ekip.items()
for yetki,isim in Tum_Ekip:
    print(yetki+":Bilisim Vadisi Görevlisi",isim)