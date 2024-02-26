'''Напишите программу программу, которая устраняет повторение
повторение слов, т.е. результат результат должен быть следующим:
Напишите программу, которая устраняет повторение слов, т.е.
результат должен быть следующим.'''

import re
def eliminate_repetition(sentence):
    words = re.sub(r'[^\w\s]', '', sentence)
    new_words = words.split()
    unique_words = []

    for word in new_words:
        if word not in unique_words:
            unique_words.append(word)

    result = ' '.join(unique_words)
    return result


input_sentence = "Напишите программу программу которая устраняет повторение повторение слов"
output_sentence = eliminate_repetition(input_sentence)

print(output_sentence)
