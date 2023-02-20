import unittest
from translator import english_to_french, french_to_english

class TestTranslator(unittest.TestCase):
    
    def test_null_input_french_to_english(self):
        self.assertEqual(french_to_english(None), None)
        
    def test_null_input_english_to_french(self):
        self.assertEqual(english_to_french(None), None)
        
    def test_hello_translation(self):
        self.assertEqual(english_to_french('Hello'), 'Bonjour')
        self.assertNotEqual(french_to_english('Bonjour'), 'Hello')
        
    def test_bonjour_translation(self):
        self.assertEqual(english_to_french('Bonjour'), 'Hello')
        self.assertNotEqual(french_to_english('Hello'), 'Bonjour')

if __name__ == '__main__':        
    unittest.main()
