#yazıyı tersten yazdırma
# for döngüsü ile
text = "Oğuzhan"
length = len(text)
for i in range(length-1,-1,-1):
    print(text[i],end=",")
