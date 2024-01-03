## Girilen sayı 100'den büyük mü?

#sayı gir

girdi = int(input("Sayı girin: "))

#100'den büyük mü?

if(girdi > 100):
    print(f"Girilen sayı 100'den büyüktür.")
elif(girdi == 100):
    print(f"Sayı 100'e eşittir.")
else:
    print("Girilen sayı 100'den küçüktür")

input()