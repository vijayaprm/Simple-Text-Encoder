import unittest

def msgEncrypt(mymsg):
    return 0

class TestEncryption(unittest.TestCase):
    
    def setUp(self):                            
        self.mymsg = ""                      # assigned mymsg to pass the first unit
    
    #we will do all the tests here
    #Test 1 checking if value is assignmed to the argument mymsg 
    def test_inputExists(self):
        self.assertIsNotNone(self.mymsg)        #mymsg means mymessage

    #Test 2 to confirm if mymsg is of type str
    def test_inputType(self):
        self.assertIsInstance(self.mymsg, str)
        
    #Test 3 to check if msgEncrypt function returns something or not
    def test_checkfunction(self):
        self.assertIsNotNone(msgEncrypt(self.mymsg))

if __name__ == "__main__":
    unittest.main()
