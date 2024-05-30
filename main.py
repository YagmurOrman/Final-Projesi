import pandas as pd
import numpy as np
import Personel
import Hasta
import Hemsire
import Doktor

personel=Personel.Personel("788", "Ekin" , "Sözüçetin", "Temizlik Personeli", "4000")
print(str(personel))

personel1=Personel.Personel("752", "Sevgi", "Ural", "Kat Sekreteri",  "4350")
print(str(personel1))

doktor=Doktor.Doktor("5247", "İlker Batı", "Cambaz", "Cerrahi", "28000", "Kalp Damar", "12", "Yıldız Özel Hastanesi")
print(str(doktor))

doktor1=Doktor.Doktor("5786", "Selinay", "Doğan", "Dermatoloji", "18750", "Dermatoloji"," 3 ", "Devlet Hastanesi")
print(str(doktor1))

doktor2=Doktor.Doktor("5842", "Batuhan", "Durmaz", "Cerrahi", "20000" , "Genel Cerrahi", "18", "Tunguz Bayar Hastanesi")
print(str(doktor2))

hemsire=Hemsire.Hemsire("4245", "Aşkın", "Yavuzalp", "Ortopedi", "6500", "45" ,"Okul Hemşireliği", "Tuğkan Çavuşoğlu Hastanesi")
print(str(hemsire))

hemsire1=Hemsire.Hemsire("4587", "Damla", "Yılmaz","Pediatri", "3500", "35", "Yoğun Bakım" ,"Devlet Hastanesi")
print(str(hemsire1))

hemsire2=Hemsire.Hemsire("4558", "Sanem", "Dalgakıran", "Yenidoğan Yoğun Bakım", "4000", "38", "CNOR", "Kemal Kırımçak Devlet Hastanesi")
print(str(hemsire2))

hasta=Hasta.Hasta("6602","Gökalp", "Kandemir", "26.02.1998", "Bulaşıcı Hastalık", "Normal Tedavi")
print(str(hasta))

hasta1=Hasta.Hasta("6500", "Çağrı Tuna", "Naldöken", "23.11.2011", "Cilt Hastalığı ", "Özel Tedavi")
print(str(hasta1))

hasta2=Hasta.Hasta("6248", "Mutlu Savaş", "Dümen", "12.07.1955", "Akut Hastalık", "Normal Tedavi")
print(str(hasta2))
print("\n")

kisisel_veriler = {
    "Personel No": [personel.get_personel_no(), personel1.get_personel_no(), doktor.get_personel_no(), doktor1.get_personel_no(),
                    doktor2.get_personel_no(), hemsire.get_personel_no(), hemsire1.get_personel_no(), hemsire2.get_personel_no(), np.nan,np.nan ,np.nan],

    "Hasta No": [np.nan ,np.nan, np.nan, np.nan ,np.nan ,np.nan , np.nan, np.nan, hasta.get_hasta_no(), hasta1.get_hasta_no(), hasta2.get_hasta_no()],

    "Ad": [personel.get_ad(), personel1.get_ad(), doktor.get_ad(), doktor1.get_ad(), doktor2.get_ad(),
            hemsire.get_ad(), hemsire1.get_ad(), hemsire2.get_ad(),hasta.get_ad(), hasta1.get_ad(), hasta2.get_ad() ],

    "Soyad": [personel.get_soyad(), personel1.get_soyad(), doktor.get_soyad(), doktor1.get_soyad(), doktor2.get_soyad(),
            hemsire.get_soyad(), hemsire1.get_soyad(), hemsire2.get_soyad(), hasta.get_soyad(), hasta1.get_soyad(), hasta2.get_soyad()], 

    "Departman": [personel.get_departman(), personel1.get_departman(), doktor.get_departman(), doktor1.get_departman(), doktor2.get_departman(),
                  hemsire.get_departman(), hemsire1.get_departman(), hemsire2.get_departman(), np.nan, np.nan, np.nan],

    "Maas":[personel.get_maas(), personel1.get_maas(), doktor.get_maas(), doktor1.get_maas(), doktor2.get_maas(), hemsire.get_maas(),
             hemsire1.get_maas(), hemsire2.get_maas(), np.nan , np.nan , np.nan ],

    "Hastane":[np.nan, np.nan, doktor.get_hastane(), doktor1.get_hastane(), doktor2.get_hastane(), hemsire.get_hastane(), hemsire1.get_hastane(),
               hemsire2.get_hastane(), np.nan, np.nan, np.nan],

    "Çalışma Saati":[np.nan, np.nan, np.nan , np.nan, np.nan, hemsire.get_calisma_saati(), hemsire1.get_calisma_saati(), hemsire2.get_calisma_saati(), 
                     np.nan, np.nan, np.nan],
    "Sertifika":[np.nan, np.nan, np.nan , np.nan, np.nan, hemsire.get_sertifika(), hemsire1.get_sertifika(), hemsire2.get_sertifika(), 
                     np.nan, np.nan, np.nan],
    "Uzmanlık":[np.nan, np.nan, doktor.get_uzmanlik(), doktor1.get_uzmanlik(), doktor2.get_uzmanlik(), np.nan, np.nan, np.nan,np.nan, np.nan, np.nan],

    "Deneyim Yılı":[np.nan,  np.nan, doktor.get_deneyim_yili(), doktor1.get_deneyim_yili(), doktor2.get_deneyim_yili(), np.nan, np.nan, np.nan,np.nan, np.nan, np.nan],

    "Hastalik":[np.nan,  np.nan, np.nan, np.nan ,np.nan ,np.nan , np.nan, np.nan,hasta.get_hastalik(), hasta1.get_hastalik(), hasta2.get_hastalik()],

    "Tedavi":[np.nan,  np.nan, np.nan, np.nan ,np.nan ,np.nan , np.nan, np.nan, hasta.get_tedavi(), hasta1.get_tedavi(), hasta2.get_tedavi()]
}

try:
    yapi = pd.DataFrame(kisisel_veriler).fillna(0)
    print(yapi)
except Exception as e:
    print("DataFrame oluşturulurken bir hata oluştu:", e)