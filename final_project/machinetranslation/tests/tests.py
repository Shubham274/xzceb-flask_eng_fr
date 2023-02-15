import unittest

from translator import englishToFrench, frenchToEnglish

class TestEnglishToFrench(unittest.TestCase):
    def test_translation(self):
        self.assertEqual(englishToFrench("Hello"),"Bonjour")

    def test_null(self):
        self.assertEqual(englishToFrench(""),"")


class TestFrenchToEnglish(unittest.TestCase):
    def test_translation(self):
        self.assertEqual(frenchToEnglish("Bonjour"),"Hello")

    def test_null(self):
        self.assertEqual(frenchToEnglish(""),"")

if __name__ == '__main__':
    unittest.main()
