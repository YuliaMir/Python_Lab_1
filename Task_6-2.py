'''Книги прочитанные двумя учениками'''

s1 = input().split(',')
s2 = input().split(',')

tes1 = set(s1)
tes2 = set(s2)

books = list(tes1.intersection(tes2))
print(len(books))

