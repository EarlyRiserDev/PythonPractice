import unittest

class Test_Class(unittest.TestCase):
    def test_add2(self):
        self.assertEqual((1+5),6)
    def test_substract2(self):
        self.assertEqual((5-2),3)


if __name__ =="__main__":
    unittest.main()
    
    
