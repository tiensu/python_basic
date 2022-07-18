# 4. Define a function that accepts one string argument and returns number of vowels and consonants.
def count_characters(word):
    vowels=0
    consonants=0
    for i in str:
        if i in ['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U']:
            vowels = vowels + 1
        else:
            consonants = consonants + 1
    print("The number of vowels:", vowels)
    print("\nThe number of consonant:", consonants)