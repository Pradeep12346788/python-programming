def count_vowels(statement):
    vowels = "aeiouAEIOU"
    count = 0
    for char in statement:
        if char in vowels:
            count += 1
    return count
statement = "pradeep reddy"
num_vowels = count_vowels(statement)
print("Number of vowels:", num_vowels)
