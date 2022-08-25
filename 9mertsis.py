# Tuple Obje Tipleri --> tuple değerleri değiştirilemez "en azından tuple halindeyken"--> 
# liste obje tipine dönüştürüp değiştirmek tupleken değiştirmemiş oluyoruz

a=()
b=tuple()
print(type(a))
print(type(b))

# Bu bizim tuple'ın değiştirilemediğinin göstergesidir 
# x=(1,2,3,4,5,6)
# x[2]=9
# print(x)

Kazanılan_Yer = "Çanakkale 18 Mart Üniversitesi Bilgisayar Mühendisliği"
print(Kazanılan_Yer)

Kazanmak_Istenilen_Yer= tuple(Kazanılan_Yer)
print(Kazanmak_Istenilen_Yer)
#Kazanmak_Istenilen_Yer = "Gebze Teknik Üniversitesi Bilgisayar Mühendisliği"
yeni = (10,20,5,6,78,52,64,163,"arif","gökçe",100,163,163,163,163,163,163,"turkiye")
print(yeni.index("gökçe"))
print(yeni.count(163))
print(yeni.__contains__("arif"))
print(yeni.__contains__(163))
print(yeni.__contains__("18 Mart Üniversitesi"))

if "turkiye" in yeni:
    print("Kültür Vardır")

#neden tuple var--> adam zaten liste obje tipi ile bunları saklayabiliyor. Neden değişmeyen bir şeye ihyiyaç duymuş:
# 1) Değişmeyen veriler isteyebilir--> Marka ismi , IP kodu , Listede değişiklik istemiyorsak...

