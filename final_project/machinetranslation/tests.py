from translator import  *
import unittest

print("\n2 tests for each method")
print(english_to_french("what is your name"))
print(english_to_french("how are you"))

print(french_to_english("quel est ton nom"))
print(french_to_english("Comment allez-vous"))


print("\ntest for null input")
print(english_to_french(''))
print(french_to_english(''))

print('\nHello and Bonjour test')
print(english_to_french('Hello'))
print(french_to_english('Bonjour'))

print()


class TestenglishToFrench(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(english_to_french("what is your name"), 'Quel est votre nom?') 
        self.assertNotEqual(english_to_french("what is your name"), 'quel est ') 

class TestfrenchToEnglish(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(french_to_english("quel est ton nom"), 'What is your name') 
        self.assertNotEqual(french_to_english("quel est ton nom"), 'Who are you') 
        

unittest.main()