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
        self.assertEqual(square(2), 4) # test when 2 is given as input the output is 4.
        self.assertEqual(square(3.0), 9.0)  # test when 3.0 is given as input the output is 9.0.
        self.assertNotEqual(square(-3), -9)  # test when -3 is given as input the output is not -9.


class TestfrenchToEnglish(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(double(2), 4) # test when 2 is given as input the output is 4.
        self.assertEqual(double(-3.1), -6.2) # test when -3.1 is given as input the output is -6.2.
        self.assertEqual(double(0), 0) # test when 0 is given as input the output is 0.

#unittest.main()