import unittest

class MyClass1:
#Siaip klase
    def __init__(self, name):
        self.name = name

class MyClass2:
#Klase, kuri turi "linka" i 1 klase

    def __init__(self, cls1):
        self.cls = cls1

    def name(self):
        return self.cls.name

    def __str__(self):
        return str(self.cls.name)

class MyClass3:
#Klase, kuri turi MyClass2 objektu set'a

    def __init__(self):
        self.my_set = []

    def add(self, cls2):

        self.my_set.append(cls2)

    def show_all(self):
        print(self.my_set)
        return self.my_set

    def __str__(self):
        to_print = [e.name() for e in self.my_set]

        return str(to_print)

class TestMyClass(unittest.TestCase):

    def test_add1(self):

        obj1 = MyClass1("A")
        obj2 = MyClass2(obj1)
        obj22 = MyClass2(obj1)

        my_class3 = MyClass3()

        my_class3.add(obj2)
        my_class3.add(obj22)

        print(my_class3)


if __name__ == '__main__':
    unittest.main()