from hello_world import *

from unittest import TestCase


class TestHello(TestCase):

    def test_hello_world(self):
        result = Hello.hello_world(self)
        self.assertEqual(result, "Hello World")

    def test_hello2(self):
        
        H = Hello2()
        result = H.hello2()
        self.assertEqual(result, "Hello World")
