import datetime

def func1():
    s = "func1"
    return s


def func2():
    s = func1()
    return "func2 " + s


class Class1:

    def funct3(self):
        return "funct3"

    def funct4(self):
        s = self.funct3()
        return "funct4 " + s

class Class2(Class1):

    def funct5(self):
        s = self.funct4()
        return "funct5 " + s


class Class5(Class2):

    def funct11(self):
        s = self.funct4()
        s1 = self.funct3()
        return "funct11 " + s + s1


class Class3:

    def funct6(self):
        s = Class1.funct3(self) #veikia nes self nenaudoja
        return "funct6 " + s

    def funct7(self):
        c11 = Class1()
        s = c11.funct4()
        return "funct7 " + s

    def funct8(self):
        c2 = Class2()
        s = c2.funct4()
        return "funct8 " + s

    def now():
        t = datetime.datetime.now()
        return t.strftime(" %Y %b  %d ")


print ( func1() )
print ( func2() )

c1 = Class1()
print ( c1.funct3() )
print ( c1.funct4() )

c2 = Class2()

print ( c2.funct5() )

c3 = Class3()

print ( c3.funct6() )

print ( c3.funct7() )
print ( c3.funct8() )

c5 = Class5()
print ( c5.funct11() )
