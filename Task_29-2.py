'''Напишите функцию, результатом которой является расстояние
Хемминга двух строк одинаковой длины, равное количеству
несовпадающих букв на одинаковых позициях.
Например:
abc и abc – 0
abc и abd – 1
abc и xyz - 3
Попробуйте написать эту функцию в одну строчку )'''

hamming_distance = lambda str1, str2: sum([1 for x, y in zip(str1, str2) if x != y])


print(hamming_distance('abc', 'abc'))
print(hamming_distance('abc', 'abd'))
print(hamming_distance('abc', 'xyz'))
