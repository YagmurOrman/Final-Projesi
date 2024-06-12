import Personel

class Hemsire(Personel.Personel):
    def __init__(self,personel_no, ad, soyad, departman, maas, calisma_saati, sertifika, hastane):
        super().__init__(personel_no, ad, soyad, departman, maas)#Parent class'tan kullanılıcak değerler alınır
        #Değişkenler private tanımlanır
        self.__calisma_saati=calisma_saati
        self.__sertifika=sertifika
        self.__hastane=hastane
# getter ve setter metodları yardımıyla private verilere erişim sağlanır
    def set_calisma_saati(self,calisma_saati):
        self.__calisma_saati=calisma_saati

    def get_calisma_saati(self):
        return self.__calisma_saati
        

    def set_sertifika(self,sertifika):
        self.__sertifika=sertifika

    def get_sertifika(self):
        return self.__sertifika
        

    def set_hastane(self, hastane):
        self.__hastane=hastane

    def get_hastane(self):
        return self.__hastane
    
    def maas_artirir(self):# Yüzde 15 oranında doktorların maaşları arttırılır
        maas_arttirma_orani=15
        yeni_maas=int(self.get_maas())*(1+maas_arttirma_orani/100)
        return yeni_maas
        
    def __str__(self):#Ekrana yazdırma işlemi için kullanılır
        return f"{super().__str__()}, Calışma Saati: {self.__calisma_saati}, Sertifika: {self.__sertifika}, Hastane: {self.__hastane},  Maaş artışı sonucu oluşan maaş: {self.maas_artirir()}"
        
    