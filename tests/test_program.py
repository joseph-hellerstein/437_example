import sys
sys.path.insert(0, '/Users/jlheller/home/Technical/repos/437_example/src')
from example.program import hello
import unittest

class TestFunctions(unittest.TestCase):

    def testHello(self):
        result = hello()
        self.assertTrue(result == 'goodbye')


    def testHello1(self):
        result = hello()
        self.assertTrue(result == 'hello')

if __name__ == '__main__':
  unittest.main()


