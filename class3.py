from class3_0 import *
import datetime

def funct9():

    c4 = Class1()
    s = c4.funct3()

    return "funct9 " + s

class Class4(Class2):

    def funct10(self):
        s = self.funct4()
        return "funct10 " + s

class Class6(Class1):

    def funct12(self):
        s = self.funct4()
        return "funct12 " + s

class Class7():

    def funct13(self):
        c6 = Class6()
        s = c6.funct4()
        s2 = c6.funct12()
        return "funct13 " + s + s2

def funct14():
    t = datetime.datetime.now()
    return "funct14" + t.strftime(" %Y %b  %d ")

class Class8():

    def funct15(self):
        t = datetime.datetime.now()
        return "funct15" + t.strftime(" %Y %b  %d ")

    def funct16(self):
        t = Class3.now()
        return "funct16 " + t


print(funct9())

c4 = Class4()
print(c4.funct10())

c6 = Class6()
print(c6.funct12())
c7 = Class7()
print(c7.funct13())
print(funct14())
c8 = Class8()
print(c8.funct15())
print(c8.funct16())
