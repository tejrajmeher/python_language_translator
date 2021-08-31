from translator import  *
import unittest

print("\n2 tests for each method")
print(englishToFrench("what is your name"))
print(englishToFrench("how are you"))

print(frenchToEnglish("quel est ton nom"))
print(frenchToEnglish("Comment allez-vous"))


print("\ntest for null input")
print(englishToFrench(''))
print(frenchToEnglish(''))

print('\nHello and Bonjour test')
print(englishToFrench('Hello'))
print(frenchToEnglish('Bonjour'))

print()


class TestenglishToFrench(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(englishToFrench("what is your name"), 'Quel est votre nom?') 
        self.assertNotEqual(englishToFrench("what is your name"), 'quel est ') 

class TestfrenchToEnglish(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(frenchToEnglish("quel est ton nom"), 'What is your name') 
        self.assertNotEqual(frenchToEnglish("quel est ton nom"), 'Who are you') 
        

unittest.main()