import unittest
import translator


class test_translation(unittest.TestCase):
    def test1(self):
        self.assertEqual(translator.english_to_french("Hello"), "Bonjour")

    def test2(self):
        self.assertEqual(translator.french_to_english("Bonjour"), "Hello")