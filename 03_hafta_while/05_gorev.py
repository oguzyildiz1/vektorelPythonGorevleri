#boşluk girene kadar tüm sayıların ortalamasını alan program

def is_integer(n):
    try:
        int(n)
    except ValueError:
        return False
    else:
        return True
    
# def ortalama_al(n):
#     sayi = 


print("****     Girilen tüm sayıların ortalamasını alır    ****")
print("**** Çıkmak için tek boşluk bırakıp enter'a basınız ****")

sayi = 0
sayac = 0

while sayi!=" ":
    sayi = input("Sayi? ")
    
    if is_integer(sayi) == False: # string olarak harf mi girildi onu kontrol ediyor.
        print("Sayı girmediniz. Tekrar deneyin")
    elif sayac < 1: #değilse int değerine çeviriyor.
        sayi = int(sayi)
        sayi2 = input("Sayi? ") # sayac ilk iki sayının girilmesini sağlıyor
        if is_integer(sayi2) == False: # string olarak harf mi girildi onu kontrol ediyor.
            print("Sayı girmediniz. Tekrar deneyin")
        else:
            sayi2 = int(sayi2) 
            print("Ortalaması ", (sayi+sayi2)/2) #ilk iki sayının ortalamasını yazıyor
            sayac += 1
            print(sayac, "sayac")
    else: #bu kod bloğunda devam edilecek
        sayi = int(sayi)
        sayi2 = sayi + sayi2
        print("Toplam:",sayi2,"\tOrtalaması",sayi2 / 2)

#devam edilecek


        

    
    

