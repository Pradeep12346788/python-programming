def count_words(sentence):
    words = sentence.split()
    return len(words)
input_sentence = "saveetha school of engineering"

number_of_words = count_words(input_sentence)
print("Number of words in the sentence:", number_of_words)
