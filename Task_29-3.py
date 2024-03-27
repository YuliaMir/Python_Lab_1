'''Напишите функцию, которая проверяет, являются ли два слова изоморфными.
Два слова изоморфны, если буквам одного слова можно сопоставить (map)
буквам другого слова.
True:
CBAABC DEFFED
XXX YYY
RAMBUNCTIOUSLY THERMODYNAMICS
False:
AB CC
XXY XYY
ABAB CD'''


def isomorphic_words(word1, word2):
    if len(word1) != len(word2):
        return False

    mapping = {}
    used_chars = set()

    for char1, char2 in zip(word1, word2):
        if char1 not in mapping:
            if char2 in used_chars:
                return False
            mapping[char1] = char2
            used_chars.add(char2)
        elif mapping[char1] != char2:
            return False

    return True


# Test cases
print(isomorphic_words('CBAABC', 'DEFFED'))
print(isomorphic_words('XXX', 'YYY'))
print(isomorphic_words('RAMBUNCTIOUSLY', 'THERMODYNAMICS'))
print(isomorphic_words('AB', 'CC'))
print(isomorphic_words('XXY', 'XYY'))
print(isomorphic_words('ABAB', 'CD'))
