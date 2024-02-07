'''Есть текстовый файл 'test1.txt'. Надо прочитать содержимое этого файла и
создать файл 'test2.txt'. В нем должны быть строчки из первого файла, но в
обратном порядке. В каждой строке должен быть поменян порядок слов на
противоположный.'''


with open('test.txt', 'r') as file:
    lines = file.readlines()

with open('test1.txt', 'w') as file:
    for line in reversed(lines):
        words = line.split()
        reversed_line = ' '.join(reversed(words))
        file.write(reversed_line + '\n')

