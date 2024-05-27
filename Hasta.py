class Hasta():
    def __init__(self,hasta_no, ad, soyad, dogum_tarihi, hastalik, tedavi):
        self.__hasta_no=hasta_no
        self.__ad=ad
        self.__soyad=soyad
        self.__dogum_tarihi=dogum_tarihi
        self.__hastalik=hastalik
        self.__tedavi=tedavi

    def set_hasta_no(self,hasta_no):
        self.__hasta_no=hasta_no
    
    def get_hasta_no(self):
        return self.__hasta_no
    
    
    def set_ad(self,ad):
        self.__ad=ad

    def get_ad(self):
        return self.__ad
    

    def set_soyad(self,soyad):
        self.__soyad=soyad

    def get_soyad(self):
        return self.__soyad
    

    def set_dogum_tarihi(self,dogum_tarihi):
        self.__dogum_tarihi=dogum_tarihi

    def get_dogum_tarihi(self):
        return self.__dogum_tarihi
    

    def set_hastalik(self,hastalik):
        self.__hastalik=hastalik

    def get_hastalik(self):
        return self.__hastalik
    

    def set_tedavi(self, tedavi):
        self.__tedavi=tedavi

    def get_tedavi(self):
        return self.__tedavi
    
    def __str__(self):
        return f"Hasta No: {self.get_hasta_no()} Ad: {self.get_ad()} Soyad: {self.get_soyad()} Doğum Tarihi: {self.get_dogum_tarihi()} Hastalık: {self.get_hastalik()} Tedavi: {self.get_tedavi()}"
    

    def tedavi_suresi(self):
        print("Sizden istenecek tarihleri 28.11.2022 örneğindeki gibi yazınız")
        try:
            giris_tarihi=input("Hastanın Hastaneye Giriş Tarihi:").strip().split(".")
            cıkıs_tarihi=input("Hastanın Hastaneden Çıkış Tarihi:").strip().split(".")

            if int(giris_tarihi[1])==int(cıkıs_tarihi[1]):
                gunler_arasinda_fark=int(cıkıs_tarihi[0])-int(giris_tarihi[0])
                if int(cıkıs_tarihi[2])==int(giris_tarihi[2]):
                    print(f"Hatanın tedavi süresi {gunler_arasinda_fark} gündür")
                else:
                    yıllar_arasi_fark=int(cıkıs_tarihi[2])-int(giris_tarihi[2])
                    print(f"Hatanın tedavi süresi {yıllar_arasi_fark} yıl, 0 ay , {gunler_arasinda_fark} gündür")

            
            else:
                if int(cıkıs_tarihi[1])>=int(giris_tarihi[1]):
                    yıllar_arasi_fark=int(cıkıs_tarihi[2])-int(giris_tarihi[2])
                    aylar_arasi_fark=int(cıkıs_tarihi[1])-int(giris_tarihi[1])
                    gunler_arasinda_fark=int(cıkıs_tarihi[0])-int(giris_tarihi[0])
                    print(f"Hastanın tedavi süresi {yıllar_arasi_fark} yıl, {aylar_arasi_fark} ay , {gunler_arasinda_fark} gündür")
                elif int(cıkıs_tarihi[0])>=int(giris_tarihi[0]):
                    yıllar_arasi_fark=int(cıkıs_tarihi[2])-int(giris_tarihi[2])
                    aylar_arasi_fark=int(giris_tarihi[1])-int[cıkıs_tarihi[1]]
                    gunler_arasinda_fark=int(cıkıs_tarihi[0])-int(giris_tarihi[0])

        except ValueError:
            print("Geçersiz tarih formatı! Lütfen tarihleri doğru formatta girin.")
                    