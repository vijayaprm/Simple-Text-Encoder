import unittest

class TestEncryption(unittest.TestCase):
    
    def setUp(self):                            
        self.mymsg = 1                      # assigned mymsg to pass the first unit
    
    #we will do all the tests here
    #Test 1 checking if value is assignmed to the argument mymsg 
    def test_inputExists(self):
        self.assertIsNotNone(self.mymsg)        #mymsg means mymessage

    #Test 2 to confirm if mymsg is of type str
    def test_inputType(self):
        self.assertIsInstance(self.mymsg, str)
        

if __name__ == "__main__":
    unittest.main()
