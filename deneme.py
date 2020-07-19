class Student:
    def __init__(self, isim, soy_isim, cinsiyet, ders_notu, ders_kredisi = 2.4, toplam_kredi = 60):
        print("Student class'ı çalıştı..")


        self.isim = isim
        self.soy_isim = soy_isim
        self.cinsiyet = cinsiyet
        self.ders_notu = ders_notu
        self.ders_kredisi = ders_kredisi
        self.toplam_kredi = toplam_kredi

    def show_myself(self):
        print("İsim: " + self.isim)
        print("Soy isim: " + self.soy_isim)
        print("Cinsiyet: " + self.cinsiyet)
        print("Ders notu: " + str(self.ders_notu))
        print("Ders kredisi: " + str(self.ders_kredisi))
        print("Toplam kredi: " + str(self.toplam_kredi))


    def show_point(self):
        print(self.ders_notu * self.ders_kredisi / self.toplam_kredi)


okan = Student('Okan','Köse','Erkek',87)
okan.show_myself()
okan.show_point()


