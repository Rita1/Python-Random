import unittest
import re

class Parser():

    def parse(to_parse):
        #parser = re.compile("([0-9]+?('.'[0-9]*)?)")
        parser = re.compile("([0-9]+?('.'[0-9]*)?)|(([.][0-9]*)?)")
        result = parser.match(to_parse)
        #print(result, result.string)
        return result


class TestMyClass(unittest.TestCase):

    def test_parse9(self):

        result = Parser.parse("9")
        print("9", result)
        self.assertFalse(result.span()[1] == 0)

    def test_parse1000(self):

        result = Parser.parse("1000")
        print("1000", result)
        self.assertFalse(result.span()[1] == 0)

    def test_parse1_21(self):

        value = "1.21"
        result = Parser.parse(value)
        print("1.21", result)
        self.assertFalse(result.span()[1] == 0)

    def utest_parse_dot(self):

        value = "."
        result = Parser.parse(value)
        print(".",result)
        self.assertFalse(result.span()[1] == 0)

    def test_parse_dot21(self):

        value = ".21"
        result = Parser.parse(value)
        print(".21",result)
        self.assertFalse(result.span()[1] == 0)

    def test_parse_tralialia(self):

        value = "tralialia"
        result = Parser.parse(value)
        print("tralialia", result)
        self.assertTrue(result.span()[1] == 0)


if __name__ == '__main__':
    unittest.main()