import unittest
import string

def msgEncrypt(mymsg):
    check = string.ascii_letters + string.punctuation + string.digits + " "
    encryptedmsg = "".join([check[check.find(char)+1] for i,char in enumerate(mymsg)])
    #print(encryptedmsg)
    return encryptedmsg

class TestEncryption(unittest.TestCase):
    
    def setUp(self):                            
        self.mymsg = "Hello batman"                      # assigned mymsg to pass the first unit
    
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

    #Test 4 Checking if encrypted msg is of same length as of encrypted msg or not
    def test_matchLength(self):
        self.assertEqual(len(self.mymsg), len(msgEncrypt(self.mymsg)))

    #Test 5 check if input message and encrypted message is same or not
    def test_matchIO(self):
        self.assertNotIn(self.mymsg, msgEncrypt(self.mymsg))

    #Test 6 Checking if encrypted string actually shifts the characters by one or not
    def test_checkshift(self):
        check = string.ascii_letters + string.punctuation + string.digits + " "
        encryptedmsg = "".join([check[check.find(char)+1] for i,char in enumerate(self.mymsg)])
        print(encryptedmsg)
        self.assertEqual(encryptedmsg, msgEncrypt(self.mymsg))

if __name__ == "__main__":
    unittest.main()
