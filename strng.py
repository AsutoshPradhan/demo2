import unittest 
  
class TestStringMethods(unittest.TestCase): 
      
    def setUp(self): 
        pass

  
    # Returns True if the string is in upper case. 
    def test_upper(self):         
        self.assertEqual('foo'.upper(), 'FOO') 
  
    def test_isupper(self):         
        self.assertTrue('FOO'.isupper()) 
        self.assertFalse('Foo'.isupper())



if __name__ == '__main__': 
    unittest.main() 

