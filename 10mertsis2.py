#Sabah Bakılıp Tekrar Gözden GEçirilecek:)

Ekip = {
    "Uyeler":["Emin","Enes","Burak"],
    "Moderator":["Akif","Bugra","Mehmet"],
    "Yardımcı Baskan":["Kenan","Sinem","Gamze","Gökce"],
    "Baskan":["Fethi","Ethem","Nebi","Arif"]}

yetki = "Uyeler","Moderator","Yardımcı Baskan","Baskan"
isim = "kisinin adıdır"


while True:
    islem =int(input("1) Kisi Kaldır\n2) Kisi Ekle\n3) Sistemden Cık\nYapmak Istediginiz Islemi Seciniz:"  ))
    if islem == 1:
        yetki == input("Yetkiyi Yazınız: (Uyeler,Moderator,Yardımcı Baskan...) :")
        if yetki == "Uyeler": 
            print(Ekip["Uyeler"])  
            isim = input("Kaldırmak istediginiz uyenin takma adını giriniz:")
            Ekip["Uyeler"].remove(isim)
         

