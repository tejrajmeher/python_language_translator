from translator import  *


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