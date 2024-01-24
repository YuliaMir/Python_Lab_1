'''Проверить являются ли два предложения анаграммами'''

x = input()
y = input()

x1 = str(x.split())
y1 = str(y.split())

x2 = "".join(c for c in x1 if c.isalpha())
y2 = "".join(c for c in y1 if c.isalpha())

dct1, dct2 = {}, {}

for k in x2:
    if k not in dct1:
        dct1[k] = 0
    dct1[k] += 1
for k in y2:
    if k not in dct2:
        dct2[k] = 0
    dct2[k] += 1
print(dct1)
print(dct2)
print(dct1 == dct2)