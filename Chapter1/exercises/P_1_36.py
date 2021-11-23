def word_number(words_list):
    word_count = {}
    for word in words_list:
        word_count[word] = word_count.get(word, 0) + 1
    return word_count


words = "Is a word like it is the the is word banana apple word is apple"
print(word_number(words.lower().split()))
