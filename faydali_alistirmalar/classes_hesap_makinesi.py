#we are going to write a program which calculate the basic algebraic operations.

#our aim is to write this program with classes

class Hesapmakinesi:

    def __init__(self, para1=0, para2=0):

        self.firstNum = para1
        self.secNum = para2

    def toplama(self):
        total = self.firstNum + self.secNum
        return total


hm1 = Hesapmakinesi()

hm1.para1 = 5
hm1.para2 = 10

print(hm1.para1)
del hm1

try:
    print(hm1.para1)
except:
    print("nesne silinmiş.")