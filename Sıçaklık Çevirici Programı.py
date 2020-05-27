
print("""
#### Sıcaklık Çevirici Program ####
1. Celcius ---> Fahrenheit
2. Celcius ---> Kelvin
3. Fahrenheit ---> Celcius
4. Fahrenheit ---> Kelvin
5. Kelvin ---> Celcius
6. Kelvin ---> Fahrenheit                         
                           """)
selec = input("Lütfen Bir Seçim Yapın : ")
if selec == "1":
    Celcius=float(input("Celsius Sıcaklığını Giriniz: "))
    Fahrenheit=((Celcius*9) / 5) + 32
    print(Fahrenheit)
elif selec == "2":
    Celcius=float(input("Celsius Sıcaklığını Giriniz:"))
    Kelvin=(Celcius+273)
    if Kelvin < 0 :
        Kelvin =("Kelvin Sıfırın Altına Düşmez")
    print(Kelvin)
elif selec == "3":
    Fahrenheit=float(input("Fahrenheit Sıcaklığını Giriniz:"))
    Celcius=((Fahrenheit-32)*5)/9
    print(Celcius)
elif selec == "4":
    Fahrenheit=float(input("Fahrenheit Sıcaklığını Giriniz:"))
    Kelvin=(((Fahrenheit-32)*5)/9)+273
    if Kelvin < 0 :
        Kelvin =("Kelvin Sıfırın Altına Düşmez")
    print(Kelvin)
elif selec == "5":
    Kelvin=float(input("Kelvin Sıcaklığını Giriniz:"))
    Celcius=(Kelvin-273)
    print(Celcius)
elif selec == "6":
    Kelvin=float(input("Kelvin Sıcaklığını Giriniz:"))
    Fahrenheit=(((Kelvin-273)*9)/5)+32
    print(Fahrenheit)

else:
    print("Yanlis Girdiniz Tekrar Deneyin")
