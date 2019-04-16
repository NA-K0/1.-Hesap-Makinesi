import random

max_deger=int(input("max deger giriniz\n"))
min_deger=int(input("min deger giriniz\n"))
parola_uzunluk=random.randint(min_deger,max_deger)
alfabe="abcdefghijklmnoprstuvyzwx"
alfabe=(alfabe.upper() + alfabe.lower())
sayi="0123456789"
karakter=".,@!""$"

karakter1=input("Karakter olsun mu ? (E/H):")
if(karakter1=="E"):
   sayi1=input("Sayi olsun mu ? (E/H):")
   if(sayi1=="E"):
     alfabe1=input("alfabe olsun mu? (E/H):")
     if(alfabe1=="E"):
       liste=list(alfabe+sayi+karakter)
       rand = (random.sample(liste,parola_uzunluk))
       print(*rand, sep="")
     else:
       if(sayi1=="E"):
        liste=list(sayi+karakter)
        rand=(random.sample(liste,parola_uzunluk))
        print(*rand, sep="")
   else:
     alfabe1=input("alfabe olsun mu? (E/H):")
     if(alfabe1=="E"):
       liste=list(alfabe+karakter)
       rand = (random.sample(liste,parola_uzunluk))
       print(*rand, sep="")
     else:
       liste=list(karakter)
       rand = (random.sample(liste,parola_uzunluk))
       print(*rand, sep="")


else:
   sayi1=input("Sayi olsun mu ? (E/H):")
   if(sayi=="E"):
     alfabe=input("alfabe olsun mu? (E/H):")
     if(alfabe=="E"):
       liste=list(alfabe+sayi)
       rand = (random.sample(liste,parola_uzunluk))
       print(*rand, sep="")
     else:
       liste=list(sayi)
       rand=(random.sample(liste,parola_uzunluk))
       print(*rand, sep="")
   else:
     alfabe=input("alfabe olsun mu? (E/H):")
     if(alfabe=="E"):
       liste=list(alfabe)
       rand = (random.sample(liste,parola_uzunluk))
       print(*rand, sep="")
     else:
       print("şifre üretilemedi!")
