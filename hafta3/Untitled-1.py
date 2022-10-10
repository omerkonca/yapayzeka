
#SORU1

# sayi=int(input("Bir rakam giriniz : "))

# for i in range(11):
#     carpimdegeri=sayi*i
#     print(sayi,"x",i,"=",carpimdegeri)
#     i=+1


#SORU2



# sayi=int(input("Bir sayı giriniz : "))
# sayac=0

# while sayi>0:
#     sayi=sayi//10
#     sayac+=1

# print("Girdiginiz sayının basamak sayısı : ",sayac)


#SORU3

# sayısalDeğerler = [12, 15, 32, 42, 55, 75, 122, 132, 150, 180, 200]

# for i in sayısalDeğerler:
#     if i%5==0 and i<=150:
#         print("for ile : ",i)

# sayac=0
# while sayac<len(sayısalDeğerler):
#     if sayısalDeğerler[sayac]%5==0 and sayısalDeğerler[sayac]<=150:
#         print("while ile : ",sayısalDeğerler[sayac])
#     sayac+=1


#SORU4

# a=int(input("Bir sayı giriniz : "))
# b=int(input("Bir sayı giriniz : "))
# c=int(input("Bir sayı giriniz : "))

# sayac=0
# for i in range(a,b+1):
#     if i%c==0:
#         sayac+=1
#         print(i," sayısı ",c," sayısına tam bölünebiliyor")
# print("A ve B arasında C ye tam bölünebilen toplam sayı adedi :",sayac)



#SORU5

# deger=99
# for i in range(1,100):
#     print(i,"-",deger)
#     i+=1
#     deger-=1



#SORU6

# ip1=int(input("Ip adresi 1 : "))
# ip2=int(input("Ip adresi 1 : "))
# ip3=int(input("Ip adresi 1 : "))
# ip4=int(input("Ip adresi 1 : "))

# print("Örnek : ",ip1," ",ip2," ",ip3," ",ip4)
# for i in range(6):
#     if ip4<255:
#         ip4+=1
#         print("Çıktı : ",ip1," ",ip2," ",ip3," ",ip4)
#     else:
#         ip2+=1
#         ip3=0
#         ip4=0