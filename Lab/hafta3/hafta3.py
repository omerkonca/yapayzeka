# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#Soru1
akts=int(input("Akts'nizi giriniz:"))
kredi=int(input("Kredinizi giriniz:"))

if(akts>=240 and kredi>=180):
    print("Mezun Oldunuz. Tebrikler...")
else:
    print("Maalesef mezun olamıyorsunuz !!")
    

#Soru2
NormalBiletFiyat=150
KoltukCheck= 35
BufeCheck= 75
AracKiralama=250
ExtraBagaj=15

print("Yapılacak İşlemi Seçin.")
print("=======================")
print("1.Normal Bilet")
print("2.Bilet ve Koltuk Check")
print("3.Bilet ve Bufe Check")
print("4.Bilet ve Araç Kiralama")
print("5.Bilet ve Extra Bagaj")
print("6.Tüm Hizmetler")
 
# Kullanıcıdan Seçim İsteme
secim = input("Seçiminiz (1/2/3/4/5/6):")

if secim == '1':
   Bagaj=int(input("Bagajınızı giriniz:")) 
   if(Bagaj>50):
       print("Bagajınız fazla. Extra ücret ödemeniz gerekir. Extra Ücret 15 TL")
       cevap=input("Cevabınız:")
       if(cevap=="evet" or cevap=="Evet"):
           toplam=NormalBiletFiyat+ExtraBagaj
           print("Bizi tercih ettiğiniz için teşekkür eder iyi günler dileriz.Toplam Ödemeniz:",toplam)               
       else:
            print("Bilet Kesme İşlemi Gerçekleştirilmemiştir.!")
   else:
        print("Bizi tercih ettiğiniz için teşekkür eder iyi günler dileriz.Toplam Ödemeniz:",NormalBiletFiyat)
elif secim=='2':
    Bagaj=int(input("Bagajınızı giriniz:"))
    if(Bagaj>50):
       print("Bagajınız fazla. Extra ücret ödemeniz gerekir. Extra Ücret 15 TL")
       cevap=input("Cevabınız:")
       if(cevap=="evet" or cevap=="Evet"):
           toplam=NormalBiletFiyat+ExtraBagaj+KoltukCheck
           print("Bizi tercih ettiğiniz için teşekkür eder iyi günler dileriz.Toplam Ödemeniz:",toplam)               
       else:
            print("Bilet Kesme İşlemi Gerçekleştirilmemiştir.!")
    else:
        toplam= NormalBiletFiyat+KoltukCheck
        print("Bizi tercih ettiğiniz için teşekkür eder iyi günler dileriz.Toplam Ödemeniz:",toplam)
elif secim=='3':
    Bagaj=int(input("Bagajınızı giriniz:"))
    if(Bagaj>50):
       print("Bagajınız fazla. Extra ücret ödemeniz gerekir. Extra Ücret 15 TL")
       cevap=input("Cevabınız:")
       if(cevap=="evet" or cevap=="Evet"):
           toplam=NormalBiletFiyat+ExtraBagaj+BufeCheck
           print("Bizi tercih ettiğiniz için teşekkür eder iyi günler dileriz.Toplam Ödemeniz:",toplam)               
       else:
            print("Bilet Kesme İşlemi Gerçekleştirilmemiştir.!")
    else:
        toplam= NormalBiletFiyat+BufeCheck
        print("Bizi tercih ettiğiniz için teşekkür eder iyi günler dileriz.Toplam Ödemeniz:",toplam)

elif secim=='4':
    Bagaj=int(input("Bagajınızı giriniz:"))
    if(Bagaj>50):
       print("Bagajınız fazla. Extra ücret ödemeniz gerekir. Extra Ücret 15 TL")
       cevap=input("Cevabınız:")
       if(cevap=="evet" or cevap=="Evet"):
           toplam=NormalBiletFiyat+ExtraBagaj+AracKiralama
           print("Bizi tercih ettiğiniz için teşekkür eder iyi günler dileriz.Toplam Ödemeniz:",toplam)               
       else:
            print("Bilet Kesme İşlemi Gerçekleştirilmemiştir.!")
    else:
        toplam= NormalBiletFiyat+AracKiralama
        print("Bizi tercih ettiğiniz için teşekkür eder iyi günler dileriz.Toplam Ödemeniz:",toplam)

elif secim=='5':
        toplam= NormalBiletFiyat+ExtraBagaj
        print("Bizi tercih ettiğiniz için teşekkür eder iyi günler dileriz.Toplam Ödemeniz:",toplam)
    
    
elif secim=='6':
        toplam= NormalBiletFiyat+BufeCheck+ KoltukCheck+ AracKiralama+ ExtraBagaj
        print("Bizi tercih ettiğiniz için teşekkür eder iyi günler dileriz.Toplam Ödemeniz:",toplam)    
    
#Soru3

Aylar={1:"Ocak",2:"Şubat",3:"Mart",4:"Nisan",5:"Mayıs",6:"Haziran",7:"Temmuz",8:"Ağustos",
       9:"Eylül",10:"Ekim",11:"Kasım",12:"Aralık"}

for i in range(1,12,3):
    print(Aylar[i])


    


    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    