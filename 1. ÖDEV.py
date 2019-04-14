while True:
    istek=input("İşlemleri Görmek İstermisiniz? (evet) (hayır)" )

    if(istek == "evet") or (istek == "Evet"):
        print("İşlemler Yazdırılıyor...")
        print("**** Hesap Makinesi ****", "\nToplama İşlemi İçin (1)", "\nÇıkarma İşlemi İçim (2) ", "\nÇarpma İşlemi İçin (3)", "\nBölme İşlemi İçin (4)")
        break

    elif(istek == "hayır" or istek == "Hayır"):
        print("Programdan Çıkış Yaplıyor ...")
        break

    else:
        print("İşleminiz Anlaşılmadı Tekrar Deneyiniz..")


while True:

    if(istek == "hayır" or istek == "Hayır"):
        break

    elif(istek == "evet" or istek == "Evet"):
        print("Yapmak İstediğiniz İşlemi ve Sayıları Giriniz..")


    while True:
        a = int(input("İlk Sayınızı Giriniz"))
        b = int(input("İkinci Sayınızı Giriniz"))
        break

    while True:
        işlem = input("İşlemi Seçiniz:")

        if(işlem == "1" ):
            print(a + b)
            print("İşleminiz Tamamlandı")
            break

        elif(işlem == "2" ):
            print(a - b)
            print("İşleminiz Tamamlandı")
            break

        elif(işlem == "3"):
            print(a * b)
            print("İşleminiz Tamamlandı")
            break

        elif(işlem == "4"):
            print(a / b)
            print("İşleminiz Tamamlandı")
            break

        else:
            print("Geçersiz İşlem")
            print("Tekrar Deneyiniz")
            continue


    while True:
        işlembitti=input("Devam Edilsin Mi? (Evet) (Hayır):")
        if(işlembitti == "evet") or (işlembitti == "Evet"):
            print("İşlem Devam Ediyor")
            break

        elif(işlembitti == "hayır") or (işlembitti == "Hayır"):
            print(quit("Program Kapatılıyor.."))


        else:
            print("Geçersiz İşlem Tekrar Deneyiniz")
            continue















