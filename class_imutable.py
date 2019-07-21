import unittest

class myClass:

    def __init__(self, my_string, my_list):

        self.my_string = my_string
        self.my_list = my_list.copy()

    def get_string(self):
        return self.my_string

    def get_my_list(self):
        return self.my_list

    def __str__(self):
        return str(self.my_string) + " " + str(self.my_list)



class TestMyClass(unittest.TestCase):

    def test_mutable2(self):

        list_of_class = []
        my_list = []

        for i in range(2):
            my_list += str(i)
            list_of_class.append(myClass("String",my_list))

        self.assertFalse(list_of_class[0].get_my_list() == list_of_class[1].get_my_list())

    def test_mutable4(self):

        c1 = myClass("String1",["A1","B1","C1"])
        my_list = c1.get_my_list()
        c2 = myClass("String2", my_list)
        my_list[0] = "D1"

        #print(c1)
        #print(c2)
        self.assertFalse(c1.get_my_list() == c2.get_my_list())

    def test_mutable6(self):

        c1 = myClass("String1", ["A1", "B1", "C1"])
        my_list = c1.get_my_list()

        c2 = myClass("String2", my_list)
        my_list.append("D1")

        print(c1, c2)
        self.assertFalse(c1.get_my_list() == c2.get_my_list())



if __name__ == '__main__':
    unittest.main()