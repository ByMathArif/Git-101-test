V = float(input("Gerilim Degerini Giriniz: "))


while True:
    try:
        0
        R = float(input("Direnc Degerini Giriniz:"))
        İ = V/R
        break
    except ZeroDivisionError:
        print("Direnc 0 Olamaz!!!")
print("Akım Degeriniz:"+str(İ))        


kelimeler = dict()

ingKelime = input("Ogrendiginiz kelimeyi yazınız:")
karsilik = input("Türkce Karsılıgı yazınız:")

kelimeler[ingKelime] = karsilik
for ingKelime in karsilik:
    print(kelimeler)






