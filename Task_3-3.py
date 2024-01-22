'''На вход подается предложение из нескольких слов. Слова разделены пробелами. Напечатать все самые длинные слова.'''

s = str(input())

marks = '''!()-[]{};?@#$%:'"\\,./^&amp;*_'''

for x in s:
    if x in marks:
        opt_str = s.replace(x, "")


words = opt_str.split()
longest_word_length = max(len(word) for word in words)
longest_words = [word for word in words if len(word) == longest_word_length]

for word in longest_words:
    print(word)


