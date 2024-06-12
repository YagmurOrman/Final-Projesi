#Doktor.py
import Personel 

class Doktor(Personel.Personel):
    def __init__(self, personel_no, ad, soyad, departman, maas, uzmanlik, deneyim_yili, hastane):
        super().__init__(personel_no, ad, soyad, departman, maas)#Parent class'tan kullanılıcak değerler alınır
        #Değişkenler private tanımlanır
        self.__uzmanlik = uzmanlik
        self.__deneyim_yili = deneyim_yili
        self.__hastane = hastane

# getter ve setter metodları yardımıyla private verilere erişim sağlanır
    def set_uzmanlik(self, uzmanlik):
        self.__uzmanlik = uzmanlik

    def get_uzmanlik(self):
        return self.__uzmanlik

   
    def set_deneyim_yili(self, deneyim_yili):
        self.__deneyim_yili = deneyim_yili

    def get_deneyim_yili(self):
        return self.__deneyim_yili
    

    def set_hastane(self, hastane):
        self.__hastane = hastane

    def get_hastane(self):
        return self.__hastane


    def maas_artirir(self):# Yüzde 25 oranında doktorların maaşları arttırılır
        maas_arttirma_orani=25
        yeni_maas=int(self.get_maas())*(1+maas_arttirma_orani/100)
        return yeni_maas

    
    def __str__(self):#Ekrana yazdırma işlemi için kullanılır
        return f"{super().__str__()}, Uzmanlık: {self.__uzmanlik}, Deneyim Yılı: {self.__deneyim_yili}, Hastane: {self.__hastane},  Maaş artışı sonucu oluşan maaş: {self.maas_artirir()}"