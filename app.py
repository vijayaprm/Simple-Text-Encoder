import unittest

class TestEncryption(unittest.TestCase):
    #we will do all the tests here
    def test_inputExists(self):
        self.assertIsNotNone(self.mymsg)        #mymsg means mymessage


if __name__ == "__main__":
    unittest.main()
