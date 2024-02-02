'''Коррекция генетического кода'''


def change_gens(s):
    gens = list(s)
    i = 0
    while i < len(gens) - 1:
        if (gens[i] == 'А' and gens[i + 1] == 'Г') or (gens[i] == 'Г' and gens[i + 1] == 'А'):
            gens[i], gens[i + 1] = gens[i + 1], gens[i]
            i += 2
        elif (gens[i] == 'Ц' and gens[i + 1] == 'Т') or (gens[i] == 'Т' and gens[i + 1] == 'Ц'):
            gens.insert(i + 1, 'А')
            gens.insert(i + 2, 'Г')
            i += 3
        else:
            i += 1
    return ''.join(gens)


print(change_gens(input()))
