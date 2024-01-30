#finding factoriel of a number
factoriel = 1
#def fonksiyonu
def find_factoriel(para1, factoriel):
    #bulunca döndur 
    #base case
    factoriel *= para1

    if para1 == 1:
        return factoriel
    
    return find_factoriel(para1-1, factoriel)
    #buluna kadar recursive


#girdi
sayi = int(input("Tam sayı? "))
print("Factoriel:", find_factoriel(sayi, factoriel))