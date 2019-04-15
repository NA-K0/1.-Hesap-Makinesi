import random
import time



while (True):
  try:
    s = str(input("Parolanızın içerisinde sayı olsunmu?.E/H"))
    if (s == "E" or s == "e"):
        sayi = True
    elif (s == "H" or s == "h"):
        sayi = False
    else:
        print("Hata! Cevabı E yada H olarak vermeniz gerekir.")
        continue

    d = str(input("Parolanın içerisinde harf olsunmu?.E/H"))
    if (d == "E" or d == "e"):
        harf = True
    elif (d == "H" or d == "h"):
        harf = False
    else:
        print("Hata! Cevabı E yada H olarak vermeniz gerekir.")
        continue

    f = str(input("Parolanın içerisinde özel karakter olsunmu?.E/H"))
    if (f == "E" or f == "e"):
        ozelkarakter = True
    elif (f == "H" or f == "h"):
        ozelkarakter = False
    else:
        print("Hata! Cevabı E yada H olarak vermeniz gerekir.")
        continue

    g = int(input("Parola minimum kaç karakter olsun?"))
    if (g <= 0):
        print("0'dan küçük sayı girmeyiniz!")
        continue
    else:
        minimum = g

    a = int(input("Parola maksimum kaç karakter olsun?"))
    if (g <= 0):
        print("0'dan küçük sayı girmeyiniz!")
        continue
    elif (a <= g):
        print("Maksimum karakter sayısı minimumdan küçük yada eşit olamaz.")
    else:
        maksimum = a
    print("Şifre yapılıyor")
    time.sleep(3)
    def rasgele (minimum , maksimum):
        if (harf == True):
            harfler = "abcdefghijklmnoprstuvyzwx"
        else:
            harfler = ""
        if (sayi == True):
            sayilar = "123456789"
        else:
            sayilar = ""
        if (ozelkarakter == True):
            ozelkarakterler = "!@#$'.,"
        else:
            ozelkarakterler = ""
        sifreuzunlugu = random.randint(minimum-1 , maksimum+1)
        harfler = harfler.upper() + harfler.lower()
        sifreicerigi = list(harfler + sayilar + ozelkarakterler)
        rasgele = (random.sample(sifreicerigi,sifreuzunlugu ))
        print(*rasgele, sep="")
    rasgele(minimum, maksimum)


  except:
      print("Bir hata oluştu yazdığınız harf sayısını kontrol ediniz.")
      continue







































