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
        return f"Hasta No: {self.get_hasta_no()}, Ad: {self.get_ad()}, Soyad: {self.get_soyad()}, Doğum Tarihi: {self.get_dogum_tarihi()}, Hastalık: {self.get_hastalik()}, Tedavi: {self.get_tedavi()}, Tedavi süresi: {self.tedavi_suresi()}"
    

    def tedavi_suresi(self):
        tedavi_sure_sayaci=0
        bir_kez_dondur=1
        try:
            while bir_kez_dondur==1:
                if self.get_hastalik()=="Bulaşıcı Hastalık":
                    tedavi_sure_sayaci=tedavi_sure_sayaci+4
                elif self.get_hastalik()=="Cilt Hastalığı":
                    tedavi_sure_sayaci=tedavi_sure_sayaci+14
                elif self.get_hastalik()=="Akut Hastalık":
                    tedavi_sure_sayaci=tedavi_sure_sayaci+7

                bir_kez_dondur=bir_kez_dondur+1
            
            if self.get_tedavi()=="Özel Tedavi":
                tedavi_sure_sayaci=tedavi_sure_sayaci+10
            
            if self.get_tedavi()=="Normal Tedavi":
                tedavi_sure_sayaci=tedavi_sure_sayaci+2

            return tedavi_sure_sayaci
        except Exception as e:
            print("Tedavi süresi hesaplanırken bir hata oluştu", e)






        
                    