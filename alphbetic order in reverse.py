def sort_letters_reverse(word):
    letters = list(word)
    letters.sort(reverse=True)
    sorted_word = ''.join(letters)
    
    return sorted_word

word = "pradeep"
sorted_word = sort_letters_reverse(word)
print(f"Original word: {word}")
print(f"Sorted in reverse alphabetical order: {sorted_word}")
