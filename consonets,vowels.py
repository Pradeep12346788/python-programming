def count_vowels_and_consonants(input_string):
    vowels = "aeiouAEIOU"
    vowel_count = 0
    consonant_count = 0

    for char in input_string:
        if char.isalpha():
            if char in vowels:
                vowel_count += 1
            else:
                consonant_count += 1

    return vowel_count, consonant_count

input_str = "python programming"
vowels, consonants = count_vowels_and_consonants(input_str)
print("Number of vowels:", vowels)
print("Number of consonants:", consonants)
