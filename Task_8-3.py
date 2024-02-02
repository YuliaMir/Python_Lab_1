'''Сортировка по количеству уникальных букв '''


words = ["app", "ban", "original", "pull", "grass", "kiss"]

sorted_words = sorted(words, key=lambda word: (-len(set(word)), word))

print(sorted_words)