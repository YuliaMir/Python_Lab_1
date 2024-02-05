'''Произвести частотный анализ'''


def frequency_analysis(text):
    text = text.lower()
    freq_dict = {}

    for char in text:
        if char.isalnum() or char.isspace():
            freq_dict[char] = freq_dict.get(char, 0) + 1

    sorted_freq = sorted(freq_dict.items(), key=lambda x: (-x[1], x[0]))

    print("Character - Frequency")
    for i in range(10):
        if i < len(sorted_freq):
            print(f"{sorted_freq[i][0]} - {sorted_freq[i][1]}")


text = "Томаты и помирдоры"
print(frequency_analysis(text))
