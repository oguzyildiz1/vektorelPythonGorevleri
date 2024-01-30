#date tarihi ile kullanıcı girdileri
import datetime as d
import time as t

ad = input("Adınız? ")
soyad = input("Soyadınız? ")
telNo = input("Telefon? ")
tarih = d.datetime.now()

dosya = open("rehber.dat","w")
dosya.write(ad + "\n")
dosya.write(soyad + "\n")
dosya.write(telNo + "\n")
dosya.write("Tarih : "+tarih.strftime("%Y-%m-%d %H:%M"))
dosya.close()

