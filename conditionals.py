istenenKredi = 100000
hesap = 9450
minimumOlmasıGerekenHesap = 10000
if hesap >=minimumOlmasıGerekenHesap:
    print("Kredi Verilebilir")
    print("Ödemeler Hesaplandı")
elif hesap >=9000 and  hesap <=9500:
    print("Müdüre Sorulacak")
elif hesap >= 9501:
    print("Genel Müdüre Sorulacak")   
else:
    print("Kredi almak için bakiyeniz yetersiz")
print("işlem sonu")

