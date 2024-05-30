import Personel

class Hemsire(Personel.Personel):
    def __init__(self,personel_no, ad, soyad, departman, maas, calisma_saati, sertifika, hastane):
        super().__init__(personel_no, ad, soyad, departman, maas)
        self.__calisma_saati=calisma_saati
        self.__sertifika=sertifika
        self.__hastane=hastane

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
        
    def __str__(self):
        return f"{super().__str__()}, Calışma Saati: {self.__calisma_saati}, Sertifika: {self.__sertifika}, Hastane: {self.__hastane}"
        
    def maas_artirir(self):
        maas=int(self.get__maas)
        maas_arttirma_orani=25
        yeni_maas=maas*(1+maas_arttirma_orani/100)