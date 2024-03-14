def count_vowels_and_consonets(imput_string)
vowels = "aeiouAEIOU"
vowel_count=0
consonet_count=0
for char in input_string
if char.isalpha()
if char in vowels:
    vowels_count+=1
    else
    consonets_count+=1
    return vowel_count,consonet_count
input_str="python programming"
vowels,consonets=count_vowels_and consonets(input_string)
print("no of vowels:" vowels)
print("no of consonets:"consonets)
