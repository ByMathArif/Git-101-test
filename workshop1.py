sayi1 = 10
sayi2 = 20
sayi3 = 30

if sayi1 > sayi2 + sayi3 :
    print(" En Büyük Sayı1")
if sayi2 > sayi1 + sayi3 :
    print(" En Büyük Sayı2")
if sayi3 > sayi2 + sayi1 :
    print(" En Büyük Sayı3")

if sayi1 == sayi2 == sayi3 :
    print("Sayılar Aynı")

if sayi1 ==  sayi2 + sayi3 :
    print("Sayı1 Zaten Büyük" )
    if sayi2 > sayi3 :
        print("Sayı3 En Küçük")
    else:
        print("Sayı2 En Küçük")

if sayi2 == sayi1 + sayi3 : 
    print("Sayı2 Zaten Büyük")
    if sayi1 > sayi3 :
        print("Sayı3 En Küçük")
    else:
        print("Sayı1 En Küçük")
        
if sayi3 == sayi2 + sayi1 :
    print("Sayi3 Zaten Büyük")
    if sayi2 > sayi1 : 
        print("Sayı1 En Küçük")
    else:
        print("Sayı2 En Küçük")




