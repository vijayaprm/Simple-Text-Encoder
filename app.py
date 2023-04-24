import unittest

class TestEncryption(unittest.TestCase):
    #we will do all the tests here
    def test_inputExists(self):
        self.assertIsNotNone(self.mymsg)        #mymsg means mymessage

     def setUp(self):
        self.mymsg = 1                          # assigned mymsg to pass the first unit
        
if __name__ == "__main__":
    unittest.main()
