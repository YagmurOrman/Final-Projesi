
yapi['Maas'] = pd.to_numeric(yapi['Maaş'])       
yedi_yüzden_büyük_maas =  yapi[yapi['Maaş'] > 7000]
print('\033[1m' + 'Maaşı 7000den büyük kişiler' + '\033[0m')
print(yedi_yüzden_büyük_maas)
print("\n")

dogum_tarihi_listesi = list.yapi['Doğum Tarihi']
dogum_yili=[]

for tarih in dogum_tarihi_listesi:
    parcalanmis = tarih.split(".")
    dogum_yili.append(parcalanmis[2])

for i in range(len(dogum_yili)):
    if int(dogum_yili[i]) >= 1990:
        print(yapi.iloc[i])
    