import unittest

class Test_Class(unittest.TestCase):
    def test_add(self):
        self.assertEqual((3+5),8)
    def test_substract(self):
        self.assertEqual((5-3),2)


if __name__ =="__main__":
    unittest.main()
    
    
