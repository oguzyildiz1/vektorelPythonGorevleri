#istenien sayıya kadar çift sayıları yazan program

sayi = int(input("Sayi? "))
sayma = 2

while sayma <= sayi:
    if sayma %2 != 0:
        sayma+=1
        continue
    print(sayma,end=",")
    sayma +=1

