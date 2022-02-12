from fernet_tool import FernetTool
import unittest

class TestFernetTool(unittest.TestCase):
    def test_encrypt(self):
        f = FernetTool(password='123')
        encrypted = f.encrypt('abc')
        decrypted = f.decrypt(encrypted.decode())
        self.assertEqual('abc', decrypted.decode())

if __name__ == '__main__':
    unittest.main()


