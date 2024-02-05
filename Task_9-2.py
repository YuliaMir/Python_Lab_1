'''Похожие слова'''


def find_similar_words(word, words_to_compare):
    vowels = "ауоыиэяюёе"
    similar_words = []

    for compare_word in words_to_compare:
        if len(word) != len(compare_word):
            continue

        is_similar = True
        for i in range(len(word)):
            if (word[i] in vowels) != (compare_word[i] in vowels):
                is_similar = False
                break

        if is_similar:
            similar_words.append(compare_word)

    return similar_words


x = input("Укажите первое слово: ")
n = int(input("Укажите количество слов к сравнению: "))
words_to_compare = [input(f"Enter word {i + 1}: ") for i in range(n)]

similar_words = find_similar_words(x, words_to_compare)

print(f"Похожие слова'{x}':")
for word in similar_words:
    print(word)
